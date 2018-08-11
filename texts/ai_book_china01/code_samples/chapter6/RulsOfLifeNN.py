from itertools import permutations
from random import shuffle
import numpy as np
from sklearn.neural_network import MLPRegressor

# creating all possible inputs
all_boards = []
for i in range(10):
    x = [0]*i + [1]*(9-i)
    all_boards += list(set(permutations(x,9)))

shuffle(all_boards)

def new_state(L):
    # number of live neighbors
    # (all elements except the central one):
    sum_nbrs = sum(L[:4]) + sum(L[5:])
    if (L[4] == 1 and sum_nbrs in [2,3]) or\
       (L[4] == 0 and sum_nbrs == 3): return 1
    return 0

new_centers = [new_state(x) for x in all_boards]

X = np.array(all_boards)
Y = np.array(new_centers)

nn = MLPRegressor(hidden_layer_sizes=(9),
                  activation='logistic', 
                  solver='lbfgs')

n = nn.fit(X,Y)

Y_predicted = nn.predict(X)
predicted_centers = [(1 if c>0.5 else 0) for c in Y_predicted.tolist()]

err = 0
for c, p in zip(new_centers,predicted_centers):
    if c != p: err += 1

print err

