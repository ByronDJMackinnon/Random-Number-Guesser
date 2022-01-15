import random

highest_number = input("How high of a number would you like to guess to?\n")

if highest_number.isdigit():
    highest_number = int(highest_number)

    if highest_number < 0:
        print("Please type in a number larger than 0.")
        quit()

else:
    print("Please type in a number.")
    quit()

random_number = random.randint(1, highest_number)
total_guesses = -1

while True:
    total_guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess < 0:
            print("Please type in a number larger than 0.")
            continue

    else:
        print("Please type in a number.")
        continue

    if user_guess == random_number:
        print(f"That's correct!\nTotal Guesses: {total_guesses}")
        break

    elif user_guess > random_number:
        print("You were above the number.")

    elif user_guess < random_number:
        print("You were under the number.")
