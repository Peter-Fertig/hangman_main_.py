#this module asks the user to guess a letter
def ask():
    guess = input("Guess a letter:  ")
    guess = guess.upper()
    print("You guessed", guess)
    return guess
