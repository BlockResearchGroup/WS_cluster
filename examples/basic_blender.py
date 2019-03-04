# Blender

from compas.datastructures import Mesh
from compas.datastructures import mesh_subdivide

from compas_blender.artists import MeshArtist

mesh = Mesh.from_polyhedron(6)
subd = mesh_subdivide(mesh, k=3)

artist = MeshArtist(None)

artist.mesh = mesh
artist.draw_vertices()
artist.draw_edges()

artist.mesh = subd
artist.draw_faces()
