class Board:
    board = []
    def __init__(self):
        self.board = ["_", "_", "_",
                    "_", "_", "_",
                    "_", "_", "_"]
    
    def printBoard(self):
        counter = 0
        for cell in self.board:
            #First row
            print(str(cell) + "|", end="")
            counter += 1
            if (counter == 3 or counter == 6 or counter == 9):
                print("\n")

    #currentSymbol is the one that the current player is placing down
    def checkWin(self, currentSymbol):
        #Horizontal top
        if ((self.board[0] == currentSymbol) and (self.board[1] == currentSymbol) and (self.board[2] == currentSymbol)):
            return "Win"
        #Vertical left
        elif ((self.board[0] == currentSymbol) and (self.board[3] == currentSymbol) and (self.board[6] == currentSymbol)):
            return "Win"
        #Horizontal bottom
        elif ((self.board[6] == currentSymbol) and (self.board[7] == currentSymbol) and (self.board[8] == currentSymbol)):
            return "Win"
        #Vertical right
        elif ((self.board[2] == currentSymbol) and (self.board[5] == currentSymbol) and (self.board[8] == currentSymbol)):
            return "Win"
        #Diagonal bottom left to top right
        elif ((self.board[6] == currentSymbol) and (self.board[4] == currentSymbol) and (self.board[2] == currentSymbol)):
            return "Win"
        #Diagonal top left to bottom right
        elif ((self.board[0] == currentSymbol) and (self.board[4] == currentSymbol) and (self.board[8] == currentSymbol)):
            return "Win"
        else:
            return "Play"