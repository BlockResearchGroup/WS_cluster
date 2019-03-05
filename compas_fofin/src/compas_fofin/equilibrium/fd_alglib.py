from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from math import sqrt
from copy import deepcopy
from functools import partial

import compas

try:
    from compas.numerical._alglib._core import xalglib
except ImportError:
    compas.raise_if_ironpython()


__all__ = ['cablenet_fd_alglib']


def cross_vectors(u, v):
    return [u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0]]


def length_vector(vector):
    return sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)


def centroid_points(points):
    p = len(points)
    x, y, z = zip(*points)
    return [sum(x) / p, sum(y) / p, sum(z) / p]


def cablenet_fd_alglib(cablenet):
    """Compute the equilibrium shape of a cablenet using the force density method implemented with AlgLib.

    Parameters
    ----------
    cablenet : compas_fofin.datastructures.Cablenet
        The cablenet data structure.

    """
    key_index = cablenet.key_index()

    xyz     = cablenet.get_vertices_attributes('xyz')
    loads   = cablenet.get_vertices_attributes(('px', 'py', 'pz'))
    n       = cablenet.number_of_vertices()
    anchors = [key_index[key] for key, attr in cablenet.vertices_where({'is_anchor': True}, True)]
    fixed   = []
    fixed   = list(set(anchors + fixed))
    free    = list(set(range(n)) - set(fixed))
    ni      = len(free)
    nf      = len(fixed)
    xyzf    = [xyz[i] for i in fixed]

    adjacency = {key_index[key]: [key_index[nbr] for nbr in cablenet.vertex_neighbors(key)] for key in cablenet.vertices()}

    ij_q = {uv: cablenet.get_edge_attribute(uv, 'q', 1.0) for uv in cablenet.edges()}
    ij_q.update({(v, u): q for (u, v), q in ij_q.items()})
    ij_q = {(key_index[u], key_index[v]): ij_q[u, v] for u, v in ij_q}

    nonzero_fixed, nonzero_free = _nonzero(adjacency, fixed, free)

    CtQC = xalglib.sparsecreate(n, n)
    CitQCi = xalglib.sparsecreate(ni, ni)
    CitQCf = xalglib.sparsecreate(ni, nf)

    s = xalglib.linlsqrcreate(ni, ni)

    _update_matrices(adjacency, free, nonzero_fixed, nonzero_free, CtQC, CitQCf, CitQCi, ij_q)
    _compute_xyz_free(s, xyz, xyzf, loads, free, ni, CitQCf, CitQCi)

    p = deepcopy(loads)

    rx, ry, rz = _compute_residuals(xyz, p, n, CtQC)

    for key, attr in cablenet.vertices(True):
        index = key_index[key]
        cablenet.vertex[key]['x']  = xyz[index][0]
        cablenet.vertex[key]['y']  = xyz[index][1]
        cablenet.vertex[key]['z']  = xyz[index][2]
        cablenet.vertex[key]['rx'] = rx[index]
        cablenet.vertex[key]['ry'] = ry[index]
        cablenet.vertex[key]['rz'] = rz[index]

    for u, v in cablenet.edges():
        i, j = key_index[u], key_index[v]
        q = ij_q[i, j]
        l = cablenet.edge_length(u, v)
        f = q * l
        cablenet.set_edge_attributes((u, v), ('q', 'f', 'l'), (q, f, l))


# ==============================================================================
# helpers
# ==============================================================================


def _nonzero(adjacency, fixed, free):
    n = len(adjacency)

    j_col_free = {value: index for index, value in enumerate(free)}
    j_col_fixed = {value: index for index, value in enumerate(fixed)}
    i_nonzero_free = {i: [] for i in range(n)}
    i_nonzero_fixed = {i: [] for i in range(n)}

    fixed = set(fixed)

    for i in range(n):
        if i in fixed:
            i_nonzero_fixed[i].append((i, j_col_fixed[i]))
        else:
            i_nonzero_free[i].append((i, j_col_free[i]))

        for j in adjacency[i]:
            if j in fixed:
                i_nonzero_fixed[i].append((j, j_col_fixed[j]))
            else:
                i_nonzero_free[i].append((j, j_col_free[j]))

    return i_nonzero_fixed, i_nonzero_free


def _update_matrices(adjacency, free, nonzero_fixed, nonzero_free, CtQC, CitQCf, CitQCi, ij_q):
    xalglib.sparseconverttohash(CtQC)
    xalglib.sparseconverttohash(CitQCi)
    xalglib.sparseconverttohash(CitQCf)

    n = len(adjacency)
    ni = len(free)

    for i in range(n):
        Q = 0
        for j in adjacency[i]:
            q = ij_q[(i, j)]
            Q += q
            xalglib.sparseset(CtQC, i, j, -q)
        xalglib.sparseset(CtQC, i, i, Q)

    for row in range(ni):
        i = free[row]
        for j, col in nonzero_fixed[i]:
            xalglib.sparseset(CitQCf, row, col, xalglib.sparseget(CtQC, i, j))
        for j, col in nonzero_free[i]:
            xalglib.sparseset(CitQCi, row, col, xalglib.sparseget(CtQC, i, j))


def _compute_xyz_free(s, xyz, xyzf, loads, free, ni, CitQCf, CitQCi, selfweight=None):
    xalglib.sparseconverttocrs(CitQCi)
    xalglib.sparseconverttocrs(CitQCf)

    p = deepcopy(loads)

    if selfweight:
        sw = selfweight(xyz)
        for i in range(len(p)):
            p[i][2] -= sw[i]

    out = [[0, 0, 0] for row in range(ni)]

    b  = xalglib.sparsemm(CitQCf, xyzf, 3, out)
    bx = [p[free[row]][0] - b[row][0] for row in range(ni)]
    by = [p[free[row]][1] - b[row][1] for row in range(ni)]
    bz = [p[free[row]][2] - b[row][2] for row in range(ni)]

    xalglib.linlsqrsolvesparse(s, CitQCi, bx)
    xi, _ = xalglib.linlsqrresults(s)

    xalglib.linlsqrsolvesparse(s, CitQCi, by)
    yi, _ = xalglib.linlsqrresults(s)

    xalglib.linlsqrsolvesparse(s, CitQCi, bz)
    zi, _ = xalglib.linlsqrresults(s)

    for row in range(ni):
        index = free[row]
        xyz[index][0] = xi[row]
        xyz[index][1] = yi[row]
        xyz[index][2] = zi[row]


def _compute_residuals(xyz, p, n, CtQC):
    xalglib.sparseconverttocrs(CtQC)

    x, y, z = zip(*xyz)
    x = list(x)
    y = list(y)
    z = list(z)

    rx_ = [0] * n
    rx_ = xalglib.sparsemv(CtQC, x, rx_)
    rx  = [p[i][0] - rx_[i] for i in range(n)]

    ry_ = [0] * n
    ry_ = xalglib.sparsemv(CtQC, y, ry_)
    ry  = [p[i][1] - ry_[i] for i in range(n)]

    rz_ = [0] * n
    rz_ = xalglib.sparsemv(CtQC, z, rz_)
    rz  = [p[i][2] - rz_[i] for i in range(n)]

    return rx, ry, rz


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":
    pass
