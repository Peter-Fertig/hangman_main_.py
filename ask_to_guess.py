#this module asks the user to guess a letter
def ask():
    while True:
        guess = (input("Guess a letter:  "))
        if guess.isalpha():
            guess = guess.upper()
            #print("You guessed", guess)
            return guess
        else:
            print("That is not a letter\n\nTry again")