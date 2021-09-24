import random
import words

def wordsGame():

    n = random.randint(0,4)
    computer_word = random.choice(words.english_words)
    chances = 0

    while True:

        user_choise = str(input("Choose a letter :"))

        print(computer_word)

        if user_choise in computer_word:
            print("Good! That letter is in the word! Keep going")
        elif chances == 5:
            print("Game over")
            break
        elif user_choise not in computer_word:
            print("That letter is not in the word, try again")
            chances += 1

wordsGame()


