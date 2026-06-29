#PROGRAM: Basic Login Gatekeeper
# DESCRIPTION: A simple dual-verification authentication script practicing loop
#              control mechanics. It uses 'continue' to restart the loop if the
#              username is incorrect, and 'break' to escape the infinite loop
#              entirely once both credentials match.
# ==============================================================================
while True: #Starts an infinite loop for the login prompt

    name = input('Who are you?') #Asks for a username input

    if name!= 'Joe': #It checks if the input taken by user is 'Joe' or NOT
        continue #If it is not Joe, it jumps the top of the loop again and takes input

    print('Hello joe, what is you password?') # This part will be executed only in condition if the name typed by user is 'Joe'

    password = input() #Takes input for password
    if password == 'swan': # This statement checks if the password is correct
        break # If the password is correct it will just break the statement
print('Got it!') # After breaking the statement succesfully it will print this
