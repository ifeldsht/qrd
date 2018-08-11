from random import randint
from copy import deepcopy

class board:
    def __init__(self):
        self.empty = " "
        self.buffer = [self.empty] * 9

    def filled(self):
        return len([x for x in self.buffer if x is self.empty])==0 \
               or self.winner("X") or self.winner("O")

    def winner(self,p):
        winning_lines = [[0,1,2],[3,4,5],[6,7,8],
                         [0,3,6],[1,4,7],[2,5,8],
                         [0,4,8],[2,4,6]]
        for line in winning_lines:
            if self.buffer[line[0]] == p and \
               self.buffer[line[1]] == p and \
               self.buffer[line[2]] == p:
                return True
        return False

    def on_move(self,move,symbol):
        self.buffer[move] = symbol

    def moves(self):
        return [c[0] for c in enumerate(self.buffer) if c[1] is self.empty]

    def reward(self):
        if self.winner("X"): return 1.0
        if self.winner("O"): return -1.0
        return 0.0

    def __repr__(self):
        return "{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}".format(*self.buffer) 

class player:
    def __init__(self,symbol):
        self.symbol = symbol

    def move(self,board):
        pass

class computer(player):
    def __init__(self):
        player.__init__(self,"X")

    def move(self,board):
        moves = board.moves()
        mm = []
        for m in moves:
            m_board = deepcopy(board)
            m_board.on_move(m,self.symbol)
            mm.append( self.minimax(m_board,False) )
        mm_index = mm.index(max(mm))
        return moves[mm_index]

    def minimax(self,board,maximizing):
        score = board.reward()
        if score != 0: return score
        if board.filled(): return 0
        if maximizing:
            best = -10000.0
            for m in board.moves():
                m_board = deepcopy(board)
                m_board.on_move(m,"X")
                best = max(best,self.minimax(m_board,not maximizing))
        else:
            best = 10000.0
            for m in board.moves():
                m_board = deepcopy(board)
                m_board.on_move(m,"O")
                best = min(best,self.minimax(m_board,not maximizing))
        return best

class human(player):
    def __init__(self):
        player.__init__(self,"O")
    
    def move(self,board):
        print board
        i = int(input(">"))  
        if i not in board.moves(): return self.board.move(board)
        return i

class TTTMinimax:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.board = board()

    def switch(self):
        self.player1, self.player2 = self.player2, self.player1

    def play(self):
        while not self.board.filled():
            move = self.player1.move(self.board)
            self.on_move(move)

    def on_move(self,move):
        self.board.on_move(move,self.player1.symbol)
        if self.board.filled():
            self.done()
        else:
            self.switch()

    def done(self):
        print "Done:"
        print self.board

if __name__=="__main__":
    p1 = computer()
    p2 = human()
    game = TTTMinimax(p1,p2)
    game.play()

