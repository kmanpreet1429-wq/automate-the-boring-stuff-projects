#PROGRAM: Literal Name Matcher (Infinite Loop Exercise)
#DESCRIPTION: This script continuously prompts the user to enter their name.
#             It uses an intentional infinite loop structure ('while True') and
#             will only terminate ('break') when the user literally types
#             the string phrase 'your name'.
# ==============================================================================
while True: # Create an intentional infinite loop using True

    name = input('your name:') # Takes input from the user
    if name == 'Priya': # Exits the infinite loop immediately
        break

print('Thank You!') # Executed only after breaking out of the loop
