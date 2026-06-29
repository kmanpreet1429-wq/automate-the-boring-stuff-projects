# PROGRAM: Number Triangle Pattern
# Description: Generates an increment number triangle using nested loops.

print('my name is')

for i in range(1,6): #Outer loop: Controls the number of rows (loops from 1 up to 5)
    for j in range(1,i+1): # Inner loop: Controls the number printed inside each specific row
        print(j,end = '') # Print the current number followed by space instead of new line
    print('') #Prints blank space to move to the next row after inner loop finishes
