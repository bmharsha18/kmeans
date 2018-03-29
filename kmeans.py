#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 08:08:36 2018

@author: harshabm
"""

import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plotsse

dataset = []
cost=[]

lines = [line.rstrip('\n') for line in open('tshirtdata.txt')]

for line in lines:
    if line == 'width\tlength':
        continue
    width = float(line[0:2])
    length = float(line[3:5])
    dataset.append((width,length))
    
print("\nNumber of students : ",len(dataset))
plotx = []
ploty = []

plt.axis([50,70,60,85])

for i in dataset:
	plotx.append(i[0])
	ploty.append(i[1])

plt.plot(plotx,ploty,'bo')
plt.title("Before clustering             (Tshirt size)")
plt.xlabel("width in cms")
plt.ylabel("length in cms")
plt.show()

xcord = sorted(dataset)
ycord = sorted(dataset,key=lambda tup: tup[1])

c1 = ycord[0]
c2 = ycord[189]
c3 = ycord[249]

def distance(x,y):
	return math.sqrt(math.pow((x[0]-y[0]),2)+math.pow((x[1]-y[1]),2))

def assigncluster(p,c1,c2,c3):
    d1 = distance(p,c1)
    d2 = distance(p,c2)
    d3 = distance(p,c3)
    if(d1<d2 and d1<d3):
        return 1
    elif(d2<d1 and d2<d3):
        return 2
    elif(d3<d1 and d3<d2):
        return 3


def centroid(points):
    x,y=0,0
    for i in points:
        x = x + i[0]
        y = y + i[1]
    cenx = x/float(len(points))
    ceny = y/float(len(points))
    return(cenx,ceny)

iterc = 1
  
def kmeans(c1,c2,c3,iterc):
    centroid1 = c1
    centroid2 = c2
    centroid3 = c3
    label = 0
    while 1:
        sse=0
        cluster1 = []
        cluster2 = []
        cluster3 = []
        iterc+=1
        
        for i in range(len(dataset)):
            label = assigncluster(dataset[i],centroid1,centroid2,centroid3)
            if label == 1:
                cluster1.append(dataset[i])
                sse+=distance(dataset[i],centroid1)**2
            elif label == 2:
                cluster2.append(dataset[i])
                sse+=distance(dataset[i],centroid2)**2
            elif label == 3:
                cluster3.append(dataset[i])
                sse+=distance(dataset[i],centroid3)**2
        
        centroid1 = centroid(cluster1)
        centroid2 = centroid(cluster2)
        centroid3 = centroid(cluster3)

        if (centroid1==c1 and centroid2==c2 and centroid3==c3):
            break
        else:
            c1 = centroid1
            c2 = centroid2
            c3 = centroid3
        sse=sse/50
        cost.append((sse,iterc))
        if (iterc==200):
            break   
            
    
    return(cluster1,cluster2,cluster3)




cluster1,cluster2,cluster3 = kmeans(c1,c2,c3,0)

print("\n\t--------------K means---------------")

cen1 = centroid(cluster1)
cen2 = centroid(cluster2)
cen3 = centroid(cluster3)

plotx = []
ploty = []

plt.axis([50,70,60,85])

for i in cluster1:
	plotx.append(i[0])
	ploty.append(i[1])
plt.plot(plotx,ploty,'bo')	

plotx = []
ploty = [] 

for i in cluster2:
	plotx.append(i[0])
	ploty.append(i[1])
plt.plot(plotx,ploty,'ro')

plotx = []
ploty = []

for i in cluster3:
	plotx.append(i[0])
	ploty.append(i[1])
plt.plot(plotx,ploty,'go')
plt.plot([cen1[0],cen2[0],cen3[0]],[cen1[1],cen2[1],cen3[1]],'ko')
plt.title("After clustering        (Tshirt size)")
plt.xlabel("width in cms")
plt.ylabel("length in cms")
plt.show()			

print("\nAverage t shirt size recommended for around 500 students through k-means clustering are: ")
print("\nWidth and length of 'S': ",round(cen1[0],2),"cms  ",round(cen1[1],2),"cms")
print("\nWidth and length of 'M': ",round(cen2[0],2),"cms  ",round(cen2[1],2),"cms")
print("\nWidth and length of 'L': ",round(cen3[0],2),"cms  ",round(cen3[1],2),"cms")


plotx=[]
ploty=[]

plotsse.axis([0,len(cost), 0, max(cost[0])])

for i in cost:
    ploty.append(i[0])
    plotx.append(i[1])
plotsse.plot(plotx, ploty, 'b')
plotsse.title("Cost function (optimum k value)")
plotsse.xlabel("Number of clusters")
plotsse.ylabel("Average within - Cluster sum of squares")
plotsse.show()    



	


