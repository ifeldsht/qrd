from copy import copy
from random import random
from random import randint
from heapq import heappop
from heapq import heappush

goal = (1,2,3,4,5,6,7,8,0)

def position(board,n):
    for i in range(3):
        for j in range(3):
            if board[3*i+j] == n:
                return (i,j)

def moves(board):
    i,j = position(board,0)
    all_moves = []
    # up
    if i-1>=0: all_moves.append( board[(i-1)*3+j] )
    # down
    if i+1<=2: all_moves.append( board[(i+1)*3+j] )
    # left
    if j-1>=0: all_moves.append( board[i*3+j-1] )
    # right
    if j+1<=2: all_moves.append( board[i*3+j+1] )
    return all_moves

def move(board,n):
    new_board = copy(board)
    i0, j0 = position(board,0)
    i, j = position(board,n)
    # swap: a,b=b,a
    new_board[i0*3+j0],new_board[i*3+j]=new_board[i*3+j],new_board[i0*3+j0]
    return new_board

def cmp_boards(b1,b2):
    return tuple(b1)==tuple(b2)

def dist(b1,b2):
    total_dist = 0
    for i1 in range(3):
        for j1 in range(3):
            i2, j2 = position(b2,b1[i1*3+j1])
            total_dist += abs(i1-i2) + abs(j1-j2)
    return total_dist

def generate(board):
    new_board = copy(board)
    for _ in range(randint(10,20)):
        all_moves = moves(new_board)
        random_move_index = randint(0,len(all_moves)-1)
        random_move = all_moves[random_move_index]
        new_board = move(new_board,random_move)
    return new_board

def Puzzle8BFS(board):
    Q = [([],board)]
    V = []
    counter = 0
    max_size = 0
    while len(Q) > 0:
        path, cur = Q[0]
        Q = Q[1:]
        if cmp_boards(cur,goal): return (True,counter,max_size,path)
        if tuple(cur) in V: continue
        V.append(tuple(cur))
        for m in moves(cur):
            Q.append((path+[m],move(cur,m)))
        if max_size < len(Q): max_size = len(Q)
        counter += 1
    return (False,counter,max_size,[])

def Puzzle8AStar(board):
    Q = []
    heappush(Q,(dist(board,goal),[],board))
    V = []
    counter = 0
    max_size = 0
    while len(Q) > 0:
        _, path, cur = heappop(Q)
        if cmp_boards(cur,goal): return (True,counter,max_size,path)
        if tuple(cur) in V: continue
        V.append(tuple(cur))
        for m in moves(cur):
            m_board = move(cur,m)
            heappush(Q,(dist(m_board,goal),path+[m],m_board))
        if max_size < len(Q): max_size = len(Q)
        counter += 1
    return (False,counter,max_size,[])

if __name__=="__main__":
    board = generate(list(goal))
    print Puzzle8BFS(board)
    print Puzzle8AStar(board)

