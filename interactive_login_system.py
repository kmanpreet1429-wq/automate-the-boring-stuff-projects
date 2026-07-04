while True: 
    name = input('Who are you?')
    if name != 'Joe': 
        print('You are not Joe! Access denied for this username.')
        continue  
    print('Hello Joe, what is your password?')
    password = input() 
    if password == 'swan':
        break  
    else:
        print('Joe, that password is incorrect. Try again.')
print('Got it!')
