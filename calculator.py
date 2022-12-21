# програма, която реализира калкулатор за цели числа
# действията, които могат да се изпълняват, са събиране, изваждане, умножение и деление
# потребителят въвежда вида на операцията
# след това въвежда две цели числа
# резултатът се принтира на екрана
# реализирайте отделни функции за отделните операции

def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    return 'division by zero!'


def substract(x, y):
    return x - y


function = {
    '/': divide,
    '*': multiply,
    '+': add,
    '-': substract,
}
operation = input('enter operation: (/, *, -, +)')
a = int(input('a = '))
b = int(input('b = '))
print(function[operation](a, b))