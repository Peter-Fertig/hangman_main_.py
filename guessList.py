#!bin/python3

#this module creates a list(set) if letters already guessed

guesslist = set()

def oldlist():
    return guesslist

def usedL(guess):

    newlist = guesslist.add(guess)
    
    return guesslist
