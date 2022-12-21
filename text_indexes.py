def from_indexes(text, *indexes):
    return "".join(text[i] for i in indexes if i < len(text))

print(from_indexes('hello world', 0, 1, 100, 9, 5, 6, 7, 6, 100))