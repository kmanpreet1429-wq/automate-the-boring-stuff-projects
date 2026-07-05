import random 
secretNumber = random.randint(1,20) 
print('I am thinking of a number between the range of 1 and 20')

for noOfGuesses in range(1,7): 
    print('take a guess')
    guess = int(input())

    if guess < secretNumber: 
        print('higher')
    elif guess > secretNumber: 
        print('lower')
    else: 
        break
if guess == secretNumber:
    print('you guessed the number in ' + str(noOfGuesses) + ' guesses.')
else:
    print('no...the number i was thinking was ' + str(secretNumber) + ' .')
