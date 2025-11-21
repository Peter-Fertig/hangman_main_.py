#!bin/python3

import guessList as gL
import secretWord as sW
import wordSpace as wS
import ask_to_guess as ATG
import guessCheck as gC
import numberMuncher as nM
from solver import solve
import endGame as eG
secret = "sail boat"
secret = secret.upper()

blank = "_"
space = " "
phrase = [blank if character != space else space for character in secret]

while "_" in phrase:
    print(wS.blanks(phrase))
    letterguess = ATG.ask(gL.usedL())
    print("letters guessed so far: ", gL.usedL(letterguess))
    #solve(ATG.ask(), phrase, sW.secret(secret))
    number = solve(letterguess, phrase, sW.secret(secret))
    #nM.munch(gC.check(number))
    wrong = nM.munch(gC.check(number))
    if "_" in phrase:
        print("you guessed wrong ", wrong," times" )
    if wrong == 5:
        print("YOU LOSE!!")
        break
else:
    eG.win(secret)

#####TO FIX####
#wrong counter counts against you if you guess wrong letter twice
#in letter guess check for letters already guessed and do not accept non-letters