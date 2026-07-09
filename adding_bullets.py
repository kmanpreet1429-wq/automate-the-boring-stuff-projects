import pyperclip

text = pyperclip.paste()
print('Before: ', text)

lines = text.split('\n')

n = len(lines)
print('Length of Text:', n)

for i in range(n):
    lines[i] = '* ' + lines[i]

line = '\n'.join(lines) 

text = pyperclip.copy(line)
print ('After: 'line)

