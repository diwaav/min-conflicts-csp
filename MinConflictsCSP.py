import numpy as np
from numpy.core.fromnumeric import prod
def solve_csp(nodes, arcs, max_steps):
    """
    This function solves the csp using the MinConflicts Search Algorithm.

    :param nodes, a list of letters that indicates what type of node it is,
                  the index of the node in the list indicates its id
                  letters = {R, Y, G, B, V}
                
    :param arcs,  a list of tuples that contains two numbers, indicating the 
                  IDs of the nodes the arc connects. 
                
    :param max_steps, max number of steps to make before giving up

    returns a list of values for the solution to the CSP where the 
             index of the value corresponds the value for that given node.
    """
    node_values = []
    ### YOUR CODE HERE ###
    csp_variables = [] # conflicted variables' index

    # for G and B
    def summer(neighbors, side):
      # neighbors: list of the neighbor's indices 
      # side: STRING L OR R = left or right for leftmost or rightmost digit to be returned
      s = str(int(sum(neighbors)))
      if side == "B":
        # go leftmost, blue
        return int(s[0])
      # go rightmost, green
      return int(s[-1])

    # for Y and V
    def producter(neighbors, side):
      s = str(int(prod(neighbors)))
      if side == "V":
        # go leftmost, violet
        return int(s[0])
      # go rightmost, yellow
      return int(s[-1])

    # converts every neighbor node to its value in the neighbors function
    def values(neighbors):
      values = [[], [], [], [], []]
      for n, node in enumerate(neighbors):
        for v in node:
          values[n].append(node_values[v])
      return values
    
    # counts the number of constraints 
    # violated by a particular value, given the rest 
    # of the current assignmnet
    def conflicts(neighbor_values, csp_variables):
      conflicts = 0
      for i, v in enumerate(node_values):
        # loop through each thing in current state
        if (nodes[i] == "Y") and (producter(neighbor_values[i], "Y") != v):
          conflicts += 1
          csp_variables.append(i)
        if (nodes[i] == "V") and (producter(neighbor_values[i], "V") != v):
          conflicts += 1
          csp_variables.append(i)
        if (nodes[i] == "B") and (summer(neighbor_values[i], "B") != v):
          conflicts += 1
          csp_variables.append(i)
        if (nodes[i] == "G") and (summer(neighbor_values[i], "G") != v):
          conflicts += 1
          csp_variables.append(i)
      return conflicts

    # make neighbors for each node in nodes by interpretting arcs
    neighbors = [[], [], [], [], []] # one for each color
    for edge in arcs:
      a, b = edge
      (neighbors[a]).append(b)
      (neighbors[b]).append(a)

    # random initial state... choose random values
    node_values = np.random.randint(1, 10, 5)
    node_values = node_values.tolist()
    # values at each neighbor for this randomized state
    neighbor_values = values(neighbors)

    for i in range(max_steps):
      if conflicts(neighbor_values, csp_variables) == 0:
        break
      var = np.random.choice(csp_variables)
      value = conflicts(neighbor_values, csp_variables)
      v = 1
      for j in range(1, 10):
        node_values[var] = j
        neighbor_values = values(neighbors)
        if conflicts(neighbor_values, csp_variables) < value:
          value = conflicts(neighbor_values, csp_variables)
          v = j
      node_values[var] = v
      neighbor_values = values(neighbors)
      csp_variables = []
    if conflicts(neighbor_values, csp_variables) != 0:
      return []
    return node_values



# test Case 1

nodes = 'YGVRB'
arcs = [(0,1), (0,2), (1,2), (1,3), (1,4), (2,3), (2,4)]
max_steps = 1000

for _ in range(max_steps):
    sol = solve_csp(nodes, arcs, max_steps)
    if sol != []:
        break
        
all_solutions = [[1, 1, 1, 7, 2],[2, 1, 2, 4, 3],[2, 6, 7, 6, 1],[2, 8, 9, 6, 1],
                 [3, 3, 1, 5, 4],[6, 2, 8, 7, 1],[6, 7, 8, 2, 1],[6, 9, 4, 8, 1]]

if sol == []:
    print('No solution')
else:
    if sol in all_solutions:
        print('Solution found:', sol)
    else:
        print('ERROR: False solution found:', sol)


# test Case 2

nodes = 'YVBGR'
arcs = [(0,1), (0,2), (1,3), (2,4)]
max_steps = 1000

for _ in range(max_steps):
    sol = solve_csp(nodes, arcs, max_steps)
    if sol != []:
        print(nodes)
        break
        
all_solutions = [[1, 1, 1, 1, 9], [1, 3, 7, 3, 6], [1, 7, 3, 7, 2], [1, 9, 9, 9, 8]]

if sol == []:
    print('No solution')
else:
    if sol in all_solutions:
        print('Solution found:', sol)
    else:
        print('ERROR: False solution found:', sol)


# test Case 3

nodes = 'VYGBR'
arcs = [(0,1), (1,2), (2,3), (3,4)]
max_steps = 1000

for _ in range(max_steps):
    sol = solve_csp(nodes, arcs, max_steps)
    if sol != []:
        print(nodes)
        break
        
all_solutions = [[2, 2, 1, 9, 8],[3, 3, 1, 8, 7],[4, 4, 1, 7, 6],[5, 5, 1, 6, 5],[5, 5, 3, 8, 5],
                 [6, 6, 1, 5, 4],[7, 7, 1, 4, 3],[8, 8, 1, 3, 2],[8, 8, 6, 8, 2],[9, 9, 1, 2, 1]]

if sol == []:
    print('No solution')
else:
    if sol in all_solutions:
        print('Solution found:', sol)
    else:
        print('ERROR: False solution found:', sol)


# test Case 4

nodes = 'YGVBR'
arcs = [(0,1), (0,2), (1,3), (2,3), (3,4), (1,2)]
max_steps = 1000

for _ in range(max_steps):
    sol = solve_csp(nodes, arcs, max_steps)
    if sol != []:
        print(nodes)
        break
        
all_solutions = [[4, 4, 1, 9, 4],[4, 7, 2, 1, 1],[4, 7, 2, 1, 2],[4, 7, 2, 1, 3],[4, 7, 2, 1, 4],
                 [4, 7, 2, 1, 5],[4, 7, 2, 1, 6],[4, 7, 2, 1, 7],[4, 7, 2, 1, 8],[4, 7, 2, 1, 9],
                 [4, 8, 3, 1, 1],[4, 8, 3, 1, 2],[4, 8, 3, 1, 3],[4, 8, 3, 1, 4],[4, 8, 3, 1, 5],
                 [4, 8, 3, 1, 6],[4, 8, 3, 1, 7],[4, 8, 3, 1, 8],[5, 1, 5, 1, 4],[5, 1, 5, 1, 5],
                 [5, 1, 5, 1, 6],[5, 1, 5, 1, 7],[5, 1, 5, 1, 8],[5, 1, 5, 1, 9]]

if sol == []:
    print('No solution')
else:
    if sol in all_solutions:
        print('Solution found:', sol)
    else:
        print('ERROR: False solution found:', sol)
