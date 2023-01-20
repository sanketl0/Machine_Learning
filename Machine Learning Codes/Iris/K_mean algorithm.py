import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

#importing dataset with pandas

dataset = load_iris()

x = dataset.iloc[:,[0,1,2,3]].values

#finding the optimum number of cluster for k means classification 
from sklearn.cluster import Kmeans
wcss = []

for i in range(1,11):
    kmeans = Kmeans(n_clusters = i,int = 'k-means++',max_iter = 300,n_init = 10,random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

#plotting the result on the plotting graph alloeing us to observe the elbow
    plt.plot(range(1,11),wcss)
    plt.title('The elbow method')
    plt.xlabel('Number of cluster')
    plt.ylabel('WCSS')
    plt.show()


#applying kmeans to datasets creating the kmeans classifier
    kmeans = kMeans(n_cluster =3 ,init = 'k-means++',max_iter = 300,n_init=10,random_state = 0)
    y_kmeans = kmeans.fit_predict(x)

#visulising the cluster 
    plt.scatter(x[y_kmeans == 0, 0],x[y_kmeans == 0,1],s =100,c='red',label = 'Irirs-setosa')
    plt.scatter(x[y_kmeans == 1,0],x[y_kmeans == 1,1],s = 100,c = 'blue',label ='Iris-versicolour')
    plt.scatter(x[y_kmeans ==2,0],x[y_kmeans == 2,1],s =100,c ='green',label ="Iris-virginica")
#plotting the centroids of the cluster
    plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s =100,c = 'yellow',label = 'Centroids')

    plt.legend()
    plt.show()

