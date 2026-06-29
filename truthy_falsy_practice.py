#PROGRAM: Basic Login Gatekeeper
# DESCRIPTION: A simple dual-verification authentication script practicing loop
#              control mechanics. It uses 'continue' to restart the loop if the
#              username is incorrect, and 'break' to escape the infinite loop
#              entirely once both credentials match.
# ==============================================================================
name = '' #Initialize an empty string. It is considered falsly in Python

while not name: #'not name' coverts falsly empty string to true to start the loop, i.e( if name = false then, not name = True)
    name = input('enter your name:') # Takes input from the user

    if name == '': # It checks if the user just pressed Enter without typing anything
        print('end') # It will end the loop then

numOfGuests = int(input('how many guests will you have?')) # Prompt for taking input and  coverts the input string to integer

if numOfGuests: # If the number of guests is any number other than 0, it evaluated true and will print this line
    print('Be sure to have enough rooms!')

print('done')

