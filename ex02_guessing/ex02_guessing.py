import random


def guessing_game():

    n = random.randint(0,10)

    print("Guess a number between 0 and 10")


    while True:
        user_number = int(input("Enter your guess :"))
        if user_number == n:
            print("Congrats! You guessed the right number: %d" % n )
            break
        elif user_number > n:
            print("The number is lower than your guess")
        elif user_number < n:
            print("The number is higher than your guess")

guessing_game() 



    


