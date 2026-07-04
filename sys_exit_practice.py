import sys 
print('Program started...')
while True: 
    num = input('Enter:')
    if num == 'exit': 
        sys.exit() 
    print('You entered ' + num + '.')
