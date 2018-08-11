import sys

argv_str = ""
for s in sys.argv[1:]:
    argv_str += s
print argv_str

# or

print "".join(sys.argv[1:])

# or comma-separated

print ",".join(sys.argv[1:])

