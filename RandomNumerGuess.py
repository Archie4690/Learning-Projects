import random 

def game():
    guessNum = 0
    compNum = random.randint(1, 100)
    while True: 
        userGuess = input("Please take guess a number between 1-100: ")
        guessNum = guessNum + 1
        if int(userGuess) == compNum:
            print("Congratulations, the number was " + str(compNum) + " it took " + str(guessNum) + " attempts")
            playAgain()
            break
        elif int(userGuess) > compNum:
            print("Your guess was too high! Please try again.")
        elif int(userGuess) < compNum:
            print("Your guess was too low! Please try again.")

def playAgain():
    YN = input("Would you like to play again? (Y/N) ")
    if YN.lower() == "y":
        game()
    elif YN.lower() == "n":
        print("We hope you had fun!")
    else:
        print("Please answer with Y or N")
        playAgain()


game()
