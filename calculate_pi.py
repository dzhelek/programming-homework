def pi(n=1000000):
    n = n * 2 + 1
    denominator = 6
    while n != 1:
        denominator = 6 + n**2/denominator 
        n -= 2
    return 3 + 1/denominator

if __name__ == '__main__':
    print(pi(0)) # 1 digit
    print(pi(2)) # 2 digits
    print(pi(10)) # 3 digits
    print(pi(50)) # 5 digits
    print(pi(100)) # 6 digits
    print(pi(500)) # 8 digits
    print(pi(1000)) # 9 digits
    print(pi(5000)) # 10 digits
    print(pi(50000)) # 14 digits
    print(pi(100000)) # 15 digits
    print(pi(1000000)) # max digits for python float