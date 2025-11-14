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
    #[ Write a verifier that, given a possible solution, responds yes or no.
    # Couple this with a program that generates all possible solutions one at
    # a time. Stop with “yes” if a solution is found, or “no” if all possible
    # solutions have been tried.]

# Read files


# Generate all possibly permutations of vertices


# Check for each ordering
# Form a hamiltonian path/cycle? 


# If doing salesman problem, compute total weight


# Stop early if cycle is found or track best cost


# Time how long it takes on each test graph