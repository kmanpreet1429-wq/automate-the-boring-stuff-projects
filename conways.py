import random,copy,time
HEIGHT = 10
WIDTH = 20
nextcells = []

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextcells.append(column)
while True:
     currentCells = copy.deepcopy(nextcells)


     for y in range(HEIGHT):
        for x in range(WIDTH):
             print(currentCells[x][y], end='')
        print()

     for x in range(WIDTH):
        for y in range(HEIGHT):
             leftCoord = (x - 1) % WIDTH
             rightCoord = (x + 1) % WIDTH
             aboveCoord = (y - 1) % HEIGHT
             belowCoord = (y + 1) % HEIGHT
    
             numNeighbors = 0
             if currentCells[leftCoord][aboveCoord] == '#':
                  numNeighbors += 1 
             if currentCells[x][aboveCoord] == '#':
                  numNeighbors += 1 
             if currentCells[rightCoord][aboveCoord] == '#':
                  numNeighbors += 1 
             if currentCells[leftCoord][y] == '#':
                  numNeighbors += 1 
             if currentCells[rightCoord][y] == '#':
                  numNeighbors += 1 
             if currentCells[leftCoord][belowCoord] == '#':
                  numNeighbors += 1 
             if currentCells[x][belowCoord] == '#':
                  numNeighbors += 1 
             if currentCells[rightCoord][belowCoord] == '#':
                  numNeighbors += 1 

             if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                 nextcells[x][y] = '#'
             elif currentCells[x][y] == ' ' and numNeighbors == 3:
                 nextcells[x][y] = '#'
             else:
                 nextcells[x][y] = ' '
time.sleep(0.1)

