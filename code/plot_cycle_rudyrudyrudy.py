# Wanted to try to plot the actual hamiltonian path
# Used same sources geeksforgeeks and matplotlib library

import math
import matplotlib.pyplot as plt
from bruteforce_rudyrudyrudy import read_graph, brute_force_traveling


# create fucntion to plot
def plot_cycle(filename):
    # read the graph
    # solve for the traveling salesman
    directed, vertices, adj = read_graph(filename)
    best_order, bestweight = brute_force_traveling(vertices, adj)

    # get num of vertices
    n = len(vertices)

    # position the vertices in a circle?? this could be the wrong way to do it
    positions = {}

    # going wayyy back into sophomore year for the cos/sin functions
    # defintely had to reference geeks for geeks as a refresh
    for i, v in enumerate(vertices):
        angle = 2 * math.pi * i/n
        positions[v] = (math.cos(angle), math.sin(angle))
    
    # make plot
    plt.figure()

    # draw edges
    for u in adj:
        for v in adj[u]:
            x1, y1 = positions[u]
            x2, y2 = positions[v]
            plt.plot([x1, x2], [y1, y2], color = "black")

    # now draw the actual hamiltonian cycle (only if it exists)
    if best_order is not None: 
        for i in range(len(best_order) - 1):
            u = best_order[i]
            v = best_order[i + 1]
            x1, y1 = positions[u]
            x2, y2 = positions[v]
            plt.plot([x1, x2], [y1, y2], color = "blue")

    # now draw the vertices
    # make them points and label them
    for v in vertices:
        x, y = positions[v]
        plt.scatter(x, y, color = "pink")
        plt.text(x, y, str(v))

    # formatting
    plt.title(f"Hamiltonian cycle for {filename}")
    plt.show()

# do same thing as main program so we can have temrinal input for filenames
if __name__ == "__main__":
    filename = input("Enter filename: ").strip()
    plot_cycle(filename)