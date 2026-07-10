sentence = input('Enter a sentence:')
VOWELS = ('a', 'e', 'i', 'o', 'u')
words = sentence.split()

for word in words:
    prefix_words = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_words += word[0]
        word = word[1:]
    
    suffix_words = ''
    while len(word) > 0 and not word[-1].isalpha():
        suffix_words = word[-1] + suffix_words
        word = word[:-1]
    

    is_uppercase = word.isupper()
    is_titlecase = word.istitle()
    word = word.lower()

    if word[0] in VOWELS :
        pig_latin = word + 'yay'
    else:
        consonents = ''
        while len(word) > 0 and word[0] not in VOWELS:
            consonents += word[0]
            word = word[1:]

        pig_latin = word + consonents + 'ay'

    if is_uppercase:
        pig_latin = pig_latin.upper()
    elif is_titlecase:
        pig_latin = pig_latin.title()

    pig_latin = prefix_words + pig_latin + suffix_words
    print(pig_latin,end = '')
    







    

