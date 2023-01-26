import numpy as np

pHit = 0.7

pMiss = 0.2



p = 1/4225*np.ones(4225)



def bayes(p):

    for i in range(4225):

        if i == 849 or i == 849+1550 or i == 849+1550+625 or i == 849+1550+625+650:

            p[i] =  0.7 * p[i]

        else:

            p[i] =  0.2 * p[i]



    return 0.7*p / sum(p)





def move(p,u):

    q = np.zeros(len(p))

    for i in range(len(p)):

        q[i] = p[(i+u)%len(p)]

    return q


v = 25

t = np.array([3, 65, 90, 116])

m = v*t



p = bayes(p)

p = move(p,m[0])+move(p,m[1])+move(p,m[2])+move(p,m[3])

print(np.argwhere(p ==np.max(p)))

