from game_logic import determine_winner
from player import get_user_input
from computer import get_computer_choice


EMOJI_MAP={
    "rock": "✊",
    "paper": "👋",
    "scissors": "✌️"
}

def get_emoji(choice):
    return EMOJI_MAP.get(choice)



def welcome_user():
    print("Welcome to Rock, Paper, Scissors! Best of 3")
welcome_user()


valid_choices=["rock", "paper", "scissors"]

play_again = "yes"

while play_again == "yes":

    player_score=0
    computer_score=0
    round_number=1

    while (round_number<=3):
        user_choice=get_user_input(valid_choices)
        print(f"You chose: {get_emoji(user_choice)}")

        
        computer_choice=get_computer_choice(valid_choices)
        print(f"Computer chose: {get_emoji(computer_choice)}")

        result=determine_winner(user_choice, computer_choice)
        print(result)

        if result=="You win!":
            player_score+=1
        elif result=="You lose!":
            computer_score+=1

        round_number+=1    



    print("\nBest of 3 Summary ")
    print(f"You won {player_score} round(s)")
    print(f"Computer won {computer_score} round(s)")


    if player_score > computer_score:
        print("Congratulations! You won the best-of-3 game! ")
    elif computer_score > player_score:
        print("Computer wins! Better luck next time ")
    else:
        print("It's a tie! Well played!")

    play_again = input("\nDo you want to play another best-of-3 game? (yes/no): ").lower()
    while play_again not in ["yes", "no"]:
        play_again = input("Please type 'yes' or 'no': ").lower()

print("Thanks for playing! Goodbye!")





        

