### Project 1
# Hamiltonian Path/Cycle + Traveling Saleman

    # Brute Force
    #   - try every possible asssignment

    # Backtracking
    #   - cut down the options that cannot work

###  We want to:
#   - Run these programs on different test graphs
#   - Measure how long they take
#   - Prove that these problems are very complex (use timing)

### Topic
# Given:
#   - a graph (vertices, edges, maybe weights)

# Hamiltonian
#   - visits every vertex exactly once
#   - PATH: start and end at different vertex
#   - CYCLE: start and end are the same

#    - If a Hamiltonial path doesn’t exist --> what is the largest number of vertices for which a Hamiltonian cycle exists?


### Traveling Salesman
#   - each edge has a weight (distance/cost)
# -  we want the minimum sum of edge weights



### BRUTE FORCE
    # [Write a verifier that, given a possible solution, responds yes or no.
    # Couple this with a program that generates all possible solutions one at
    # a time. Stop with “yes” if a solution is found, or “no” if all possible
    # solutions have been tried.]


import csv
import itertools # helps with efficient looping
import math
import time


# ------------------- Graph reading --------------------
# Read files
# Graph file format
    # c, .... comment line
    # p, u/d, #V, #E for undirected/directed
    # v, <id>   vertices
    # e, <u>, <v>, <weight>
    # vertices = list of vertex ids
    # adj = adjacency dict      <- ex: adj[u][v] = weight

def read_graph(filename):
    # read one graph from csv file
    # return directed, vertices, adj
    with open(filename, newline='') as f:
        rows = list(csv.reader(f))

    directed = False        # store if graph is directed or undirected
    vertices = []           # vertex IDs
    adj = {}                # adjacency list --> adj[u][v] is the weight

    for row in rows:
        # get rid of empty cells - check if row is empty or not
        cleaned_row = []
        for i in row:
            if i != "":
                cleaned_row.append(i)
        
        row = cleaned_row

        # skip row if blank
        if not row:
            continue
        front = row[0]      # get first element of row

        # p, u/d, #V, #E
        if front == 'p':
            direction_type = row[1]
            directed = (direction_type == 'd')
        # vertex line
        elif front == 'v':
            vertice_id = row[1]
            vertices.append(vertice_id)

            # make sure vertex is in adj dict
            if vertice_id not in adj:
                adj[vertice_id] = {}

        # edge line for weight for salesman
        elif front == 'e':
            u, v = row[1], row[2]

            # add weight column for later use of Traveling salesman
            # read it if it is there, but if it is not, then it is 1.0
            if len(row) > 3:
                w = float(row[3])
            else:
                w = 1.0

            # endpoints, make sure they're in adj dict
            if u not in adj:
                adj[u] = {}
            if v not in adj:
                adj[v] = {}
            
            # add the edge u --> v
            adj[u][v] = w

            # undirected -> add reverse edge
            if not directed:
                adj[v][u] = w

    return directed, vertices, adj




# ------------------- Build verifier for Hamiltonian --------------------
# Look at Project 1 doc!!
# Brute force = generate candidate assignment + verifier
# Trust it but still verify it

# Candidate = order of vertices
# Verifier (check if...) 
    # consecutive pairs are connected by an edge
    # if cycle, then check the last one with the first 
    # if valid, return the weight


def verify_path(order, adj, cycle = False):
    # Check if it is a valid hamiltonian path/cycle (described by adj)
    # So bascially check the order

    # initialize weight
    total_weight = 0.0

    # check the edges in the path
    # order = list of vertices in the order we will visit them
            # represents ONE possible hamiltonian path/cycle we are testing
    for i in range(len(order) - 1):
        u, v = order[i], order[i + 1]

        # do a check if there are NOT undirected + vertice
        # if the edge is not in the graph, we fail
        if u not in adj or v not in adj[u]:
            return False, None
        
        # now add that undirected weight
        total_weight += adj[u][v]

    # check the last -> first vertice in order to close the cycle
    u, v = order[-1], order[0]

    # check if it is valid and there
    if u not in adj or v not in adj[u]:
        return False, None
        
    # update weight
    total_weight += adj[u][v]

    return True, total_weight




# ------------------- Permutations! --------------------
# Now we solve for a brute force for the Salesman
    # Initialize the starting vertice
    # Try all the different possible paths for vertices
    # Check for a hamiltonian cycle
    # Make sure to include the weight so we can check which has the lowest
    # Want to return the best options (for weight and order)

def brute_force_traveling(vertices, adj):

    # Make sure there are vertices to look at
    if not vertices:
        return None, None

    start = vertices[0]
    next = vertices[1:]

    best_order = None

    # use math library! 
    # start with highest number so we can find the smallest one
    best_weight = math.inf 

    # now cycle through
    for i in itertools.permutations(next):
        order = [start] + list(i)

        # if the cycle works
        is_valid, weight = verify_path(order, adj)

        if is_valid and weight < best_weight:
            best_order = order
            best_weight = weight

    # return the best path/cycle 
    # return None if there is no cycle (just another good checkpoint to have)
    if best_order is None:
        return None, None
    
    ## Maybe display the cycle so we can import it into project????
    best_order = best_order + [best_order[0]]

    # return the order and weight!
    return best_order, best_weight





# ------------------- Testing! --------------------
# Start testing with test files

def test_brute_force(filename):

    # read graph
    directed, vertices, adj = read_graph(filename)

    # time the solver



    return True