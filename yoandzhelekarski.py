from datetime import date
print("Hello world!")
today = date.today()

birth_day = int(input("Enter your birth day: "))
birth_month = int(input("Enter your birth month: "))

next_birthday = date(today.year, birth_month, birth_day)

if today > next_birthday:
 next_birthday = date(today.year + 1, birth_month, birth_day)

days = (next_birthday - today).days
print(days, "days to your next birthday")
