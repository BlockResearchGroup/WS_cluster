from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import scriptcontext as sc

__commandname__ = "FoFin_init"


def RunCommand(is_interactive):
    sc.sticky["FoFin"] = {
        'a': 1,
        'b': 2
    }


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    RunCommand(True)
