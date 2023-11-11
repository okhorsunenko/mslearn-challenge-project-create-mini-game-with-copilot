# write code in python for multiplayer game , where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console (Terminal).
# write code in python for The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# write code in python for At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# write code in python for By the end of each round, the player can choose whether to play again.
# write code in python for Display the player's score at the end of the game.



import random
game_list = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
while True:
    user_choice = input("Enter your choice: ").lower()
    computer_choice = random.choice(game_list)
    print("Computer's choice: ", computer_choice)
    if user_choice in game_list:
        if user_choice == computer_choice:
            print("Draw")
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("Computer wins")
                computer_score += 1
            elif computer_choice == "scissors":
                print("You win!")
                user_score += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("You win!")
                user_score += 1
            elif computer_choice == "scissors":
                print("Computer wins")
                computer_score += 1
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("Computer wins")
                computer_score += 1
            elif computer_choice == "paper":
                print("You win!")
                user_score += 1
        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break
    else:
        print("Invalid input")
