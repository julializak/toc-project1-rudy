# REQUIRED
# For each instance tried, a record should be made of
    # the instance number
    # the result
    # the time spent in the solution

# Need to:
    # find all data... files (probably should use regex to easily find them in ym folder)
    # run the brute force solver
    # somehow plot the csvs

# loop over all data files
# get # vertices from read_graph
# output the results


import csv
import glob         # how we will get data.... files
# use the functions I already made from the other .py code
from bruteforce_rudyrudyrudy import test_brute_force, read_graph


# create an output file that gets updated with data once thhis is run
results = "timing_results_rudyrudyrudy.csv"


with open(results, "w", newline="") as f: 
    writer = csv.writer(f)
    writer.writerow(["filename", "vertices", "has_cycle", "best_weight", "time(s)"])

    # run all of hte data files I have saved in folder
    # use glob and regexx!!
    # fix how we get the vertices, when testing, I was coming to issues with the 7 vertice graph
    for filename in sorted(glob.glob("data_*.csv")):
        _, vertices, _ = read_graph(filename)
        num_vertices = len(vertices)

        best_order, best_weight, elapsed = test_brute_force(filename)
        has_cycle = best_order is not None

        writer.writerow([filename, num_vertices, has_cycle, best_weight, elapsed])

    
# Do a check out for user and also to make sure it all worked correctly
print("Timing complete!")