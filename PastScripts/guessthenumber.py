import random
number=random.randint(1,5)
guess, ct = 0,0
while guess != number:
    guess = int(input("Can you get the number between 1 and 10?"))
    if guess == number:
        ct=ct+1
        print(f"Correct! You guessed the number {guess} and it too {ct} tries")
    else:
        print("wrong, press guess again")
        ct=ct+1
