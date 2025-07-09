import random
def guessNumberGame():
    secret_number = random.randint(1,100)
    attempts_left = 7
    print("guess the number between 1 &&&&&&&&&&&&&&&&&&&&& 100")
    print(f"you have {attempts_left} attempts.\n" )
    while attempts_left>0:
        guess = int(input("Guess the number!"))
        attempts_left -= 1
        if guess == secret_number:
            print(f"congratulations you guessed the number in{7-attempts_left} attempts")
        elif guess<secret_number:
            print("too low:")
        else:
            print("too high")
        if attempts_left>0:
            print(f"you have {attempts_left} attempts!")
        else:
            print(f"you have not enough attempts: the number was{secret_number}")
guessNumberGame()