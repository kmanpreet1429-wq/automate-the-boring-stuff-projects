import random
flip=[]

for i in range(100):
    coin = random.choice(['H','T'])
    flip.append(coin)
print(flip)

count  = 0
for i in range(len(flip) - 5):
    if flip[i : i + 6] == ['H'] * 6:
        print('6 Heads found',flip[i : i + 6] )
        count = count + 1

    elif flip[i : i + 6] == ['T'] * 6:
        print("6 Tails found",flip[i : i + 6] )
        count = count + 1

print('Total Streaks:',count)

