import random

game_choice = ["Rock", "Paper", "Scissors"]
computer = 0
player = 0
print("Score : Computer= " + str(computer) + " " + "Player=  " + str(player))

while True:
    computer_choice = random.choice(game_choice)
    player_choice = input("Rock, Paper, Scissors Or Quit: ").strip()
    if computer_choice == player_choice:
        print("Balance")

    elif player_choice == "Rock":
        if computer_choice == "Paper":
            print("Computer Win")
            computer += 1
        else:
            print("Player Win")
            player += 1

    elif player_choice == "Paper":
        if computer_choice == "Rock":
            print("Player Win")
            player += 1
        else:
            print("Computer Win")
            computer += 1

    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            print("Computer Win")
            computer += 1
        else:
            print("Player Win")
            player += 1

    elif player_choice == "Quit":
        print("End")
        break
    else:
        print("Wrong Choice")
        break

    print("Player: " + player_choice)
    print("Computer: " + computer_choice)
    print("Score: Computer= " + str(computer) + " " + "Player= " + str(player))
    print(" ----------------- ")