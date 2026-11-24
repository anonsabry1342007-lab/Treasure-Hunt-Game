import random

print("==============================")
print("       TREASURE HUNT")
print("==============================")
print("Welcome to the Treasure Hunt!")
print("Find the hidden treasure!")
#attemps عدد المحاولات
treasure = random.randint(1, 10)
attempts = 5
print("I have hidden a treasure between 1 and 10.")
print("You have 5 attempts.")
while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == treasure:
        print("Congratulations! You found the treasure!")
        break
    else:
        attempts -= 1
        print("Sorry! Wrong guess.")
        if attempts > 0:
            print("Try again!")
            print("Attempts left:", attempts)
if attempts == 0:
    print("Game Over!")
    print("The treasure was:", treasure)

