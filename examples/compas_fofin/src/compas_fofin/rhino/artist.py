from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import compas_rhino

from compas.geometry import scale_vector
from compas.geometry import add_vectors
from compas.geometry import subtract_vectors
from compas.geometry import length_vector_sqrd

from compas_rhino.artists import NetworkArtist


__all__ = ['CablenetArtist']


class CablenetArtist(NetworkArtist):
    """Artist for the visualisation of a Cablenet in Rhino.

    Examples
    --------
    .. code-block:: python

        from compas_fofin import Cablenet
        from compas_fofin.rhino import CablenetArtist

        cablenet = Cablenet.from_json('saddle.obj')

        artist = CablenetArtist(cablenet, layer="FoFin::Cablenet")
        artist.clear_layer()
        artist.draw_vertices()
        artist.draw_edges()
        artist.update()

    """

    @property
    def cablenet(self):
        return self.datastructure

    @cablenet.setter
    def cablenet(self, cablenet):
        self.datastructure = cablenet

    def _draw_lines(self, lines):
        compas_rhino.xdraw_lines(lines,
                                 layer=self.cablenet.layer,
                                 clear=False,
                                 redraw=True)

    def _draw_cylinders(self, cylinders):
        compas_rhino.xdraw_cylinders(cylinders,
                                     layer=self.cablenet.layer,
                                     clear=False,
                                     redraw=True,
                                     cap=True)

    def _draw_spheres(self, spheres):
        compas_rhino.xdraw_spheres(spheres,
                                   layer=self.cablenet.layer,
                                   clear=False,
                                   redraw=True)

    def clear_forces(self):
        """Clear all previously drawn forces from the Rhino View."""
        guids = compas_rhino.get_objects(name="{}.force.*".format(self.cablenet.name))
        compas_rhino.delete_objects(guids)

    def draw_forces(self, compression=None, tension=None, scale=None, tol=None):
        """Draw the axial forces in the edges of the cablenet as pipes.

        Parameters
        ----------
        compression : str or tuple, optional
            Color of compression forces.
        tension : str or tuple, optional
            Color of tension forces.
        scale : float, optional
            Scale of axial forces.
        tol : float, optional
            Threshold for drawing axial forces.

        """
        self.clear_forces()

        compression = compression or self.cablenet.attributes['color.force:compression']
        tension     = tension or self.cablenet.attributes['color.force:tension']
        scale       = scale or self.cablenet.attributes['scale.force']
        tol         = tol or self.cablenet.attributes['tol.force']
        tol2        = tol**2

        lines = []
        for u, v in self.cablenet.edges():
            f = self.cablenet.get_edge_attribute((u, v), 'f')
            sp, ep = self.cablenet.edge_coordinates(u, v)

            if f ** 2 < tol2:
                continue
            if f > 0.0:
                color = tension
            if f < 0.0:
                color = compression
                f = -f

            radius = scale * f

            lines.append({
                'start'  : sp,
                'end'    : ep,
                'radius' : radius,
                'color'  : color,
                'name'   : "{}.force.{}-{}".format(self.cablenet.name, u, v)
            })

        self._draw_cylinders(lines)

    def clear_reactions(self):
        """Clear all previously drawn reaction forces from the Rhino View.
        """
        guids = compas_rhino.get_objects(name="{}.reaction.*".format(self.cablenet.name))
        compas_rhino.delete_objects(guids)

    def draw_reactions(self, color=None, scale=None, tol=None):
        """Draw the reaction forces at the anchor points of the Cablenet.

        Parameters
        ----------
        color : str or tuple, optional
            Color of reaction forces.
        scale : float, optional
            Scale of reaction forces.
        tol : float, optional
            Threshold for drawing reaction forces.

        """
        self.clear_reactions()

        color = color or self.cablenet.attributes['color.reaction']
        scale = scale or self.cablenet.attributes['scale.reaction']
        tol   = tol or self.cablenet.attributes['tol.reaction']
        tol2  = tol**2

        lines = []
        for key, attr in self.cablenet.vertices(True):
            if not attr['is_anchor']:
                continue

            r = self.cablenet.get_vertex_attributes(key, ('rx', 'ry', 'rz'))

            if length_vector_sqrd(r) <= tol2:
                continue

            sp = self.cablenet.vertex_coordinates(key)
            ep = subtract_vectors(sp, scale_vector(r, scale))

            lines.append({
                'start' : sp,
                'end'   : ep,
                'name'  : "{}.reaction.{}".format(self.cablenet.name, key),
                'color' : color,
                'arrow' : 'end'
            })

        self._draw_lines(lines)

    def clear_loads(self):
        """Clear all previously drawn loads from the Rhino View.
        """
        guids = compas_rhino.get_objects(name="{}.load.*".format(self.cablenet.name))
        compas_rhino.delete_objects(guids)

    def draw_loads(self, color=None, scale=None, tol=None):
        """Draw the externally applied loads at the vertices of the cablenet.

        Parameters
        ----------
        color : str or tuple, optional
            Color of loads.
        scale : float, optional
            Scale of loads.
        tol : float, optional
            Threshold for drawing loads.

        """
        self.clear_loads()

        color = color or self.cablenet.attributes['color.load']
        scale = scale or self.cablenet.attributes['scale.load']
        tol   = tol or self.cablenet.attributes['tol.load']
        tol2  = tol**2

        lines = []
        for key, attr in self.cablenet.vertices(True):
            if attr['is_anchor']:
                continue

            p = self.cablenet.get_vertex_attributes(key, ('px', 'py', 'pz'))

            if length_vector_sqrd(p) <= tol2:
                continue

            sp = self.cablenet.vertex_coordinates(key)
            ep = add_vectors(sp, scale_vector(p, scale))

            lines.append({
                'start' : sp,
                'end'   : ep,
                'name'  : "{}.load.{}".format(self.cablenet.name, key),
                'color' : color,
                'arrow' : 'end'
            })

        self._draw_lines(lines)


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":
    pass
