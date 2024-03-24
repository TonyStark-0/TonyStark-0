import random


def main():
    print("Welcome in game!")
    print("In this game, you will guess a random number between 1 and 100.")
    print("You have 10 attempts to guess the correct number.")
    print("Good luck!")

    secret_number = random.randint(1,100)
    attempts = 10

    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

        attempts -= 1

    if attempts == 0:
        print("Sorry, you have run out of attempts. The correct number was", secret_number)

if __name__ == "__main__":
    main()


