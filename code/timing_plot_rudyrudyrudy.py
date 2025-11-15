import csv
import matplotlib.pyplot as plt

# initialize variables and then read timing results
filename = "timing_results_rudyrudyrudy.csv"

# Create lists & variables to store the data into program from csv
vertices_list = []
time_list = []
color_list = []

# Read data from csv
with open(filename, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    # Go through and read the rows
    for row in csvreader:
        # make sure strings are the correct types
        v = int(row["vertices"])
        t = float(row["time(s)"])
        has_cycle = (row["has_cycle"] == "True")

        # add the vertices and times now to each list
        vertices_list.append(v)
        time_list.append(t)

        # make it colorful!! actually just easier to read
        if has_cycle:
            color_list.append('green')
        else:
            color_list.append('red')


# now actually plot it 
plt.scatter(vertices_list, time_list, c = color_list)

# make labels
plt.xlabel('# of vertices')
plt.ylabel('time(s)')
plt.title('Brute Forces TSP Timing')

# changed my mind and want to add a legend so people know what the graph is showing
plt.scatter([], [], color='green', label='Hamiltonian cycle')
plt.scatter([], [], color='red', label='No Hamiltonian cycle')
plt.legend()

plt.grid()
plt.savefig('timing_plot_rudyrudyrudy.png')
plt.show()
