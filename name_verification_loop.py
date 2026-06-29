# PROGRAM: Name Verification Loop
# DESCRIPTION: A conditional while loop that repeatedly requests user input until
#              the correct authorized username string ('Mannu') is entered.
#              Demonstrates basic string comparison and pre-test loop execution.
# ==============================================================================
user_name = ' ' # Initialize an empty string variable to store the user's input

while user_name != 'Mannu': # This loop will run infinitely until the user explicitly inputs 'Mannu'

    user_name = input('Enter your name:') # Prompt the user for their name and capture their response
print('Thank You!') # Once the condition is met and the loop breaks, display a success message


