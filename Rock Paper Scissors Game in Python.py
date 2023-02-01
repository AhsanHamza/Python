import random #Import random package

# Define a funciton to get choices from user and computer
def get_choices():
    player_choice = input("Please Choose one: [Rock, Paper, Scissors] ")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"Player: ": player_choice, "Computer: ": computer_choice}
    return choices

# Define funciton to check who;s gonna win by using conditional statements
def check_win(player, computer):
    print(f"You choose {player}, Computer choose {computer}")
    if player == computer:
        return "Its a Tie"
    elif player == "Rock":
        if computer == "Paper":
            return "You Lose: Paper covers the Rock"
        else:
            return "You win! Rock smashes the Scissor"
    elif player == "Scissors":
        if computer == "Paper":
            return "You Win! Scissors cut the Paper"
        else:
            return "You Lose: Rock smash the Scissors"
    elif player == "Paper":
        if computer == "Rock":
            return "You Win! Paper covers the Rock"
        else:
            return "You Lose: Scissors cut the Paper"

choice = get_choices() # Declare a variable and assign function name
result = check_win(choice["Player: "], choice["Computer: "]) # Declare a variable and assign function to check the choices of player and copputer
print (result) # Print the game resul. 