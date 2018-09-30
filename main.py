import numpy
import json
import requests
from runkmeans import runkmeans
from matplotlib import pyplot
from findclosestcentroid import findclosestcentroid
from computecentroids import computecentroids
from randominit import randominit
##crimestring = requests.get('http://opendata.mybluemix.net/crimes?lat=41.8986&lon=-87.6628&radius=500').text
d=json.load(open("data.txt","r"))
##d=json.loads(crimestring)
##print("formatted object below")
##print(json.dumps(d,indent=4))
num_rows=d.get("num_rows")
##print(num_rows)
crimelist=d.get('features')##a list of crime dictionary objects
##print(json.dumps(crimelist[1],indent=4))
geolocationlist=[]
desclist=[]
for i in range(0,num_rows-1):
    geolocationlist.append(crimelist[i].get("geometry").get("coordinates"))
    desclist.append(crimelist[i].get("properties").get("desc"))
geolocationlist=numpy.transpose(geolocationlist)
##print(geolocationlist[0])


geolocationlist=numpy.matrix(geolocationlist).T

idx,centroids,count=runkmeans(geolocationlist,10,25)
print(centroids.T[0])
print(centroids.T[1])
print(idx)
print('centroid shape={}x{}'.format(centroids.shape[0],centroids.shape[1]))
print('geolocationlist shape={}x{}'.format(geolocationlist.shape[0],geolocationlist.shape[1]))
for i in range(0,geolocationlist.shape[0]):
    pyplot.plot(geolocationlist[i,0],geolocationlist[i,1],color=(1-1.0/centroids.shape[0]*idx[i],1.0/centroids.shape[0]*idx[i],0.5),marker='o')
for i in range(0,centroids.shape[0]):
    pyplot.plot(numpy.array(centroids[i,0]),numpy.array(centroids[i,1]),color=(1-1.0/centroids.shape[0]*idx[i],1.0/centroids.shape[0]*i,0.5),marker='o', markersize=count[i]/30)
pyplot.show()