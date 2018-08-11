# run "python 8a.py 1 2 3 4 5"

import sys

argv_sum = 0
for s in sys.argv[1:]:
    argv_sum += float(s)

print argv_sum
