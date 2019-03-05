import os
from compas_fofin.datastructures import Cablenet
from compas_fofin.rhino import CablenetArtist
from compas.rpc import Proxy

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, '..', '..', 'data')
FILE = os.path.join(DATA, 'saddle.obj')

proxy = Proxy('compas_fofin.equilibrium')

cablenet = Cablenet.from_obj(FILE)
cablenet.set_vertices_attribute('is_anchor', True, keys=cablenet.vertices_where({'vertex_degree': 1}))

result = proxy.cablenet_fd_rpc(cablenet.to_data())
cablenet.data = result

artist = CablenetArtist(cablenet, layer="FoFin::Cablenet")
artist.clear_layer()
artist.draw_vertices()
artist.draw_edges()
artist.draw_forces(scale=0.05)
artist.draw_loads()
artist.draw_reactions()
artist.redraw()
