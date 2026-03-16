SHORTCUTS = {
    "r": "rock",
    "p": "paper",
    "s": "scissors"
}

def get_user_input(valid_choices):
    while True:
        user_input=input("Enter rock(r),paper(p), or scissors(s):").lower()

        if user_input in SHORTCUTS:
            user_choice=SHORTCUTS[user_input]
        else:
            user_choice=user_input    

        if user_choice in valid_choices:
            break
        
        if user_choice not in valid_choices:
            print("Oops! That's not a valid move. Please enter rock, paper, or scissors.")

    return user_choice