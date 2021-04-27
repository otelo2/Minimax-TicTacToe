# José Antonio Solís Martínez
# 162442
# TicTacToe program that uses the Minimax algorithm 
# PlayerVsComputer. The computer is the one making moves via Minimax

from Board import *
from Colors import *

def main():
    winner = None
    gameState = "Start"
    while True:
        #Starting state
        if (gameState == "Start"):
            ticTacToe = Board()
            if winner == "Player":
                turn = "Computer"
            elif winner == "Computer":
                turn = "Player"
            else:
                turn = "Player"
            input(f"{bcolors.HEADER}Press enter to start\n{bcolors.ENDC}")
            gameState = "Play"
            continue

        #Playing state
        elif (gameState == "Play"):
            #Assign the correct symbols to each player
            if (turn == "Player"):
                currentSymbol = "X"
            elif (turn == "Computer"):
                currentSymbol = "O"

            #Here is where the move is performed, plus some error handling
            while True:
                try:
                    move = int(input(f"\n\nWhat is your {bcolors.BOLD}move{bcolors.ENDC}, {bcolors.OKGREEN}{turn}{bcolors.ENDC}? "))-1
                    ticTacToe.placeSymbol(move, currentSymbol)
                except IndexError:
                    #only allow numbers from 1 to 9
                    print(f"{bcolors.FAIL}Please choose a number from 0 to 8. {bcolors.ENDC}\n")
                except ValueError:
                    #Prevent placing a symbol where there is already another one
                    print(f"{bcolors.FAIL}This move has already been done! Choose another space. {bcolors.ENDC}\n")
                else:
                    break

            #Print the board  to the console
            ticTacToe.printBoard()

            #Check if there has been a winner
            gameState = ticTacToe.checkWin(currentSymbol)
            if gameState == "Win":
                winner = turn
                continue
            elif gameState == "Draw":
                winner = "No one"
                continue
            else:
                #If there is no winner yet,start the next turn
                if turn == "Computer":
                    turn = "Player"
                elif turn == "Player":
                    turn = "Computer"

        #Win state
        elif (gameState == "Win"):
            #smth
            print(f'\n\n{bcolors.OKCYAN}{winner} won!{bcolors.ENDC}')
            answer = input(f"Do you want to play again? {bcolors.OKBLUE}y/n{bcolors.ENDC}\n")
            if (answer == 'y' or answer == 'Y'):
                gameState = "Start"
            else:
                gameState = "End"
        
        #Draw state
        elif (gameState == "Draw"):
            #smth
            print(f'{winner} won! It\'s a draw!')
            answer = input(f"Do you want to play again? {bcolors.OKBLUE}y/n{bcolors.ENDC}\n")
            if (answer == 'y' or answer == 'Y'):
                gameState = "Start"
            else:
                gameState = "End"

        #end state
        elif (gameState == "End"):
            #smth
            print(f"{bcolors.WARNING}Thanks for playing!{bcolors.ENDC}")
            break
        else:
            print("You broke something lol")
            gameState == "Start"
            continue


if __name__ == "__main__":
    main()