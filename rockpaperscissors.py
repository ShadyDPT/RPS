import random

options = {"1": "rock", "2": "paper", "3": "scissors"}

def game_sequence():
    global player_score, computer_score
    while True:
        
        choice = input("Do you choose:\n 1) Rock\n 2) Paper\n 3) Scissors\n Please enter the number that correlates to your choice.\n ")
        if not choice.isdigit():
            print("Please enter a number!")
            continue
        elif choice not in options:
            print("Please enter a valid choice!")
            continue

        player_move = options[choice] # Looks up the player's choice from the dictionary "Options". This accesses a value by its key
        computer_choice = random.choice(list(options.values())) # list(options(values)) converts options(values) to a list so random choice can pick a random option from it
    
        if player_move == computer_choice:
            print(f"You and the computer both chose {player_move}... its a draw!\n")
        elif (player_move == "rock" and computer_choice == "scissors") or \
            (player_move == "paper" and computer_choice == "rock") or \
            (player_move == "scissors" and computer_choice == "paper"):
            player_score += 1
            print(f"The computer played {computer_choice} and you won! Your score increased to {player_score}.\n ")
        else:
            computer_score += 1 
            print(f"The computer played {computer_choice} and you lost! The computer's score increased to {computer_score}.\n ")
            
        play_again()
        break
    
def play_again():
    while True:
        again = input("Would you like to play again or go back to the menu? Enter [1] for Play Again or [2] for Menu.\n ")
        if not again.isdigit():
            print("Please enter a number!")
        
        if again == "1":
            game_sequence()
            break
        elif again == "2":
            return
        else:
            print("Invalid input. Please type again...")
            
def main_menu():
    print("What would you like to do?")
    print("[1] Play")
    print("[2] View Current Scores")
    print("[3] Leave Game")
    return input(">> ")
  
# ==== main game sequence ====

player_score = 0
computer_score = 0

while True:
    choice = main_menu()
    if choice == "1":
        game_sequence()
    elif choice == "2":
        print(f"Player score: {player_score} | Computer score: {computer_score}" )
        continue
    elif choice == "3":
        print(f"Good playing! You won {player_score} times and the computer won {computer_score}! See you next time!")
        quit()        
    else:
        print("Invalid input. Please type again...")