import numpy as np
import csv
import matplotlib.pyplot as plt

# ############################## Approach ##############################
"""
Firstly, the user enters the CSV file to load, the number of clusters (k) 
and the number of iterations to perform. Then, the data read from the CSV files 
are divided into 1-D lists of country names, x values (birth rate) and 
y values (life expectancy).

For the first iteration, a user-defined k amount of centroids are selected by
randomly choosing the index of an item in the x values list. The same y value 
at that index is also selected to get the x,y coordinates of the centroid. The 
x values are stores in one list, and the y values in a separate list.
 
The following steps have to be repeated for as many iterations as the user 
has input. The centroid's x,y values are passed to the 
'assign_clusters' function that calculates the Euclidean distance between each 
data point and the centroids. The minimum distance is computed and added to a 
list. Thus, the function returns a list of each data point's cluster 
assignment for that iteration. Next, the assignment's list is passed to the 
'make_scatter_plt' function that displays a scatter plot of the clusters and
centroids. Then, the 'find_new_centroids' function calculates the mean x, y 
values for each cluster which defines the centroids for the next iteration.

Each iteration outputs a scatter plot of data points with a '+' to denote the 
centroids, and different colours for the different clusters. After closing the 
scatter plot window, the information about the number of countries, the country 
names, the mean birth rate and life expectancy for each cluster is printed 
to the console.

Note that the random selection of centroids may not always yield reasonable 
cluster divisions, in which case the program has to be re-run.

References:
I used the following resources to help me complete this task: 
- for the order of steps:
    (https://www.youtube.com/watch?v=AFS8LUgBMS0)
    (https://stackabuse.com/k-means-clustering-with-scikit-learn/)
- for the cluster assignment logic:
    (https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-
    clustering/#h2_10)
- for displaying centroids in matplotlib:
    (https://towardsdatascience.com/create-your-own-k-means-clustering-algorithm
    -in-python-d7d4c9077670)
"""

# ############################## User Inputs ############################
# get the data set to load (and ensure user input is valid before proceeding)
load_file = ""
flag = False
while not flag:
    data_choice = input(
        """Please enter the number of the data set to use 
        1 - data1953.csv
        2 - data2008.csv
        3 - dataBoth.csv
        : """)
    if data_choice == "1":
        load_file = "data1953.csv"
        flag = True
    elif data_choice == "2":
        load_file = "data2008.csv"
        flag = True
    elif data_choice == "3":
        load_file = "dataBoth.csv"
        flag = True
    else:
        print("No such option, please try again.")

# get the number of clusters from the user and check that its between 2 - 5
k = 0
valid_k = False
while not valid_k:
    k = int(input("Enter the number of clusters (bet. 2 - 5): "))
    if k not in range(2, 6):
        print("Please enter a number between 2 - 5.")
    else:
        valid_k = True

# ask for number of iterations to perform
iterations = int(input("Enter the number of iterations to perform: "))


# ############################## Define Methods ###############################
def readCSV(file):
    """
    Reads a CSV file using Python's CSV module and returns the contents
    as a long list.
    :param file:    the name and of the csv file
    :return:        a long list of all the file's data
    """
    with open(file, 'r') as csvfile:
        data_list = list(csv.reader(csvfile, delimiter=','))
    return data_list


def euclidean(p1, p2):
    """
    Computes the Euclidean distance between two points. Takes in two
    tuples of x, y values. Called by the 'calc_distances' function.
    :param p1:  a tuple of x, y values of the 1st point
    :param p2:  a tuple of x, y values of the 2nd point
    :return:    the Euclidean distance between two points
    """
    return np.sqrt(
        # where distance = sqr(((x1-x2)**2) + ((y1-y2)**2)))
        ((p1[0] - p2[0]) ** 2) +
        ((p1[1] - p2[1]) ** 2)
    )


