from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas_rhino.selectors import VertexSelector
from compas_rhino.selectors import EdgeSelector
from compas_rhino.modifiers import VertexModifier

# issue new release to put this in main
from compas_fofin.rhino.edgemodifier import EdgeModifier


__all__ = ['CablenetHelper']


class CablenetHelper(VertexSelector,
                     EdgeSelector,
                     VertexModifier,
                     EdgeModifier):
    """A cablenet helper groups functionality for selecting and modifying cablenet
    vertices and edges in Rhino.
    """

    __module__ = 'compas_fofin.rhino'


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":
    pass
