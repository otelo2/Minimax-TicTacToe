# José Antonio Solís Martínez
# 162442
# TicTacToe program that uses the Minimax algorithm 
# PlayerVsComputer. The computer is the one making moves via Minimax

from Board import *

def main():
    ticTacToe = Board()
    finished = False
    turn = "Player"

    while (not finished):
        if (turn == "Player"):
            #print("What is your move, player?")
            currentSymbol = "X"
            move = int(input("What is your move, player? "))
            ticTacToe.board[move] = currentSymbol
            ticTacToe.printBoard()
            turn = "Computer"
            finished = ticTacToe.checkWin(currentSymbol)
            if finished:
                continue
        if (turn == "Computer"):
            #print("What is your move, player?")
            currentSymbol = "O"
            move = int(input("What is your move, computer? "))
            ticTacToe.board[move] = currentSymbol
            ticTacToe.printBoard()
            turn = "Player"
            finished = ticTacToe.checkWin(currentSymbol)
            if finished:
                continue
    
    print("Thanks for playing")

if __name__ == "__main__":
    main()