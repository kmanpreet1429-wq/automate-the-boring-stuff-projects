#PROGRAM: Guess the  Number game
#Description: A game where a player tries to guess a random number in 6 tries.

import random # Import the random module to generate a secret number

secretNumber = random.randint(1,20) #Generate a random target integer between 1 and 20
print('I am thinking of a number between the range of 1 and 20')

for noOfGuesses in range(1,7): # Allow the player up to 6 guesses
    print('take a guess')
    guess = int(input())

    if guess < secretNumber: # Checks if the guess is too low
        print('higher')
    elif guess > secretNumber: # Checks if the guess is too high
        print('lower')
    else: # If the guess is correct, Break out of the loop early
        break

if guess == secretNumber:
    print('you guessed the number in ' + str(noOfGuesses) + ' guesses.')
else:
    print('no...the number i was thinking was ' + str(secretNumber) + ' .')
