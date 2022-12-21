from operations import add, divide, multiply, substract

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