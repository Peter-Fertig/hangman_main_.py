#this module asks the user to guess a letter
def ask(guesslist):
    while True:
        guess = (input("Guess a letter:  "))
        if guess not in guesslist or guess.isalpha():
            guess = guess.upper()
            print("You guessed", guess)
            return guess
        elif guess in guesslist and guess.isalpha():
            print("you already guessed this letter\n\nTry again")
            continue
        else:
            print("That is not a letter\n\nTry again")
