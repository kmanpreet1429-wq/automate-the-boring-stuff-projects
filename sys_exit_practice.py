#PROGRAM: System Exit Practice Loop
#Description: continuously echoes user inputs until the keyword 'exit' is typed.

import sys # Import the core system module to excess the exit tool
print('Program started...')

while True: # Begin an infinite loop
    num = input('Enter:')

    if num == 'exit': # Checks if the user typed exit
        sys.exit() # Cleanly terminates program execution

    print('You entered ' + num + '.')
