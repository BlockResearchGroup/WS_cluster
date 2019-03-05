import os
import compas_fofin
from compas_fofin.datastructures import Cablenet
from compas_fofin.equilibrium import cablenet_fd_numpy
from compas.plotters import NetworkPlotter
from compas.utilities import i_to_red

FILE = os.path.join(compas_fofin.DATA, 'saddle.obj')

cablenet = Cablenet.from_obj(FILE)
cablenet.set_vertices_attribute('is_anchor', True, keys=cablenet.vertices_where({'vertex_degree': 1}))

cablenet_fd_numpy(cablenet)

z = cablenet.get_vertices_attribute('z')
zmin = min(z)
zmax = max(z)
zspn = zmax - zmin

plotter = NetworkPlotter(cablenet, figsize=(10, 7))
plotter.draw_vertices(facecolor={key: i_to_red((attr['z'] - zmin) / zspn) for key, attr in cablenet.vertices(True)})
plotter.draw_edges()
plotter.show()
