def DFS(graph,node,visited,goal):
    visited.append(node)
    if node == goal: return True
    for child in graph[node]:
        if child not in visited: 
            if DFS(graph,child,visited,goal): return True
    return False

def is_inside(index,maze_width,maze_hight):
    # checking first index component
    if index[0] < 0 or index[0] >= maze_hight: return False
    # checking second index component
    if index[1] < 0 or index[1] >= maze_width: return False
    # in all other cases index is inside
    return True

def create_tree(maze):
    # height of the maze is the number of lines in the definition
    height = len(maze)
    # we are assuming all lines in the definition are of the same length
    width = len(maze[0])
    # we are creating empty dictionary ...
    tree = {}
    # ... and first populate it with path elements mapped to empty lists
    for i in range(height):
        for j in range(width):
            if maze[i][j]: tree[(i,j)] = []
    # now for all elements of the tree we populated
    # lists with indices of surrounding path elements:
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

f = open("maze.txt","r")

maze = [[x=="1" for x in line] for line in f.read().split("\n") if len(line)>0]

tree = create_tree(maze)

visited = []

print DFS(tree,(0,1),visited,(1,6))
print visited
print DFS(tree,(0,1),visited,(2,6))
