with open('words.txt', 'r') as f:
    words = f.read().split()

print(words.count('alpha'))