# José Antonio Solís Martínez
# 162442
# TicTacToe program that uses the Minimax algorithm 
# PlayerVsComputer. The computer is the one making moves via Minimax

from Board import *

def main():
    winner = None
    gameState = "Start"
    Error = False
    while True:
        if (gameState == "Start"):
            ticTacToe = Board()
            if winner == "Player":
                turn = "Computer"
            elif winner == "Computer":
                turn = "Player"
            else:
                turn = "Player"
            input("Press a key to start\n")
            gameState = "Play"
            continue

        elif (gameState == "Play"):
            if (turn == "Player"):
                currentSymbol = "X"
                #only allow numbers from 0 to 8
                while True:
                    try:
                        move = int(input("What is your move, player? "))
                        ticTacToe.board[move] = currentSymbol
                    except IndexError:
                        print("Please choose a number from 0 to 8")
                    else:
                        break
                ticTacToe.printBoard()
                turn = "Computer"
                gameState = ticTacToe.checkWin(currentSymbol)
                if gameState == "Win":
                    winner = "Player"
                    continue
            if (turn == "Computer"):
                #print("What is your move, player?")
                currentSymbol = "O"
                #only allow numbers from 0 to 8
                while True:
                    try:
                        move = int(input("What is your move, computer? "))
                        ticTacToe.board[move] = currentSymbol
                    except IndexError:
                        print("Please choose a number from 0 to 8")
                    else:
                        break
                ticTacToe.printBoard()
                turn = "Player"
                gameState = ticTacToe.checkWin(currentSymbol)
                if gameState == "Win":
                    winner = "Computer"
                    continue

        elif (gameState == "Win"):
            #smth
            print(f'{winner} won!')
            answer = input("Do you want to play again? y/n\n")
            if (answer == 'y' or answer == 'Y'):
                gameState = "Start"
            else:
                gameState = "End"

        elif (gameState == "End"):
            #smth
            print("Thanks for playing!")
            break
        else:
            print("You broke something lol")
            gameState == "Start"
            continue


if __name__ == "__main__":
    main()