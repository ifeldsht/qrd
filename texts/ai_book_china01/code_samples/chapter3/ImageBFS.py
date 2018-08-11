import sys
from PIL import Image


def is_inside(index,maze_width,maze_hight):
    if index[0] < 0 or index[0] >= maze_hight: return False
    if index[1] < 0 or index[1] >= maze_width: return False
    return True

def create_tree(maze):
    height = len(maze)
    width = len(maze[0])
    tree = {}
    for i in range(height):
        for j in range(width):
            if maze[i][j]: tree[(i,j)] = []
    for e in tree:
        i,j = e[0], e[1]
        if is_inside((i-1,j),width,height):
            if maze[i-1][j]: tree[e].append((i-1,j))
        if is_inside((i+1,j),width,height):
            if maze[i+1][j]: tree[e].append((i+1,j))
        if is_inside((i,j-1),width,height):
            if maze[i][j-1]: tree[e].append((i,j-1))
        if is_inside((i,j+1),width,height):
            if maze[i][j+1]: tree[e].append((i,j+1))
    return tree

def BFS(graph,start,goal):
    Q = [([start],start)]
    V = []
    while len(Q)>0:
        path, current_node = Q[0]
        Q = Q[1:]
        if current_node == goal: return (path,V,True)
        if current_node in V: continue
        V.append(current_node)
        for neighbor in graph[current_node]:
            Q.append((path+[neighbor],neighbor))
    return ([],[],False)

img = Image.open(sys.argv[1])
imglist = list(img.getdata())
w, h = img.size

maze = []
for i in range(h):
    row = [(p<192) for p in imglist[(i*w):((i+1)*w)]]
    maze.append(row)

tree = create_tree(maze)
path, visited, found = BFS(tree,(0,0),(h-1,w-1))
if not found:
    print "no exit"
    exit()

newimglist = [(x,x,x) for x in imglist]
for v in visited:
    newimglist[v[0]*w+v[1]] = (255,0,0)
for p in path:
    newimglist[p[0]*w+p[1]] = (0,255,0)
newimg = Image.new("RGB",img.size)
newimg.putdata(newimglist)

newimg.save("img_bfs.jpg")

