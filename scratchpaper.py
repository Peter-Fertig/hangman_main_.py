for x in range(9):
    if "_" in phrase:
        print(wS.blanks(phrase))
        letterguess = ATG.ask()
        print(gL.usedL(letterguess))
        #solve(ATG.ask(), phrase, sW.secret(secret))
        number = solve(letterguess, phrase, sW.secret(secret))
        #nM.munch(gC.check(number))
        wrong = nM.munch(gC.check(number))
        print("you guessed wrong ", wrong," times" )
    else:
        eG.win(secret)
        break
else: print("YOU LOSE!!")