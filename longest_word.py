with open('words.txt', 'r') as f:
    words = f.read().split()
    # longest = words[0]
    # for word in words:
    #     if len(word) > len(longest):
    #         longest = word
    print(max(words, key=len))
