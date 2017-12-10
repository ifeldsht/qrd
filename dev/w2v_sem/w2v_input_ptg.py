import json
import re
from itertools import permutations

with open("words.json","r") as f:
    words = json.load(f)
voc = words["voc"]

def clean(s):
    words = re.sub("[^a-z]"," ",s.lower()).split()
    return [w for w in words if w in voc]

def process_file(filename,max_len):
    with open(filename,"r") as f:
        data = f.read().split("\n")
    data = [clean(d) for d in data]
    return [d for d in data if len(d)>1 and len(d)<=max_len]

max_len = 10
groups = []
for i in range(1000):
    print i
    filename = "out/words." + str(i) + ".txt"
    groups += process_file(filename,10)

#print len(groups), float(sum([len(s) for s in groups]))/len(groups)

pairs = []
for g in groups:
    gid = [voc[w] for w in g]
    pairs += list(permutations(gid,2))

with open("pairs_ptg.json","w") as f:
    json.dump(pairs,f)

print len(groups), len(pairs)
