from random import randint
num = randint(1, 10)
i = 3
while i > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == num:
        print("You guessed right!")
        break
    elif guess > num:
        i = i - 1
        print("Too high!")
        print("You have %d guesses left" % i)
    elif guess < num:
        i = i - 1
        print("Too low!")
        print("You have %d guesses left" % i)