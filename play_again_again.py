def playAgain():
    playAgain = 0
    while(playAgain != "Y" or playAgain != "N"):
        playAgain = raw_input("Do you want to play again (Y or N)?: ")
        if playAgain == "Y":
            return True
        elif playAgain == "N":
            return False
        else:
            print "Invalid input"

playAgain()
