grade = float(input())
max_scholarship = int(input())

if grade < 4.50:
    print("no scholarship")
elif 5 > grade > 4.50:
    print(50/100*max_scholarship)
elif 5.50 > grade >= 5:
    print(70/100*max_scholarship)
elif grade >= 5.50:
    print(max_scholarship)
