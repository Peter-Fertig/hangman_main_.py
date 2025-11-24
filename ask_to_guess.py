#this module asks the user to guess a letter
from gui_hangman import letter


def ask(*args):
    try:
        guess = str(letter.get())
        guess.set
    except ValueError:
        pass