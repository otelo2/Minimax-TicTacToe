# José Antonio Solís Martínez
# 162442
# TicTacToe program that uses the Minimax algorithm 
# PlayerVsComputer. The computer is the one making moves via Minimax

def printBoard(board):
    counter = 0
    for cell in board:
        #First row
        print(str(cell) + "|", end="")
        counter += 1
        if (counter == 3 or counter == 6 or counter == 9):
            print("\n")

#currentSymbol is the one that the current player is placing down
def checkWin(board, currentSymbol):
    #Horizontal top
    if ((board[0] == currentSymbol) and (board[1] == currentSymbol) and (board[2] == currentSymbol)):
        print("Someone won!")
        return True
    #Vertical left
    elif ((board[0] == currentSymbol) and (board[3] == currentSymbol) and (board[6] == currentSymbol)):
        print("Someone won!")
        return True
    #Horizontal bottom
    elif ((board[6] == currentSymbol) and (board[7] == currentSymbol) and (board[8] == currentSymbol)):
        print("Someone won!")
        return True
    #Vertical right
    elif ((board[2] == currentSymbol) and (board[5] == currentSymbol) and (board[8] == currentSymbol)):
        print("Someone won!")
        return True
    #Diagonal bottom left to top right
    elif ((board[6] == currentSymbol) and (board[4] == currentSymbol) and (board[2] == currentSymbol)):
        print("Someone won!")
        return True
    #Diagonal top left to bottom right
    elif ((board[0] == currentSymbol) and (board[4] == currentSymbol) and (board[8] == currentSymbol)):
        print("Someone won!")
        return True
    else:
        return False

def main():
    board = ["_", "_", "_",
            "_", "_", "_",
            "_", "_", "_"]
    finished = False
    turn = "Player"

    while (not finished):
        if (turn == "Player"):
            #print("What is your move, player?")
            currentSymbol = "X"
            move = int(input("What is your move, player? "))
            board[move] = currentSymbol
            printBoard(board)
            turn = "Computer"
            finished = checkWin(board, currentSymbol)
            if finished:
                continue
        if (turn == "Computer"):
            #print("What is your move, player?")
            currentSymbol = "O"
            move = int(input("What is your move, computer? "))
            board[move] = currentSymbol
            printBoard(board)
            turn = "Player"
            finished = checkWin(board, currentSymbol)
            if finished:
                continue
    
    print("Thanks for playing")

if __name__ == "__main__":
    main()