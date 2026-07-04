name = '' 
while not name: 
    name = input('enter your name:') 

    if name == '':
        print('end') 

numOfGuests = int(input('how many guests will you have?')) 

if numOfGuests: 
    print('Be sure to have enough rooms!')

print('done')

