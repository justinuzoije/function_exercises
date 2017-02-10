def playAgain():
    playAgain = raw_input("Do you want to play again (Y or N)?: ")
    if playAgain == "Y":
        return True
    else:
        return False

playAgain()
