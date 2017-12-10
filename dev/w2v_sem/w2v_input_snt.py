import sys
import re
from nltk.corpus import stopwords
import json

sw = stopwords.words("english")

def clean(s):
    words = re.sub("[^a-z]"," ",s.lower()).split()
    return [w for w in words if len(w)>1 and w not in sw]

def build_pairs(s,w,voc):
    P = []
    num = len(s)
    for i in range(num):
        iid = voc[s[i]]
        n = max(0,i-w)
        for j in range(n,i):
            jid = voc[s[j]]
            P.append((iid,jid))
        n = min(num,i+w+1)
        for j in range(i+1,n):
            jid = voc[s[j]]
            P.append((iid,jid))
    return P

with open(sys.argv[1],"r") as f:
    data = f.read().split("\n")
    data = [d.split("\t") for d in data]

sents = [clean(d[1]) for d in data if len(d)==2]
print len(sents)
words = {}
for s in sents:
    for w in s:
        if w not in words: words[w] = 0
        words[w] += 1

#print len(sents), sum([len(s) for s in sents])
#for i in range(0,50,5): print i, len([w for w in words if words[w]>i])

w10 = enumerate([w for w in words if words[w]>10])
word2id = {x[1]:x[0] for x in w10}

with open("words.json","w") as f:
    json.dump({"words":words,"voc":word2id},f)

sents = [[w for w in s if w in word2id] for s in sents]
print len(sents)
sents = [s for s in sents if len(s)>1]
print len(sents)

width = 2
pairs = []
for s in sents:
    pairs += build_pairs(s,width,word2id)

with open("pairs_snt.json","w") as f:
    json.dump(pairs,f)

print len(sents), len(pairs)
