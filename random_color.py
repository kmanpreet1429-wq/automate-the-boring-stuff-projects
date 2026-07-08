import random
def colorBall(number):
    if number == 1:
        return 'blue'

    elif number == 2:
        return 'black'

    elif number == 3:
        return 'green'

    elif number == 4:
        return 'pink'

    elif number == 5:
        return 'orange'

    elif number == 6:
        return 'purple'

    elif number == 7:
        return 'white'

r = random.randint(1,7)         #r = random.randint(1,7)           or print(magicball(random.dandint(1,7)))
print(colorBall(r))             #  pick = magicball(r)
                                #   print(pick)
