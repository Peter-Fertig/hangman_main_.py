#!bin/python3

def secret(phrase):
    phrase = phrase.upper()
    secretList = []
    for character in phrase:
        secretList.append(character)
    return secretList
