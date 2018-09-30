import numpy
def randominit(X,num_centroids):
    randidx=numpy.random.permutation(X.shape[0])
    return X[randidx[:num_centroids],:]