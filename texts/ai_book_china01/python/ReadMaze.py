import sys
 
f = open(sys.argv[1],"r")
maze = [[x=="1" for x in line] for line in f.read().split("\n") if len(line)>0]
f.close()
 
print maze
