from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas.datastructures import Network


__all__ = ['Cablenet']


class Cablenet(Network):
    """"""

    __module__ = 'compas_fofin.datastructures'

    def __init__(self):
        super(Cablenet, self).__init__()
        self.update_default_vertex_attributes({
            'px' : 0.0,
            'py' : 0.0,
            'pz' : 0.0,
            'rx' : 0.0,
            'ry' : 0.0,
            'rz' : 0.0,

            'is_fixed'  : False,
            'is_anchor' : False,
        })
        self.update_default_edge_attributes({
            'q' : 1.0,
            'f' : 0.0,
            'l' : 0.0,
        })
        self.attributes.update({
            'layer' : 'Fofin::Cablenet',

            'color.vertex'        : (0, 0, 0),
            'color.vertex:anchor' : (255, 0, 0),
            'color.edge'          : (0, 0, 0),

            'color.force:compression' : (0, 0, 255),
            'color.force:tension'     : (255, 0, 0),
            'color.reaction'          : (0, 255, 0),
            'color.load'              : (0, 255, 0),

            'scale.force'    : 1.0,
            'scale.reaction' : 1.0,
            'scale.load'     : 1.0,

            'tol.force'    : 1e-3,
            'tol.reaction' : 1e-3,
            'tol.load'     : 1e-3,
        })

    @property
    def layer(self):
        return self.attributes['layer']

    @layer.setter
    def layer(self, layer):
        self.attributes['layer'] = layer


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":
    pass
