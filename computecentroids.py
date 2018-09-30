import numpy
def computecentroids(X,idx,num_centroids):
    count=numpy.zeros(num_centroids)##counts of points assigned to the centroid
    centroids=numpy.matrix(numpy.zeros([num_centroids,X.shape[1]]))
    centroids.flatten()
    for i in range (0,X.shape[0]):
        count[idx[i]] = count[idx[i]]+1##increase 1 count for that centroid
        centroids[idx[i],:] = centroids[idx[i],:]+X[i,:]##add the point to the centroid;
    for i in range (0,num_centroids):
        if count[i]==0:
            centroids[i]=centroids[i+1]
        centroids[i]=centroids[i]/count[i]
    return centroids,count