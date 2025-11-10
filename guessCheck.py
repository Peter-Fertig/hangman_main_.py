#this module checks to see if the guess was right or wrong

def check(number):
    if number == 1:
        print("That letter is not in the phrase")
        return 1
    elif number == 0:
        return 0