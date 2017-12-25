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

def DFS(graph,node,visited,goal):
    visited.append(node)
    if node == goal: return True
    for child in graph[node]:
        if child not in visited:
            if DFS(graph,child,visited,goal): return True
    return False


img = Image.open(sys.argv[1])
imglist = list(img.getdata())
w, h = img.size

maze = []
for i in range(h):
    row = [(p<192) for p in imglist[(i*w):((i+1)*w)]]
    maze.append(row)

sys.setrecursionlimit(100000)

tree = create_tree(maze)
visited = []
if not DFS(tree,(0,0),visited,(h-1,w-1)):
    print "no exit"
    exit()


newimglist = [(x,x,x) for x in imglist]
for v in visited:
    newimglist[v[0]*w+v[1]] = (255,0,0)
newimg = Image.new("RGB",img.size)
newimg.putdata(newimglist)

newimg.save("img_dfs.jpg")

