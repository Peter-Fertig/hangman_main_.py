#number muncher adds up all the wrong guesses
nl = []
def munch(z):
    nl.append(z)
    wg = sum(nl)
    #print(nl)
    return wg
#print(munch(1))