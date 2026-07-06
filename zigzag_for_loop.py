import time

indent = 0
indentIncreasing = True

while True:
    for indent in range(0,21):
        print(' ' * indent, end =' ')
        print('********')
        time.sleep(0.1)

    #for indent in range(20,0,-1):
        #print(' ' * indent, end =' ')
        #print('********')
        #time.sleep(0.1)

        if indent == 20:
            indentincreasing = False
        
    for indent in range(20,0,-1):
        print(' ' * indent, end =' ')
        print('********')
        time.sleep(0.1)

        if indent == 0:
            indentIncreasing = True
