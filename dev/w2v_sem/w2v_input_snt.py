import sys
import re
from nltk.corpus import stopwords

sw = stopwords.words("english")

def clean(s):
    words = re.sub("[^a-z]"," ",s.lower()).split()
    return [w for w in words if len(w)>1 and w not in sw]

with open(sys.argv[1],"r") as f:
    data = f.read().split("\n")
    data = [d.split("\t") for d in data]

sents = [clean(d[1]) for d in data if len(d)==2]

words = {}
for s in sents:
    for w in s:
        if w not in words: words[w] = 0
        words[w] += 1

#print len(sents), sum([len(s) for s in sents])
#for i in range(0,50,5): print i, len([w for w in words if words[w]>i])

w10 = enumerate([w for w in words if words[w]>10])
word2id = {x[1]:x[0] for x in w10}

print word2id
