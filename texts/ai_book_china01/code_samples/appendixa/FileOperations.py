# create a file with one line of text inside:
f = open("filename.txt","w")
f.write("Hello world!")
f.close
 
# read the file and print its content:
f = open("filename.txt","r")
content = f.read()
f.close
print content
 
# append some text to the file
f = open("filename.txt","a")
f.write("Hello again")
f.close
