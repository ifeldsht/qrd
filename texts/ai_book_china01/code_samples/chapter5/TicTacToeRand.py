from random import randint

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

    def __repr__(self):
        return "{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}".format(*self.buffer) 

class player:
    def __init__(self,symbol):
        self.symbol = symbol

    def move(self,board):
        pass

class computer(player):
    def __init__(self,symbol):
        player.__init__(self,symbol)

    def move(self,board):
        options = board.moves()
        return options[randint(0,len(options)-1)]

class human(player):
    def __init__(self,symbol):
        player.__init__(self,symbol)
    
    def move(self,board):
        print board
        i = int(input(">"))  
        if i not in board.moves(): return self.board.move(board)
        return i

class TTTRandom:
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
    p1 = computer("X")
    p2 = human("O")
    game = TTTRandom(p1,p2)
    game.play()

