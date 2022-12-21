# chislov spisuk ot sluchaini chisla
# между всяка двойка елементи от този списък се вмъква сумата от стойностите на съседните му елементи

import random

n = int(input("n = "))

l = [random.randint(1, 100) for _ in range(n)]

print(l)

n -= 1
while n > 0:
    # print(f"DEEEEEEEE: l[n] = {l[n]} l[n-1] = {l[n-1]} n = {n}")
    l.insert(n, l[n] + l[n - 1])
    n -= 1

print(l)