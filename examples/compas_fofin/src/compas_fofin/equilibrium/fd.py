from compas.numerical import fd_numpy


__all__ = [
    'cablenet_fd_numpy'
]


def cablenet_fd_numpy(cablenet):
    """Compute the equilibrium shape of a cablenet using the force density method.

    Parameters
    ----------
    cablenet : compas_fofin.cablenet.Cablenet
        The cablenet data structure.

    """
    key_index = cablenet.key_index()

    xyz   = cablenet.get_vertices_attributes('xyz')
    edges = [(key_index[u], key_index[v]) for u, v in cablenet.edges()]
    fixed = [key_index[key] for key in cablenet.vertices_where({'is_anchor': True})]
    q     = cablenet.get_edges_attribute('q', 1.0)
    loads = cablenet.get_vertices_attributes(('px', 'py', 'pz'), (0.0, 0.0, 0.0))

    xyz, q, f, l, r = fd_numpy(xyz, edges, fixed, q, loads)

    for key, attr in cablenet.vertices(True):
        index = key_index[key]
        cablenet.set_vertex_attributes(key, 'xyz', xyz[index])
        cablenet.set_vertex_attributes(key, ('rx', 'ry', 'rz'), r[index])

    for index, (u, v, attr) in enumerate(cablenet.edges(True)):
        attr['f'] = f[index][0]
        attr['l'] = l[index][0]


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":
    pass
