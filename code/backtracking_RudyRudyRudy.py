import networkx as nx

# if there is an edge return true
def edge_exists(graph, u, v):
    return graph.has_edge(u, v)

# return the weight of the edge, if edge does not exist return none
def edge_weight(graph, city1, city2):
    # if there is no edge between the two cities, return None
    if not graph.has_edge(city1, city2):
        return None

    # get the edge data
    edge_data = graph[city1][city2]

    # return the weight if it exists
    if "weight" in edge_data:
        return edge_data["weight"]
    else:
        # if no weight is specified, assume weight of 1
        return 1


# depth-first search with backtracking for TSP
def dfs_tsp(graph, start_city, current_route, visited_cities, current_cost, result_box):
    # total number of cities in the graph
    total_cities = graph.number_of_nodes()

    # base case for our recursion if we've visited all cities, check if we can return to start
    if len(current_route) == total_cities:
        last_city = current_route[-1] #  check if there's an edge back to the start city
        closing_cost = edge_weight(graph, last_city, start_city) # get the cost to return to start city

        # If no edge exists to return to start city, we can't complete the cycle
        if closing_cost is None:
            return

        #the total cost of this complete route
        total_cost = current_cost + closing_cost

        # if this complete route is better than the best we've found, update result_box
        if total_cost < result_box["cost"]:
            result_box["cost"] = total_cost
            result_box["route"] = current_route + [start_city] # complete the cycle by returning to start city
        return  

    # get rid of paths that are already more expensive than the best found
    if current_cost >= result_box["cost"]:
        return

    # explore neighbors/cities
    last_city = current_route[-1] # minus one to get the last city in the current route
    for next_city in graph.neighbors(last_city): # iterate through neighboring cities

        # skip cities we've already visited
        if next_city in visited_cities:
            continue

        # get the cost to travel to next_city
        travel_cost = edge_weight(graph, last_city, next_city)

        # if no edge exists to next_city skip it
        if travel_cost is None:
            continue

        # calculate new cost
        new_cost = current_cost + travel_cost

        # prune paths that are already more expensive than the best found
        if new_cost >= result_box["cost"]:
            continue

        # move to next vertex/city
        visited_cities.add(next_city)
        current_route.append(next_city)

        # resursively visit next city
        dfs_tsp(graph, start_city, current_route, visited_cities, new_cost, result_box)

        # back track 
        current_route.pop()
        visited_cities.remove(next_city)


# backtracking TSP solver
#  function to find the cheapest route on a weighted graph for Hamiltonian cycle, starts and ends at the same vertex by visiting all the vertices exactly once.
# if no Hamiltonian cycle exists, returns nothing
def tsp_backtracking(graph, start_city):
    # check if start_city is already in the graph
    if start_city not in graph:
        return None, None

    # box to store the best route and its cost found so far
    result_box = {
        "route": None, # to store the best route found
        "cost": float("inf")   # start with "infinity" as the worst possible cost
    }

    # initialize the current route with the start city
    current_route = [start_city]

    # visited cities
    visited_cities = {start_city}

    # start the DFS backtracking process
    dfs_tsp(graph, start_city, current_route, visited_cities, 0, result_box)

    # return the best route and its cost found
    if result_box["route"] is None:
        return None, None
    else:
        return result_box["route"], result_box["cost"]


