n = int(input("n = "))

l = list(range(1, n))

d = dict(zip(l, l[::-1]))

print(d)