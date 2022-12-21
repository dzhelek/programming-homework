while True:
    try:
        age = int(input("enter your age: "))
        if 0 < age < 150:
            break
        print('not a valid age!')
    except ValueError:
        print('not a valid number!')

if age < 18:
    print('you are not legal to vote')
else:
    print('you can vote')