alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert(number:int, base:int):
    if base <= 0:
        raise TypeError(f"There is no base {base}")
    reminders = []
    while (number):
        reminders.append(number % base)
        number //= base
    if not reminders:
        reminders.append(0)
    reminders = [str(r) if r < 10 else alphabet[r-10] for r in reminders]
    return "".join(reminders[::-1])

if __name__ == '__main__':
    print(convert(170, 2))
    print(convert(170, 16))
    print(convert(170, 8))
    print(convert(170, 32))
    print(convert(172, 3))
    print(convert(0, 4))
    print(convert(35676, 10))
    print(convert(35676, 26))
    print(convert(20, 26))
    print(convert(1, 5))
    print(convert(1, -2))