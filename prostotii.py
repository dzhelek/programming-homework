list1 = []
list2 = []
while number := int(input("enter number: ")):
    if number % 6 == 0:
        list1.append(number)
    if number % 7 == 0 and number % 2 != 0:
        list2.append(number)

print(list1)
print(list2)
print(f"Sum of odd indexes: {sum(list1[1::2])}")
list2.sort(reverse=True)
print(f"min(list2)*max(list2) = {min(list2)*max(list2)}")