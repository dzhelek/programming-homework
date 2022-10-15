from math import prod


# function to calculate the sin of any number using infinite fraction
def sin(x, n=10):
    n = n * 2
    denominator = (n + 2) * (n + 3) - x**2
    while n:
        product = n * (n + 1)
        denominator = product - x**2 + product * x**2 / denominator
        n -= 2
    denominator = 1 + x**2 / denominator
    return x / denominator

if __name__ == '__main__':
    print(sin(3.14, 10))
    print(sin(3.14, 1000))
    print(sin(2*3.14, 1000))
    print(sin(3.14/2, 1000))
    print(sin(3*3.14/2, 1000))
    print(sin(3.14/4, 1000))
    print(sin(3.14/4, 100))
    print(sin(3.14/4, 10))
    print(sin(3.14/4, 1))
    from math import sqrt
    print(sqrt(2)/2)