from heapq import heappop
from heapq import heappush

def Dijkstra(graph,start,goal):
    Q = []
    heappush( Q, (0,[start],start) )
    V = []
    while len(Q)>0:
        from_start, path, current_node = heappop(Q)
        if current_node == goal: return (path,V,True)
        if current_node in V: continue
        V.append(current_node)
        for neighbor, weight in graph[current_node]:
            heappush(Q,(from_start+weight,path+[neighbor],neighbor))
    return ([],[],False)

if __name__=="__main__":
    graph = {}
    graph["A"] = [("B",3),("C",7),("D",8)]
    graph["B"] = [("A",4),("C",1),("D",11)]
    graph["C"] = [("D",2)]
    graph["D"] = [("C",3)]

    print Dijkstra(graph,"A","D")
