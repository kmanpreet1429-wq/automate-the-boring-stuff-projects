sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0
uppercase_count = 0
lowercase_count = 0

for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

        if char.isupper():
            uppercase_count += 1
        else:
            lowercase_count += 1

print("\nSentence Statistics\n")

print("Total Characters :", len(sentence))
print("Characters (without spaces) :", len(sentence.replace(" ", "")))
print("Total Words :", len(sentence.split()))
print("Vowels :", vowel_count)
print("Consonants :", consonant_count)
print("Uppercase Letters :", uppercase_count)
print("Lowercase Letters :", lowercase_count)