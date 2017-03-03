import json
from itertools import combinations

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

def graph(T,comment=""):
    def node(c,i):
        return {"caption":c,"id":i}
    def edge(c,s,t):
        return {"source":s,"target":t,"caption":c}
    #
    A = { "comment":comment, "nodes":[], "edges":[] }
    A["nodes"].append(node(comment,0))
    counter = 0
    connected_subjs = []
    sentences = T["sentences"]
    for s in sentences:
        counter += 1
        base = counter * 1000
        A["nodes"].append(node("S"+str(counter),base))
        A["edges"].append(edge("",0,base))
        oie = sentences[s]["oie"]
        for o in oie:
            i = base + o["subj"]["ind"][0] #TODO
            j = base + o[ "obj"]["ind"][0]
            A["nodes"].append(node(o["subj"]["txt"],i))
            A["nodes"].append(node(o[ "obj"]["txt"],j))
            A["edges"].append(edge(o[ "rel"]["txt"],i,j))
            if i not in connected_subjs:
                A["edges"].append(edge("",i,base))
                connected_subjs.append(i)
    corefs = T["corefs"]
    for refs in corefs:
        comb = list(combinations([(r[0],r[1]) for r in refs],2))
        for c in comb:
            id1 = 1000 * c[0][0] + c[0][1]
            id2 = 1000 * c[1][0] + c[1][1]
            A["edges"].append(edge("coref",id1,id2))
    return A



# for tests:
if __name__=="__main__":
    import sys
    x = read(load(sys.argv[1]))
    print json.dumps(graph(x,"QWERTY"), indent=4, sort_keys=True )
 
