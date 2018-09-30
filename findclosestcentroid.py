import numpy
def findclosestcentroid(X, centroids):
    K = X.shape[0]#number of training examples
    num_centroids=centroids.shape[0]
    idx=[]##index of centroid assigned to each point
    for i in range(0,K):
        x=numpy.matrix(X[i])##turns each training example into a 1xn matrix
        vectordistance=centroids-x;##generate a matrix of distance from a training example to centroids
        distancenorm=[]##norm of distance
        for j in range(0,num_centroids):
            distancenorm.append(numpy.linalg.norm(vectordistance[j,:]))##generate a list of distance norms for each training example
        idx.append(numpy.argmin(distancenorm))
    return idx