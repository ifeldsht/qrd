# run "python 8a.py 1 2 3 4 5"

import sys

print sum([float(x) for x in sys.argv[1:]])
