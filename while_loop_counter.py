# Program: While Loop Counter Practice
# Description: Uses a while loop and an f-string counter to print a string 5 times.

print('I am')
i = 0 # Initialize the counter variable at 0
while i < 5: # It will keep running as long as i is less than 5
    print(f'happy({i})')
    i = i + 1 # increaments the counter by 1 and avoide an infinite loop
