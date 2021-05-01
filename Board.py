class Board:
    board = []
    def __init__(self):
        self.board = ["_", "_", "_",
                    "_", "_", "_",
                    "_", "_", "_"]

    #Print the current state of the board to the screen
    def printBoard(self):
        for index, cell in enumerate(self.board):
            #First row
            if index == 2 or index == 5:
                print(str(cell), end="")
                print("\n-+-+-")
            elif index == 8:
                print(str(cell), end="")
            else:
                print(str(cell) + "|", end="")
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
        #Vertical center
        elif ((self.board[1] == currentSymbol) and (self.board[4] == currentSymbol) and (self.board[7] == currentSymbol)):
            return "Win"
        #Horizontal center
        elif ((self.board[3] == currentSymbol) and (self.board[4] == currentSymbol) and (self.board[5] == currentSymbol)):
            return "Win"
        else:
            if (self.checkDraw() == "Draw"):
                return "Draw"
            else:
                return "Play"

    #Places a X or O in the location specified
    def placeSymbol(self, move, currentSymbol):
        symbol = self.board[move]
        if symbol == '_' or currentSymbol == "_":
            self.board[move] = currentSymbol
        else:
            raise ValueError()

    #Checks if there has been a draw and restarts the board
    def checkDraw(self):
        #Checks if the board is full
        if ("_" not in self.board):
            return "Draw"

    #Minimax algorithm
    def minimax(self, maximizing):
        #Exit conditions
        if (self.checkWin("X") == "Win"):
            #Player wins
            return -1
        elif (self.checkWin("O") == "Win"):
            #Computer wins
            return 1
        elif (self.checkDraw() == "Draw"):
            #Draw
            return 0

        #Maximizing operations by the computer
        if maximizing:
            #Initialize with very low value so it gets overriden
            bestScore = -1000
            #Computer maximazing actions
            #counter = 0
            for index, cell in enumerate(self.board):
                if cell == "_":
                    #Make hypotetical computer play in current empty location
                    self.placeSymbol(index, "O")
                    #Run the minimax algorithm again, now with the hypotetical play
                    score = self.minimax(False)
                    #Return the board to the original state
                    self.placeSymbol(index, "_")
                    #Increment the counter that moves the board (This has a high potential of messing up due to recursion)
                    #counter += 1
                    #Check if the newfound score is better than our best score
                    if (score > bestScore):
                        bestScore = score
            return bestScore
        #Minimizing operations by the player
        else:
            #Initialize with very low value so it gets overriden
            bestScore = 1000
            #Computer maximazing actions
            #counter = 0
            for index, cell in enumerate(self.board):
                if cell == "_":
                    #Make hypotetical player play in current empty location
                    self.placeSymbol(index, "X")
                    #Run the minimax algorithm again, now with the hypotetical play
                    score = self.minimax(True)
                    #Return the board to the original state
                    self.placeSymbol(index, "_")
                    #Increment the counter that moves the board (This has a high potential of messing up due to recursion)
                    #counter += 1
                    #Check if the newfound score is better than our best score
                    if (score < bestScore):
                        bestScore = score
            return bestScore
