txt = 'hello 123'

with open('file11', 'wb') as f:
    f.write(txt.encode())

with open('file11', 'rb') as f:
    print(f.read().decode())
