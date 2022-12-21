import numbers


n = int(input())

numbers = []
for i in range(n):
    numbers.append(int(input()))

print(max(numbers))