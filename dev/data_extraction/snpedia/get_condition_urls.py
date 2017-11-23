import sys
import json

line1 = int(sys.argv[1])-1
line2 = int(sys.argv[2])

with open(sys.argv[3],"r") as f:
    lines = f.read().split("\n")[line1:line2]

with open("condition_urls.json","r") as f:
    conds = json.load(f)

for line in lines:
    url = line.split(" ")[-1]
    condition = url.split("/")[-1].replace("_"," ")
    conds[condition] = url

with open("condition_urls.json","w") as f:
    json.dump(conds,f)
