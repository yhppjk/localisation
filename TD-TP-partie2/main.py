import numpy as np

map = ['red', 'red', 'green', 'green', 'red', 'red', 'green', 'red']
p = np.array([1 / 8, 1 / 8, 1 / 8, 1 / 8, 1 / 8, 1 / 8, 1 / 8, 1 / 8])

green = 3
pgreen = np.zeros_like(p)

for i in range(0, 7):
    if map[i] == 'green':
        pgreen[i] = p[i] / (3 / 8)
        print(p[i])
        print(pgreen[i])

print(pgreen)
