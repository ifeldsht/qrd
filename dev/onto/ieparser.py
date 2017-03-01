import json
import itertools

def load(file_name):
    with open(file_name,"r") as f:
        d = json.load(f)
    return d

def read(data):
    def token(t):
        return { t["index"]:(t["originalText"],t["lemma"]) }
    def openie(d):
        return { "subj":{"txt":d["subject"],\
                         "ind":[dd+1 for dd in d["subjectSpan"]]},\
                 "obj" :{"txt":d["object"],\
                         "ind":[dd+1 for dd in d["objectSpan"]]},\
                 "rel" :{"txt":d["relation"],\
                         "ind":[dd+1 for dd in d["relationSpan"]]} }
    def sentence(s):
        return {"tok":[token(t)  for t in s["tokens"]],\
                "oie":[openie(d) for d in s["openie"]] }
    def coref(r):
        return (r["sentNum"],r["startIndex"],r["endIndex"])
    S = {(s["index"]+1):sentence(s) for s in data["sentences"]}
    R = [[coref(rr) for rr in data["corefs"][r]] for r in data["corefs"]]
    return {"sentences":S,"corefs":R}

# for tests:
if __name__=="__main__":
    import sys
    x = read(load(sys.argv[1]))
    print json.dumps(x, indent=4, sort_keys=True )
 
