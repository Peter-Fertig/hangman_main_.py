#!bin/python3

#this module creates a list(set) if letters already guessed

guesslist = set()
def usedL(guess):
    guesslist.add(guess)
    
    return guesslist
