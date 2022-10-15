# scirpt to sum the elements of list having even sum of digits
import random

numbers = [random.randint(0, 100) for _ in range(10)]

result = 0

for n in numbers:
    if sum(int(digit) for digit in str(n)) % 2 == 0:
        result += n

print(numbers)
print(result)