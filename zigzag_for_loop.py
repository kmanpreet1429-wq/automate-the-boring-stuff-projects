import time

while True:
    for indent in range(0,21):
        print(' ' * indent, end =' ')
        print('********')
        time.sleep(0.1)

        
    for indent in range(20,0,-1):
        print(' ' * indent, end =' ')
        print('********')
        time.sleep(0.1)

        