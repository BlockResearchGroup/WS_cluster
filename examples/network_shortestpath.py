import os

from compas.utilities import pairwise
from compas.datastructures import Network
from compas.topology import shortest_path
from compas.plotters import NetworkPlotter

# load a network from an OBJ file
network = Network.from_obj('../data/grid_irregular.obj')

# define start and end vertices
start = 21
end = 11

# compute the shortest path
path = shortest_path(network.adjacency, start, end)

# convert the path to edges of the network
edges = [(v, u) if not network.has_edge(u, v) else (u, v) for u, v in pairwise(path)]

# visualise
plotter = NetworkPlotter(network, figsize=(10, 7))
plotter.draw_vertices(text='key', facecolor={start: '#ff0000', end: '#ff0000'}, radius=0.15)
plotter.draw_edges(color={uv: '#ff0000' for uv in edges}, width={uv: 5.0 for uv in edges})
plotter.show()
