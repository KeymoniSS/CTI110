# This program lets the user play the game Rock, Paper, Scissors against the computer.
# October 1, 2018
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Keymoni Sakil-Slack
#

import random

# Set range
random = random.randint(1,4)

def main():
    # Create a variable to control the loop
    again = 'y'

    while again == 'y' or again =='Y':
        # Have user choose between rock, paper, and scissors
        player = input('Choose either rock(r), paper(p), or scissors(s): ')
        # Note: 
        # r = rock
        # p = paper
        # s = scissors
        
        # Determine computer's choice 
        if random == 1:
            computer = 'r'
        elif random == 2:
            computer = 'p'
        else:
            computer = 's'

        # Set the rules/outcome for the game
        if player == computer:
            print("It's a draw! A winner must be determined...!\n")
            # If a draw, prompt user to try again.
            again = input('Try Again? (y = yes): ')
            print('__________________________________________________________\n')
        elif player == 'r' and computer == 'p':
            print('ROCK V.S. PAPER')
            print('--Paper covers Rock--')
            print('Computer wins!\n')
            # Ask the user if they would want to play again
            again = input('Play again? (y = yes): ')
            print('__________________________________________________________\n')
        elif player == 'r' and computer == 's':
            print('ROCK V.S. SCISSORS')
            print('--Rock crushes Scissors--')
            print('Player wins!\n')
            again = input('Play again? (y = yes): ')
            print('__________________________________________________________\n')
        elif player == 'p' and computer == 'r':
            print('PAPER V.S. ROCK')
            print('--Paper covers rock--')
            print('Player wins!\n')
            again = input('Play again? (y = yes): ')
            print('__________________________________________________________\n')
        elif player == 'p' and computer == 's':
            print('PAPER V.S. SCISSORS')
            print('--Scissors cuts Paper--')
            print('Computer wins!\n')
            again = input('Play again? (y = yes): ')
            print('__________________________________________________________\n')
        elif player == 's' and computer == 'r':
            print('SCISSORS V.S. ROCK')
            print('--Rock crushes Scissors--')
            print('Computer wins!\n')
            again = input('Play again? (y = yes): ')
            print('__________________________________________________________\n')
        elif player == 's' and computer == 'p':
            print('SCISSORS V.S. PAPER')
            print('--Scissors cuts Paper--')
            print('Player wins!\n')
            again = input('Play again? (y = yes): ')
            print('__________________________________________________________\n')
        
    
# Call main function    
main()

# Pseudocode:
# Prompt user to type in either rock, paper, or scissors
# Assign a variable for a random number in the range of 1 through 3
# Display user's and computer's choice
# Display outcome and select winnder
# Ask the user if they would want to play again
