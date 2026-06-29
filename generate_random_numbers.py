# Program: Generate Random Numbers
# Description: Uses the random module and a for loop to print 5 random integers.

import random #Import Python's built-in random module to access randomizing functions

for i in range(5): # The variable i counts from 0 up to 4
    print(random.randint(1,10)) #Generate and prints any 5 random integers between 1 to 10