def calc_distances(centroid_x_list, centroid_y_list):
    """
    Calls the 'euclidean' function to calculate the distance between each
    point in the original data and each of the centroids. The original data set
    comprises two lists of x and y values, and its call is hard-coded
    into the function as x_data and y_data respectively.
    :param centroid_x_list: a list of x values for each centroid
    :param centroid_y_list: a list of y values for each centroid
    :return:                a long list of distances, k * each data point
    """
    distances_list = []
    for item in range(len(x_data)):
        for c in range(len(x_centroids)):
            distances_list.append(
                euclidean((x_data[item], y_data[item]),
                          (centroid_x_list[c], centroid_y_list[c]))
            )
    return distances_list


def assign_clusters(cent_x, cent_y, k):
    """
    Calls the 'calc_distances' function to obtain a list of all the euclidean
    distances calculating for processing. Converts the list into a np array
    where each row contains an array of distances from each centroid of a data
    point. The index of the minimum distance for each point is taken as the
    point's cluster assignment. The clusters are therefore named 0, 1, 2 etc...
    The cluster name for each point is returned in a long list
    :param cent_x:  a list of the centroids' x values
    :param cent_y:  a list of the centroids' y values
    :param k:       number of clusters as input by the user
    :return:        a list of cluster assignments corresponding to each data
    point
    """
    # for each point, calculate its distance from each centroid
    arr = np.array(calc_distances(cent_x, cent_y))
    # convert long list of distances to np array with each point's
    # distance to each centroid listed per row e.g. (196, 3)
    row_length = np.size(arr) / k
    dist_arr = arr.reshape(int(row_length), k)
    # find the smallest distance, get its index number and append to an array
    # the indices of 0, 1, 2... are the names given to the centroids
    assignment_list = np.argmin(dist_arr, axis=1)
    return assignment_list


def make_scatter_plt(centroid_x_list, centroid_y_list,
                     centroid_assignments, iteration):
    """
    Displays a scatter plot of data with colors representing clusters
    and crosses representing the centroids.
    :param centroid_x_list:       a list of the original data's x co-ords
    :param centroid_y_list:       the data's corresponding y co-ords
    :param centroid_assignments:  a list of each data point's cluster names
    :param iteration              the iteration producing the figure
    :return:                      a matplotlib figure
    """
    # color map of the centroid names (e.g 1, 2) and their assigned colors
    colm = {0: 'red', 1: 'green', 2: 'orange', 3: 'purple', 4: 'blue',
            5: 'pink'}
    # display the data and cluster assignment colors
    ele = 0
    for ele in range(len(x_data)):
        plt.scatter(x_data[ele], y_data[ele],
                    c=colm[centroid_assignments[ele]])
        ele += 1
    # display the centroids
    clust = 0
    for clust in range(k):
        plt.plot(centroid_x_list[clust], centroid_y_list[clust], '+',
                 markersize=12, c='black')
        clust += 1
    plt.title(f"Iteration {iteration}")
    plt.xlabel("Birth Rate")
    plt.ylabel("Life Expectancy")
    plt.show()


def print_cluster_info(cluster_name, country_list, mean_x, mean_y, n):
    """
    Called only by the 'find_new_centroids' method to print information about
    the new clusters. That is, the number of countries, the list of countries
    and the mean Birth Rates (x) and Life Expectancies (y) for each cluster.
    :param cluster_name:    the numeric name given to clusters, starts from 0
    :param country_list:    a list of countries assigned to a cluster
    :param mean_x:          the mean of x co-ords in a cluster
    :param mean_y:          the mean of y co-ords in a cluster
    :param n:               the number of countries/points in a cluster
    """
    print()
    # print the country represented by the data point
    print(f"Countries in cluster '{cluster_name}': ")
    print(country_list)
    # print the number of countries to the console (i.e. n)
    print(f"There are {n} countries in cluster '{cluster_name}'")
    # print the mean Birth Rate to the console (i.e. mean x value)
    print(f"The mean Birth Rate of cluster '{cluster_name}' is {mean_x:.2f}")
    # print the mean Life Expectancy to the console (i.e. mean y value)
    print(
        f"The mean Life Expectancy of cluster '{cluster_name}' is {mean_y:.2f}")


