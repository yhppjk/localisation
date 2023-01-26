import numpy as np
import matplotlib as plt


map = np.zeros(4225)            #create the map, the zeros mean the points on the road
#print(map)
map[849]=1                      #define 4 points of checkpoint as 1
map[2399]=1
map[3024]=1
map[3674]=1
#print(map[848])
p = 1/4225*np.ones(4225)        #the possibility of all points

#print(p)

pHH = 0.7                       #the possibility of right detection and it exist a checkpoint(hit and hit)
pMM = 0.8                       #the possibility of no detection and it doesn't exist a checkpoint(miss and miss)

measurement = 1.0               #flag for detecting the checkpoint cause the checkpoints value 1

def sense(p, measurement):      #function of detection for each point
    for i in range(np.size(p)):         #in range of the whole longth
        if map[i] == measurement:       #if the point value 1
            p[i] = p[i]*pHH             #possibility is pHH
        else:
            p[i] = p[i]*(1-pMM)         #possibility is 1-pMM

    sumP = np.sum(p)                    #sum all possibility

    return p/sumP                       #to resize the possibility in total 1 and return


def move(p, U):                         #function of move
    qE = np.zeros(len(p))               #the array for calculating the length
    #q = np.zeros(len(p))

    for i in range(len(p)-U):           #find the point before the distance
        qE[i] = p[(i+U)]                #the start of the distance
    return qE


v = 25                                  #speed is 25
t = np.array([3,65,90,116])             #the time table given
m = v*t                                 #the distance

p = sense(p, measurement)                                           #use the function to detect each point and get a possibility
p = move(p,m[0])+move(p,m[1])+move(p,m[2]),move(p,m[3])             #use the function to find the movement and sum the possibility to get the start


np.savetxt('myfile.csv', p, delimiter=',')                          #save the array of possibility as .csv
print(np.argwhere(p ==np.max(p)))                                   #print the point with highest possibility as start
                                                                    # [[  0 774]] means it start at a normal point at 774
