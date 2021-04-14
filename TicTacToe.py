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

def main():
    board = ["_", "_", "_",
            "_", "_", "_",
            "_", "_", "_"]
    finished = False
    turn = "Player"

    while (not finished):
        if (turn == "Player"):
            #print("What is your move, player?")
            move = int(input("What is your move, player? "))
            board[move] = "X"
            printBoard(board)
            turn = "Computer"
        if (turn == "Computer"):
            #print("What is your move, player?")
            move = int(input("What is your move, computer? "))
            board[move] = "O"
            printBoard(board)
            turn = "Player"

if __name__ == "__main__":
    main()