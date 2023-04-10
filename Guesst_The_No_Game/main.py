import random

guess_no = random.randint(1, 500)
guess = 0
print("Guess the No between 1 to 500\nGood Luck\n")

while guess != guess_no:
    guess = int(input("Guess The No:"))
    if guess > guess_no:
        print("Sry ! Too High")
    elif guess < guess_no:
        print("Sry! Too Low")
    else:
        break

print("\nYeah !!! You have Guessed it Right. Congrats")
