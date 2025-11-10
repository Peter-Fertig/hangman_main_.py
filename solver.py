#this module checks to see if a letter can solve the puzzle and fills in the blanks where the letter goes.
#if it does not find a match it passes that information to guessCheck

def solve(guess, phrase, secretList):
    x = 0
    phrasel = len(phrase)
    for i in range(phrasel):
        if secretList[i] == guess:
            phrase[i] = guess
            x += 1
            y = 0
        else:
            if x >= 1:
                continue
            elif phrase[i] != "_" and phrase[i] != " ":
                continue
            elif i == phrasel - 1:
                return 1
    return y