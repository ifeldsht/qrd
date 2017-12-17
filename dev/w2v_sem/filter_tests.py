import json


with open("words.json","r") as f:
    words = json.load(f)
    words = words["words"]

with open("tests/wordsim353.csv","r") as f:
    ws353 = [ x.split(",") for x in f.read().lower().split("\r\n") ]

with open("tests/google_questions_words.txt","r") as f:
    goog = [ x.split() for x in f.read().lower().split("\n")\
                        if len(x) > 1 and x[0] != ":"]

ws353f = []
googf = []

for x in ws353:
    if x[0] in words and x[1] in words:
        ws353f.append( (words[x[0]],words[x[1]],float(x[2])) )

for x in goog:
    if x[0] in words and x[1] in words and x[2] in words and x[3] in words:
        googf.append( (words[x[0]],words[x[1]],words[x[2]],words[x[3]]) )

print len(ws353), len(ws353f)
print len(goog), len(googf)

with open("tests/wordsim353.json","w") as f:
    json.dump(ws353f,f)

with open("tests/google_questions_words.json","w") as f:
    json.dump(googf,f)

