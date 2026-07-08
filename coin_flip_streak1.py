
import random
flip = []

for i in range(10000):
    flip.append(random.choice(['H' , 'T']))
print(flip)

head_count = 0
tail_count = 0
for i in range(len(flip) - 5):

    if flip[i : i + 6] == ['H'] * 6:
        print('6 Heads found',flip[ i : i + 6])
        head_count += 1

    elif flip[ i : i + 6] == ['T'] * 6:
        print('6 Tails Found',flip[ i : i + 6])
        tail_count += 1

print('No. of Heads:',head_count)
print('No. of Tails:',tail_count)
print('Total:',head_count + tail_count)
