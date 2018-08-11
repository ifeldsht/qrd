import sys
 
# create a file with one line of text inside:
f = open(sys.argv[1],"w")
f.write("Hello world!")
f.close
 
# read the file and print its content:
f = open(sys.argv[1],"r")
content = f.read()
f.close
print content
 
# append some text to the file
f = open(sys.argv[1],"a")
f.write("Hello again")
f.close
