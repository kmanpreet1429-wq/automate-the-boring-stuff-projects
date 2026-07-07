import sys, pyperclip
TEXT = {
    'leave': '''Hello Sir, I am not feeling well today. Kindly grant me leave.''',

'assignment': '''Good evening Ma'am. I have submitted my assignment successfully.''',

'meeting': '''I am available for the meeting after 3 PM.''',

'thanks': '''Thank you for your support and guidance.''',

'github': '''Here is my GitHub profile: https://github.com/kmanpreet1429-wq'''
}


if len(sys.argv) < 2:
    print('Please ensure corrct usage: m.clip[Keyphrase]')
    sys.exit()

keyPhrase = sys.argv[1]

if keyPhrase in TEXT:
    pyperclip.copy(TEXT[keyPhrase])
    print('The phrase for '+keyPhrase +' is copied to clipboard')

else:
    print('Keyphrase not found')




