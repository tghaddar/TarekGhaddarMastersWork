from mesh_processor import analytical_mesh_integration_2d,create_2d_cuts,get_cells_per_subset_2d,create_2d_cut_suite
from build_global_subset_boundaries import build_global_subset_boundaries
from sweep_solver import time_to_solution_numerical,add_edge_cost,make_edges_universal,add_conflict_weights,get_y_cuts
from sweep_solver import time_to_solution
from build_adjacency_matrix import build_graphs,build_adjacency
import matplotlib.pyplot as plt
import networkx as nx
plt.close("all")

#The machine parameters.
#Communication time per double
t_comm = 4.47e-02
#The number of bytes to communicate per subset.
#The message latency time.
m_l = 1
latency = 4110.0e-02
#Solve time per unknown.
t_u = 450.0e-02
upc = 4.0
upbc = 2.0

machine_params = (t_u,upc,upbc,t_comm,latency,m_l)

#Number of rows and columns.
numrow = 2
numcol = 2
num_angles = 1

#Global boundaries.
global_xmin = 0.0
global_xmax = 10.0
global_ymin = 0.0
global_ymax = 10.0

#The subset boundaries.
x_cuts,y_cuts = create_2d_cuts(global_xmin,global_xmax,numcol,global_ymin,global_ymax,numrow)

all_x_cuts,all_y_cuts = create_2d_cut_suite(global_xmin,global_xmax,numcol,global_ymin,global_ymax,numrow)

#The subset_boundaries.
subset_boundaries = build_global_subset_boundaries(numcol-1,numrow-1,x_cuts,y_cuts)

f = lambda x,y: x+y

#cells_per_subset, bdy_cells_per_subset = get_cells_per_subset_2d(f,subset_boundaries)
#
#ycuts = get_y_cuts(subset_boundaries,numrow,numcol)
##Building the adjacency matrix.
#adjacency_matrix = build_adjacency(subset_boundaries,numcol-1,numrow-1,ycuts)
##Building the graphs.
#graphs = build_graphs(adjacency_matrix,numrow,numcol)
#
##Weighting the graphs with the preliminary info of the cells per subset and boundary cells per subset. This will also return the time to solve each subset.
#graphs,time_to_solve = add_edge_cost(graphs,subset_boundaries,cells_per_subset,bdy_cells_per_subset,machine_params,numrow,numcol)
#graphs = make_edges_universal(graphs)
#graphs = add_conflict_weights(graphs,time_to_solve)

num_x_cuts = len(all_x_cuts)
num_y_cuts = len(all_y_cuts)
max_times = []

#x_cuts = all_x_cuts[1]
#y_cuts = all_y_cuts[1]
#x_cuts = [0.0, 0.5, 0.5, 10.0] 
#y_cuts = [[0.0, 3.3333126288645043, 0.5, 10.0], [0.0, 9.5, 0.5, 10.0], [0.0, 0.5, 0.5, 10.0]]
#subset_boundaries = build_global_subset_boundaries(numcol-1,numrow-1,x_cuts,y_cuts)
#max_times,graphs = time_to_solution(f,x_cuts,y_cuts,machine_params,numcol,numrow)

#G = graphs[0]
#plt.figure("Graph Test")
#edge_labels_1 = nx.get_edge_attributes(G,'weight')
#nx.draw(G,pos=Q0,with_labels = True)
#nx.draw_networkx_edge_labels(G,pos=Q0,edge_labels=edge_labels_1,font_size=8)


for i in range(0,num_x_cuts):
  for j in range(0,num_y_cuts): 
    print(i,j)
    x_cuts = all_x_cuts[i]
    y_cuts = all_y_cuts[j]    
    x_cut = x_cuts[1]
    y_cut_0 = y_cuts[0][1]
    y_cut_1 = y_cuts[1][1]
    max_time = time_to_solution(f,x_cuts,y_cuts,machine_params,numcol,numrow,num_angles)
    max_times.append([x_cut,y_cut_0,y_cut_1,max_time])
    print("here")



