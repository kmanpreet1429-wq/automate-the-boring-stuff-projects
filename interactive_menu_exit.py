import sys 
while True:
    response = input('Enter a number (1 or 2 or 3): ') 
    if response == '1':
        print('Hello')
    elif response == '2':
        name = input('Enter user name:')
        print('Welcome!' , name)
    elif response == '3':
        print('Program closed')
        sys.exit()
    else:
        print('Invalid choice')

