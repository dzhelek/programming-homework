gender = input("Gender: ")

if gender == "m":
    threshold = 250000
    value = int(input("bank account: "))
elif gender == "f":
    threshold = 250000
    value = int(input("bank account: "))
elif gender == "n":
    threshold = 250000
    value = int(input("bank account: "))

if value < threshold:
    print("Your scholarship has been rejected!")
else:
    print("Your scholarship has been accepted!")