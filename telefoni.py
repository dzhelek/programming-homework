class Phone:
    def __init__(self, brand, model, price, quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity
    
    def print(self):
        print(f"{self.quantity}x {self.brand} {self.model}, ${self.price}")


def phone_max_price(phones):
    return max(phones, key=lambda phone: phone.price)


phones = [
    Phone('Samsung', 'Galaxy S 21', 100, 20),
    Phone('Samsung', 'Galaxy Z Flip', 1000, 10),
    Phone('Apple', '11 pro max giga tera super +', 10000, 1),
]

brand = input('enter brand: ')
for phone in phones:
    if phone.brand == brand:
        phone.print()

print("Max price phone: ")
phone_max_price(phones).print()