from random import random, randint
from copy import deepcopy
import json
import sys

class computer:
    def __init__(self,symbol,Q={},eps=0.2):
        self.symbol = symbol
        self.Q = Q
        self.eps = eps

    def move(self,board,learning):
        moves = board.moves()
        if random() < self.eps and learning:
            return moves[randint(0,len(moves)-1)]
        state = board.state(self.Q,self.symbol)
        qs = self.Q[state]
        minmax = max
        if self.symbol == "O": minmax = min
        mm = minmax(qs.values())
        options = [int(m) for m in qs if qs[m]==mm]
        return options[randint(0,len(options)-1)]

class human:
    def __init__(self,symbol):
        self.symbol = symbol
 
    def move(self,board,learning):
        print board
        i = int(input("> "))
        if i not in board.moves():
            return self.move(board,learning)
        return i

class board:
    def __init__(self):
        self.empty = " "
        self.buffer = [self.empty]*9

    def winner(self,p):
        winning_lines = [[0,1,2],[3,4,5],[6,7,8],\
                         [0,3,6],[1,4,7],[2,5,8],\
                         [0,4,8],[2,4,6]]
        for line in winning_lines:
            if self.buffer[line[0]] == p and \
               self.buffer[line[1]] == p and \
               self.buffer[line[2]] == p:
                return True
        return False

    def filled(self):
        return len([x for x in self.buffer if x is self.empty])==0 or \
               self.winner("X") or self.winner("O")

    def on_move(self,move,player):
        self.buffer[move] = player.symbol

    def moves(self):
        return [c[0] for c in enumerate(self.buffer) if c[1] is self.empty] 
 
    def state(self,Q,symbol):
        state = "".join(self.buffer) + symbol
        if state not in Q:
            Q[state] = {m:1.0 for m in self.moves()}
        return state

    def reward(self):
        if not self.filled(): return 0.0
        if self.winner("X"):  return 1.0 
        if self.winner("O"):  return -1.0 
        return 0.5

    def __repr__(self):
        return "{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}".format(*self.buffer)

class TicTacToeGame:
    def __init__(self,player1,player2,Q={}):
        self.starting_symbol = player1.symbol
        self.player1 = player1  
        self.player2 = player2
        self.learning = isinstance(player1,computer) and\
                        isinstance(player2,computer)
        self.Q = Q
        self.board = board()
        self.gamma = 0.9
        self.alpha = 0.3
        if isinstance(self.player1,computer): self.player1.Q = Q
        if isinstance(self.player2,computer): self.player2.Q = Q

    def switch(self):
        self.player1, self.player2 = self.player2, self.player1 

    def restart(self):
        if self.starting_symbol != self.player1.symbol:
            self.switch()
        self.board = board()

    def play(self):
        while not self.board.filled():
            move = self.player1.move(self.board,self.learning)
            self.on_move(move)

    def on_move(self,move):
        if self.learning:
            self.learn(move)
        self.board.on_move(move,self.player1)
        if self.board.filled():
            self.done()
        else:
            self.switch()

    def learn(self,move):
        state = self.board.state(self.Q,self.player1.symbol)
        new_board = deepcopy(self.board)
        new_board.buffer[move] = self.player1.symbol
        reward = new_board.reward()
        if not new_board.filled():
            new_state = new_board.state(self.Q,self.player2.symbol)
            qs = self.Q[new_state]
            if self.player1.symbol == "X": 
                reward = self.gamma*min(qs.values()) 
            else:
                reward = self.gamma*max(qs.values()) 
        self.Q[state][move] += self.alpha*(reward-self.Q[state][move])
  
    def done(self):
        if self.learning: return
        print "done"
        print self.board


if __name__=="__main__":
    if len(sys.argv) == 1:
        player1 = computer("X")
        player2 = computer("O")
        game = TicTacToeGame(player1,player2)
        for i in range(1000000):
            if i%10000 == 0: print i
            game.play()
            game.restart()
        with open("rlttt.json","w") as f:
            json.dump(game.Q,f)
    else:
        with open("rlttt.json","r") as f:
            Q = json.load(f)
        player1 = computer("X") 
        player2 = human("O")
        game = TicTacToeGame(player1,player2,Q)
        game.play()

 










    def filled(self):
        return len([x for x in self.buffer if x in self.empty])==0 or \
               self.winner("O") or self.winner("X")
