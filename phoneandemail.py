import pyperclip,re
phone = re.compile(r'''(
                   (\d{3} | \(\d{3}\))
                   (\s | - | \.)?
                   (\d{3})
                   (\s | - | \.)?
                   (\d{4})
                   (\s*(ext|x|ext\.)\s*(\d{2,5}))?
                   )''',re.VERBOSE)


email = re.compile(r'''(
                   [a-zA-Z0-9._%+-]+
                   @
                   [a-zA-Z0-9.-]+
                   (\.[a-zA-Z]{2,4})
                   )''',re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in phone.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in email.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    result = '\n'.join(matches)

    pyperclip.copy(result)
    print('Copied to the clipboard:')
    print(result)
else:
    print('No Phone number and email address found.')

