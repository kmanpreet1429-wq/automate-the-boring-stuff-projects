#PROGRAM: Rock, Paper, Scissors
#Description: A text-based Rock, Paper, Scissors game where the player competes against the computer. Keeps track of wins, losses and ties.
import random,sys

#Initialize game statistics
wins = 0
losses = 0
ties = 0

#Main game loop
while True:

    print(f'{wins} wins, {losses} losses, {ties} ties') #Display the current score

    print('enter your move:') #Takes input from the user for their move
    mymove = input().lower() #Converts input to lowercase to handle accidental capital letters

    #Player choice
    if mymove == 'q':
        sys.exit()
    elif mymove == 'r':
        print('rock V..')
    elif mymove == 'p':
        print('paper V..')
    elif mymove == 's':
        print('scissors  V..')
    else:
        print('Type r, p, s or q')
        continue
    #Computer move
    randomNumber = random.randint(1,3)

    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    if computerMove == mymove:
        print('its a tie.')
        ties += 1
    elif computerMove == 'r' and mymove == 'p':
        print('you win')
        wins += 1
    elif computerMove == 'r' and mymove == 's':
        print('you lose')
        losses += 1
    elif computerMove == 'p' and mymove == 'r':
        print('you lose')
        losses += 1
    elif computerMove == 'p' and mymove == 's':
        print('you win')
        wins += 1
    elif computerMove == 's' and mymove == 'r':
        print('you win')
        wins += 1
    elif computerMove == 's' and mymove == 'p':
        print('you lose')
        losses += 1



