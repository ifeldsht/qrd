import requests
import sys
import json

with open(sys.argv[1],'r') as f:
    txt = f.read()

r = requests.post("http://localhost:5000", data=json.dumps({"text":txt}))
print r.text


