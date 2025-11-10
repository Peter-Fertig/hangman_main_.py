#!bin/python3

import guessList as gL
import secretWord as sW
import wordSpace as wS

secret = "Hello World How are You"

blank = "_"
space = " "
phrase = [blank if character != space else space for character in secret]


output = wS.blanks(phrase)

print(output)
