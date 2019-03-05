"""
compas_fofin.equilibrium
========================

.. currentmodule:: compas_fofin.equilibrium

Classes
-------
.. autosummary::
    :toctree: generated/
    :nosignatures:

    cablenet_fd_numpy
    cablenet_fd_rpc

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from .fd import *


def cablenet_fd_rpc(data, **kwargs):
    """Convenience wrapper for ``cablenet_fd_numpy`` that can be used with ``RPC``.

    Parameters
    ----------
    data : dict
        The data dictionary representing a cablenet data structure.

    Returns
    -------
    dict
        A data dict with the same structure as the input dict.

    Notes
    -----
    For additional named parameters that can be passed to this function,
    see ``cablenet_fd_numpy``.

    Examples
    --------
    .. code-block:: python

        proxy = Proxy('compas_fofin.equilibrium')

        result = proxy.cablenet_fd_rpc(cablenet.to_data())
        cablenet.data = result

    """
    from compas_fofin.datastructures import Cablenet
    cablenet = Cablenet.from_data(data)
    cablenet_fd_numpy(cablenet)
    return cablenet.to_data()


__all__ = [name for name in dir() if not name.startswith('_')]
