fruites = ['Apple\n', 'Banana\n', 'Orange\n']
cars = ['Audi\n', 'Toyota\n', 'Infinity\n']

with open('fruits.py', 'w') as f:
    f.writelines(fruites)

with open('fruits.py', 'r') as f:
    print(f.read(3))

with open('fruits.py', 'a+') as f:
    for car in cars:
        f.write(car)
    f.seek(0)
    print(f.read())
