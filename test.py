from findclosestcentroid import findclosestcentroid
import numpy
from computecentroids import computecentroids
from randominit import randominit
from runkmeans import runkmeans
X=numpy.matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])
##centroids=numpy.matrix([[4,5,6,7],[9,10,11,12]])
##idx=findclosestcentroid(X,centroids)
##newcentroids=computecentroids(X,idx,centroids.shape[0])
##print(newcentroids)

idx,centroids=runkmeans(X,10,2)
print(centroids)
if __name__ == '__main__':
    print