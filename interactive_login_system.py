#PROGRAM: Interactive Login System
#DESCRIPTION: An advanced gatekeeper loop utilizing conditional branches.
#             Provides interactive error feedback to the user for both an
#             invalid username (triggering a loop reset via 'continue') and
#             an incorrect password (handled via 'else').
# ==============================================================================
while True: # Start an infinite loop
    name = input('Who are you?')

    if name != 'Joe': # Check if the username is correct
        print('You are not Joe! Access denied for this username.')
        continue  # Jump straight back to the top to ask "Who are you?" again

    # This part is only reached if the name WAS 'Joe'
    print('Hello Joe, what is your password?')
    password = input() # Takes input for the password

    # Check if the password is correct
    if password == 'swan':
        break  # Success! Break out of the infinite loop
    else:
        # This runs if the name was Joe, but the password wasn't 'swan'
        print('Joe, that password is incorrect. Try again.')

# Executed only after breaking the loop with the correct password
print('Got it!')
