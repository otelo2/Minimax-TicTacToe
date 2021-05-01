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
            TicTacToe = Board()
            if winner == "Player":
                turn = "Computer"
            elif winner == "Computer":
                turn = "Player"
            else:
                turn = "Player"
            input(f"{bcolors.HEADER}Press enter to start\n{bcolors.ENDC}")
            print("Calculating 255168 possible states...\n")
            gameState = "Play"
            continue

        #Playing state
        elif (gameState == "Play"):
            #Assign the correct symbols to each player
            if (turn == "Player"):
                currentSymbol = "X"
            elif (turn == "Computer"):
                currentSymbol = "O"

            #This section is just for the data that the minimax algorithm needs

            #Initialize variables
            bestScore = -1000
            bestMove = 0

            #Initialize Minimax algorithm, start recursion
            for index, cell in enumerate(TicTacToe.board):
                #Make hypotetical play in empty cell
                if cell == "_":
                    TicTacToe.placeSymbol(index, "O")
                    #Start recursion to find best score
                    score = TicTacToe.minimax(False)
                    #Clean the board
                    TicTacToe.placeSymbol(index, "_")
                    #If a new best score if found, record the value and move
                    if score > bestScore:
                        bestScore = score
                        bestMove = index

            #End of minimax section

            #Here is where the move is performed, plus some error handling
            while True:
                try:
                    if turn == "Computer":
                        #Make the computer play the move that Minimax calculated
                        move = bestMove
                    else:
                        #Ask player for its move
                        move = int(input(f"You are the {currentSymbol}\nWhat is your {bcolors.BOLD}move{bcolors.ENDC}, {bcolors.OKGREEN}{turn}{bcolors.ENDC}? "))-1
                    #Play the move that has been given
                    TicTacToe.placeSymbol(move, currentSymbol)
                except IndexError:
                    #only allow numbers from 1 to 9
                    print(f"{bcolors.FAIL}Please choose a number from 0 to 8. {bcolors.ENDC}\n")
                except ValueError:
                    #Prevent placing a symbol where there is already another one
                    print(f"{bcolors.FAIL}This move has already been done! Choose another space. {bcolors.ENDC}\n")
                else:
                    break

            #Print the board  to the console
            TicTacToe.printBoard()

            #Check if there has been a winner
            gameState = TicTacToe.checkWin(currentSymbol)
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