import numpy as np

map = np.zeros(4225)            #create the map, the zeros mean the points on the road

#print(map)
map[842:857]=1                      #define 4 points of checkpoint as 1
map[2392:2407]=1
map[3017:3032]=1
map[3667:3682]=1
print(map[848])
p = 1/4225*np.ones(4225)        #the possibility of all points
measurements = 1

pHH = 0.9
pMM = 0.95
vExact = 25
v_p = [0.05, 0.05, 0.07, 0.07, 0.1]
pExact = 0.32
pO = [0.1, 0.07, 0.07, 0.05, 0.05]
pU = [0.1, 0.07, 0.07, 0.05, 0.05]

def sense(p, measurement):      #function of detection for each point
    for i in range(np.size(p)):         #in range of the whole length
        if map[i] == measurement:       #if the point value 1
            p[i] = p[i]*pHH             #possibility is pHH
        else:
            p[i] = p[i]*(1-pMM)         #possibility is 1-pMM

    sumP = np.sum(p)                    #sum all possibility

    return p/sumP                       #to resize the possibility in total 1 and return

def move(p, U):                         #function of move

    qE = np.zeros(len(p))
    qO = np.zeros(len(p))
    qU = np.zeros(len(p))
    q = np.zeros(len(p))

    for i in range(len(p)):
        qE[i] = p[i-U%len(p)]*pExact
    for i in range(len(p)):
        for j in range(5):
            qO[i] = p[i-(int(U/((j+1)/3.6)))]*pO[j]
    for i in range(len(p)):
        for j in range(5):
            qU[i] = p[i+(int(U/((j+1)/3.6)))]*pU[j]
    for i in range(len(p)):
        q[i] = qE[i] + qO[i] + qU[i]


    return q


p = sense(p, measurements)
print(p)
p = move(p,4225)

np.savetxt('myfile.csv', p, delimiter=',')                          #save the array of possibility as .csv




