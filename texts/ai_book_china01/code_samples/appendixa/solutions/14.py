from random import random

N = 10000
left = 0.1
right = 0.2

in_range = 0
for _ in range(N):
    x = random()
    if x >= left and x < right:
        in_range += 1
print in_range

# or

print len( [y for y in [random() for x in range(N)] if y>=left and y<right] )
