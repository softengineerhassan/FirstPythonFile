import random
def get_computer_choice():
    return random.choice(["rock","paper","scissor"])
def determine_winner(player, computer):
    if player == computer:
        return("it is a tie")
    elif(
        (player == "rock" and computer == "scissor" ) or
        (player == "scissor" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        return "you win!"
    else:
        return("you lose")

def playGame():
    print("choose: rock, paper or scisoor")
    while True:
        player = input("Enter rock, paper, or scissor:").lower()
        if player not in ["rock", "paper", "scissor"]:
            print("you choose incorrect option")
            continue
        computer = get_computer_choice()
        print(f"computer choose: {computer}")
        result = determine_winner(player,computer)
        print(result)
        
        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break


playGame()