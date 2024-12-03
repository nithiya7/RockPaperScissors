import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!", 1
    else:
        return "You lose!", -1

def play_game():
    user_score = 0
    computer_score = 0
    rounds = int(input("How many rounds do you want to play? "))
    
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")
        
        result, score = determine_winner(user_choice, computer_choice)
        print(result)
        
        if score == 1:
            user_score += 1
        elif score == -1:
            computer_score += 1
    
    print("\nFinal Scores:")
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")
    
    if user_score > computer_score:
        print("You won the game!")
    elif user_score < computer_score:
        print("The computer won the game!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()