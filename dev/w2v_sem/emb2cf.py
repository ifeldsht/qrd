import json
import sys

with open("words.json", "r") as f:
    words = json.load(f)
    words = words["voc"]

with open(sys.argv[1],"r") as f:
    emb = json.load(f)

size = len(emb[0])
print len(words), size

for w in words:
    print w,
    for e in emb[words[w]]: print e,
    print ""

