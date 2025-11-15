# import necessary modules
import csv
import sys
import time
import networkx as nx

from backtracking import tsp_backtracking

# function to read multiple graph graph_indexs from the graph CSV file
def read_graphs_from_file(filename):
    graphs = []          # list to hold all graph graph_indexs
    current = None       # holds the current graph info while reading

    # open the file and read line by line
    with open(filename, mode="r") as file: 
        reader = csv.reader(file)

        # process each line in the graph file
        for row in reader:
            tag = row[0].strip()  # first element indicates the type of line

            # comment line: c,<graph_index_number>,<optional description>
            if tag == "c":
                # if we were reading a graph already, save it before starting a new one
                if current is not None:
                    graphs.append(current)

                graph_index_number = int(row[1].strip())  # get the graph_index number

                # start a new dictionary for this graph graph_index
                current = {
                    "graph_index": graph_index_number,
                    "directed": False,
                    "G": None,
                }

            # problem line: p,<u_or_d>,<num_vertices>,<num_edges>
            elif tag == "p":
                graph_type = row[1].strip()  # "u" (undirected) or "d" (directed)

                if graph_type == "d":        # directed graph
                    G = nx.DiGraph()
                    current["directed"] = True
                else:                        # undirected graph
                    G = nx.Graph()
                    current["directed"] = False

                current["G"] = G  # assign the graph object to this graph_index

            else:
                # vertex line or edge line
                G = current["G"]

                # vertex line: v,<vertex_id>
                if tag == "v":
                    vertex_id = row[1].strip()
                    G.add_node(vertex_id)  # add the vertex to the graph

                # edge line: e,<src>,<dst>,<weight>
                elif tag == "e":
                    source_vertex = row[1].strip() # source vertex
                    dest_vertex = row[2].strip() # destination vertex
                    weight = int(row[3].strip())  # convert weight to int
                    G.add_edge(source_vertex, dest_vertex, weight=weight) # add edge with weight

    # after finishing the file, append the last graph
    if current is not None and current["G"] is not None:
        graphs.append(current)

    return graphs


# if you are reading this far and have actually read my pseudo code,
# thank you and i wish you a happy thanksgiving :)

def main():
    filename = sys.argv[1]  # get the filename from command line arguments
    graph_entries = read_graphs_from_file(filename)  # read all graph entries from the file

    print("graph_index, vertex, edge, result, best_cost, time_sec")

    # process each graph entry
    for graph_entry in graph_entries:
        graph = graph_entry["G"]              # the NetworkX graph object
        graph_index = graph_entry["graph_index"]  # the graph number from the file

        # choose a start city
        all_nodes = list(graph.nodes)
        start_city = all_nodes[0] # get the first node as start city

        # start timing the TSP solver
        start_time = time.perf_counter()
        route, cost = tsp_backtracking(graph, start_city)
        end_time = time.perf_counter()

        elapsed = end_time - start_time  # total solving time

        if route is None:
            result = "No Hamiltonian Cycle - NO"
            best_cost = "Not Applicable"
        else:
            result = "Hamiltonian Cycle Found - YES"
            best_cost = cost

        print(
            graph_index,
            graph.number_of_nodes(),
            graph.number_of_edges(),
            result,
            best_cost,
            elapsed,
            sep=", ",
        )  # if you ACTUALLY made it this far, please add a comment
           # in the grading on what your favorite pie is!


if __name__ == "__main__":
    main()