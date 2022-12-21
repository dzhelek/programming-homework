from random import randint

guessed = 0
count = 0
generated_numbers = []
guessed_numbers = []

number = 1
while user := int(input("Guess the digit: ")):
    number = randint(1, 9)
    # user = int(input("Guess the digit: "))

    # if not user:
    #     break

    if number == user:
        guessed += 1
        guessed_numbers.append(number)
        print("you guessed right!")
    else:
        print("didn't guess")
    count += 1
    generated_numbers.append(number)

print(f"Total number of guesses: {count}")
print(f"Number of guessed digits: {guessed}")
print(f"Generated numbers: {generated_numbers}")
print(f"Winning numbers: {guessed_numbers}")