def is_palindrom(number):
    if str(number) == str(number)[::-1]:
        return 1
    else:
        return 0

print(is_palindrom(4334))
print(is_palindrom(1234))