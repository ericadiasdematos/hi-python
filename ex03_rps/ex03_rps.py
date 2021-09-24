import random

def RpcGame():

    rps = ["Rock", "Paper", "Scissors"]

    while True:

        user_choise = str(input("Enter your choise :"))
        n = random.randint(0,2)
        computer_choise = rps[n]

        if user_choise == "Rock" and computer_choise == "Rock" or user_choise == "Paper" and computer_choise == "Paper" or user_choise == "Scissors" and computer_choise == "Scissors":
            print("Its a tie")
        elif user_choise == "Rock" and computer_choise == "Scissors" or user_choise == "Paper" and computer_choise == "Rock" or user_choise == "Scissors" and computer_choise == "Paper":
            print(" User: %s , Computer: %s : The user wone!" % (user_choise, computer_choise))
            play_again = str(input("Do you want to play again ?"))
            if play_again == "no":
                break
        elif computer_choise == "Rock" and user_choise == "Scissors" or computer_choise == "Paper" and user_choise == "Rock" or computer_choise == "Scissors" and user_choise == "Paper":
            print(" User: %s , Computer: %s : The computer won!" % (user_choise, computer_choise))
            play_again = str(input("Do you want to play again ?"))
            if play_again == "no":
                break


    

RpcGame()


