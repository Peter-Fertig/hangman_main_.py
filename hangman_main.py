#!bin/python3

import guessList as gL
import secretWord as sW
import wordSpace as wS
import ask_to_guess as ATG
import guessCheck as gC
import numberMuncher as nM
from solver import solve
import endGame as eG
secret = "Hello World How are You"

blank = "_"
space = " "
phrase = [blank if character != space else space for character in secret]

for x in range(9):
    if "_" in phrase:
        ATG.ask()
        wS.blanks(phrase)

    else:
        eG.win(secret)
        break
else: print("YOU LOSE!!")

togesscheck = solve(ATG.ask(), phrase, sW.secret(secret))

print(togesscheck)
print(phrase)
print(gC.check(togesscheck))