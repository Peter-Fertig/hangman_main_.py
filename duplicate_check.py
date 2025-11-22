#This checks to see if the user has guessed a letter already.

def dupcheck(guess, letterset):
    #print(letterset)
    if guess in letterset:

        return True
    else:
        return False