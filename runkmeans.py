import numpy
from findclosestcentroid import findclosestcentroid
from computecentroids import computecentroids
from randominit import randominit
def runkmeans(X, max_iters,num_centroids):
    centroids = randominit(X, num_centroids)
    for i in range(0,max_iters):
        print('K-Means iteration {} out of {}'.format (i, max_iters))
        idx = findclosestcentroid(X, centroids)
        centroids,count = computecentroids(X, idx, num_centroids)
    return idx,centroids,count
