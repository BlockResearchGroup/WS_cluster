from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import scriptcontext as sc
import compas_rhino

__commandname__ = "FoFin_settings"


def RunCommand(is_interactive):
    if "FoFin" not in sc.sticky:
        raise Exception("Initialise the plugin first!")

    settings = sc.sticky["FoFin"]

    compas_rhino.update_settings(settings)


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    RunCommand(True)