def find_new_centroids(k, assignments_list):
    """
    Finds the new centroid co-ordinates by calculating the 2-D mean of each
    cluster. Works by iterating through the list of assignments as many times
    as there are clusters. In the first iteration, the x and y values belonging
    to the first cluster are summed and the divided by the number of data points
    found for that cluster. These means are then appended to the list and the
    iteration for the second cluster begins after variables are re-initialised
    to 0. Also,  calls 'print_cluster_info' to print information about each
    cluster; the number of countries, the mean Birth Rate and Life Expectancy
    and list of the country names.
    :param k:                   the number of clusters defined by the user
    :param assignments_list:    a list of each data point's cluster assignments
    :return:                    a 2-D list of the new centroid's co-ordinates
                                where the first row are the x values and the
                                second row consists of the v values. The columns
                                are the centroids
    """
    # --- initialise variables ---
    # holds the running sum of x and v values
    sum_x = 0
    sum_y = 0
    # counts the number of values belonging to a cluster
    n = 0
    # holds the current inner loop's position (the index of assign_croids)
    idx = 0
    # holds the mean values
    mean_x = 0
    mean_y = 0
    # counts the outer loop iterations i.e represents each cluster
    cluster_name = 0
    # a list of the means for cluster which are the new centroid's co-ordinates
    new_xcentroid = []
    new_ycentroid = []
    country_list = []
    # --- iterate through data to get the mean ---
    # repeat the inner loop calculations for each cluster, k
    while cluster_name < k:
        for assignment in assignments_list:
            # look through the list of assignments and calculate the mean for all
            # those equal to the first cluster (named '0') for the first iteration),
            # then the second cluster  (named '1') for the second iteration etc...
            if assignment == cluster_name:
                sum_x += x_data[idx]
                sum_y += y_data[idx]
                n += 1
                mean_x = sum_x / n
                mean_y = sum_y / n
                country_list.append(country_data[idx])
            idx += 1
        # append values to the new list of centroid co-ordinates
        new_xcentroid.append(mean_x)
        new_ycentroid.append(mean_y)
        # display information about the cluster
        print_cluster_info(cluster_name, country_list, mean_x, mean_y, n)
        # --- reset variables for the next cluster's calculations---
        sum_x = 0
        sum_y = 0
        n = 0
        idx = 0
        mean_x = 0
        mean_y = 0
        cluster_name += 1
        country_list.clear()
    return new_xcentroid, new_ycentroid


# ############################## Main ##############################
# ######### 1st Iteration ################
# -------- prepare data --------
# read from the file
data = readCSV(load_file)
# remove the first row of column names
data.remove(data[0])
# put the country names in a list
country_data = []
for i in range(len(data)):
    country_data.append(data[i][0])
# put the numeric data into a list of x and y values
x_data = []
for i in range(len(data)):
    x_data.append(float(data[i][1]))
y_data = []
for i in range(len(data)):
    y_data.append(float(data[i][2]))

# -------- select random centroid values for range k --------
# global variables to hold centroid x and y values
x_centroids = []
y_centroids = []
# randomly select an index of the x and y data points lists for as many times as k
for i in range(k):
    # get a random index number
    rand_index = np.random.randint(0, len(x_data) - 1)
    # store the random x and y values into respective centroid lists
    x_centroids.append(x_data[rand_index])
    y_centroids.append(y_data[rand_index])

# ######### Next Iterations ################
# repeat for as many times as the user has specified
for iterate in range(iterations):
    # print which iteration is happening (+1 to start counting from 1, not 0)
    print(f"------------------- ITERATION {iterate+1} -------------------")

    # calculate distances and assign clusters
    assn = assign_clusters(x_centroids, y_centroids, k)

    # view the scatter plot
    make_scatter_plt(x_centroids, y_centroids, assn, iterate+1)

    # calculate the new centroids and update the centroids list
    new_croids = find_new_centroids(k, assn)
    x_centroids = new_croids[0]
    y_centroids = new_croids[1]
