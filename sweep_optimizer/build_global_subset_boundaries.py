
def build_global_subset_boundaries(N_x, N_y,x_cuts,y_cuts):

  global_subset_boundary = []
  num_subsets = (N_x+1)*(N_y+1)
  
  for i in range(0,num_subsets):
    subset_boundary = []
  
    #Subset ID
    ss_id = i
  
    current_column = int(ss_id/(N_y+1))
    current_row = 0
    if (current_column == 0):
      current_row = ss_id
    else:
      current_row = int(ss_id - current_column*(N_y+1))
  
  
    #Getting x_min, x_max, y_min, y_max of current subset
    x_min = x_cuts[current_column]
    x_max = x_cuts[current_column+1]
  
    y_min = y_cuts[current_column][current_row]
    y_max = y_cuts[current_column][current_row+1]
  
    subset_boundary = [x_min, x_max, y_min, y_max]
    #print("Row: ", current_row)
    #print("Col: ", current_column)
    #print(subset_boundary)
    global_subset_boundary.append(subset_boundary)
    
  return global_subset_boundary