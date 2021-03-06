import numpy as np
from mesh_processor import get_cells_per_subset_2d_numerical,get_cells_per_subset_2d_test
from build_global_subset_boundaries import build_global_subset_boundaries
from build_adjacency_matrix import build_adjacency

nx = 1
ny = 1
x_cuts = [0.0, 0.5, 1.0]
y_cuts =  [[0.0, 0.246797, 1.0], [0.0, 0.753203, 1.0]]

bounds = build_global_subset_boundaries(nx,ny,x_cuts,y_cuts)
adjacency_matrix = build_adjacency(bounds,nx,ny,y_cuts)


points = np.genfromtxt("unbalanced_pins_centroid_data").T

cps,bzc = get_cells_per_subset_2d_test(points,bounds,adjacency_matrix,ny+1,nx+1)

