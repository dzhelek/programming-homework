vowels = 'aeiou'

with open('words.txt', 'r') as f:
    words = f.read().split()

with open('vowel_words.txt', 'w') as f:
    for word in words:
        if word[0] in vowels:
            f.write(word + ' ')
