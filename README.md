# K-Means-clustering-from-scratch
 An unsupervised machine learning algorithm to form a k number of clusters over a user-specified number of iterations. 

## Description

An implementation of the K-Means clustering algorithm without using Sklearn's functions. The algorithm consists of the following steps:
- Step 1: Getting the data from a CSV file into lists
- Step 2: Choosing random centroid points from the lists
- Step 3: Assign the rest of the data points to their nearest centroid
- Step 4: Visualise what’s happened in a scatter plot
- Step 5: Find new centroids for each cluster 
- Step 6: Repeat steps 3 – 5.

New centroids (Step 5) are calculated by first finding the mean of each cluster. Then the Euclidean distance of each data point from each of the new centroids is calculated. The data point is then assigned to the centroid that's closest to it. 
For an even more detailed explanation, check out my [blog post](https://gearsofdevthoughts.wordpress.com/2022/06/28/k-means-clustering-the-long-way/).

Convergence isn't monitored in this implementation. However, running a few iterations yields interesting insights about the data.

### About the data sets

Each of the three .csv files is made up of data points on the life expectancy and birth rate for each country. There is a data set from 1953, one from 2008 and one consisting of both data sets. The data set is from the excellent [Gap Minder](https://www.gapminder.org/). 

## Insights from running the algorithm

As life expectancy improves worldwide, there are only a few countries in recent times that are still near 1953 levels. These counties
have not seen huge improvements in life expectancy due to long periods of deep political and civil unrest. These countries include Afghanistan,
Ethiopia, Somalia, Burkina Faso and Zimbabwe.

## Getting Started

### Dependencies

The three .csv files in this repository are needed. They are: 
* data1953.csv
* data2008.csv
* dataBoth.csv

Import the following libraries:
* numpy
* csv
* matplotlib

### Installing

Runs on any Python IDE with the .csv files in the same folder as kmeans.py.

### Executing program

Follow the prompts and enter the following:
* Enter the number corresponding to the data set to use (1, 2 or 3)
* Enter the value of k - a number between 2 and 5 (inclusive) 
* Enter the number of iterations to perform. Ideally between 4 and 8. 

Each iteration generated a scatterplot of the current centroids and cluster assignments. When the matplotlib window is closed, the following information about each cluster is displayed to the console:
* A list of countries
* The number of countries
* The mean birth rate
* The mean life expectancy

## Images
![The start menu with the first iteration's info displayed](https://github.com/Nadia-JSch/K-Means-clustering-from-scratch/blob/master/demonstration%20screenshot.png)
![A matplotlib figure generated at each iteration](https://github.com/Nadia-JSch/K-Means-clustering-from-scratch/blob/master/Iteration%204%20Demonstration.png)

## Authors

Nadia Schmidtke [get in touch](https://nadia-jsch.github.io/nadia-schmidtke-resume/Contact.html)


## License

This project is licensed under the [GNU GENERAL PUBLIC LICENSE](https://github.com/Nadia-JSch/K-Means-clustering-from-scratch/blob/master/LICENSE).

## Acknowledgments

* [tanmay bakshi's YouTube Video](https://www.youtube.com/watch?v=AFS8LUgBMS0)
* [StackAbuse's article](https://stackabuse.com/k-means-clustering-with-scikit-learn/)
* [Analyticsvidhya's arcticle](https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/#h2_10)
* [Towardsdatascience's article](https://towardsdatascience.com/create-your-own-k-means-clustering-algorithm-in-python-d7d4c9077670)
