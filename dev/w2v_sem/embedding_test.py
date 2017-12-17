import json
import sys


with open(sys.argv[1],"r") as f:
    emb = json.load(f)

with open("tests/google_questions_words.json", "r") as f:
    goog = json.load(f)

with open("tests/wordsim353.json","r") as f:
    ws = json.load(f)

def dist(x,y):
    return 1.0 - sum([x[0]*z[1] for z in zip(x,y)])

def expected(v0,v1,v2):
    return [ (-x[0]+x[1]+x[2]) for x in zip(v0,v1,v2) ]


# first test
total_dist = 0
total_index = 0
num = len(goog)
counter = 0
for g in goog:
    print counter
    counter += 1
    v = [emb[x] for x in g]
    exp = expected(v[0],v[1],v[2])
    total_dist += dist(exp,v[3])
    distances = list(enumerate([dist(exp,x) for x in emb]))
    distances.sort(key=lambda x: x[1])
    dist_ids = [x[0] for x in distances]
    index = dist_ids.index(g[3])
    total_index += index
    total_dist += distances[index][1]

print total_dist/num, total_index/num
    
