import numpy as np
map = ['red', 'red', 'green', 'green', 'red', 'red', 'green', 'red']
p = np.array([1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8])

pHit = 0.6
pMiss = 0.2

pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1
measurements = ['green','green']

def sense(p, measurement):
    for i in range(np.size(p)):
        if map[i] == measurement:
            p[i] = p[i]*pHit
        else:
            p[i] = p[i]*pMiss

    sumP = np.sum(p)
    for i in range(np.size(p)):
        p[i] = p[i]/sumP
    return p

def move(p,U):
    qE = np.zeros(len(p))
    qO = np.zeros(len(p))
    qU = np.zeros(len(p))
    q = np.zeros(len(p))

    for i in range(len(p)):
        qE[i] = p[i-U%len(p)]*pExact
    for i in range(len(p)):
        qO[i] = p[i-(U+1)%len(p)]*pOvershoot
    for i in range(len(p)):
        qU[i] = p[i-(U-1)%len(p)]*pUndershoot
    for i in range(len(p)):
        q[i] = qE[i] + qO[i] +qU[i]

    return q

p = sense(p,'green')
print(p)
p = move(p,2)
print(p)
p = sense(p,'green')
print(p)



# map = ['red', 'red', 'green', 'green', 'red', 'red', 'green', 'red']
# p = np.array([1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8])
#
# pHit = 0.6
# pMiss = 0.2
#
# pExcat = 0.8
# pOvershoot = 0.1
# pUndershoot = 0.1
# measurements = ['green','green']
#
# def sense(p, measurement):
#     for i in range(np.size(p)):
#         if map[i] == measurement:
#             p[i] = p[i]*pHit
#         else:
#             p[i] = p[i]*pMiss
#
#     sumP = np.sum(p)
#     for i in range(np.size(p)):
#         p[i] = p[i]/sumP
#     return p
#
# def move(p,U):
#     q = np.zeros(len(p))
#     for i in range(len(p)):
#         q[i] = p[i-U%len(p)]*pExcat
#     return q
# p = sense(p,'green')
# print(p)
# p = move(p,1)
# print(p)
# p = sense(p,'green')
# print(p)


# map = ['red', 'red', 'green', 'green', 'red', 'red', 'green', 'red']
# p = np.array([1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8])
#
# green = 3
# pgreen = np.zeros_like(p)
#
# for i in range(0, 7):
#     if map[i] == 'green':
#         pgreen[i] = p[i] / (3/8)
#         print(p[i])
#         print(pgreen[i])
#
# print(pgreen)



# import numpy as np
#
# env = np.zeros([1, 8], dtype=float)
# p = np.zeros([1, 8], dtype=float)
#
#
#
# print(env)
# print(p)





