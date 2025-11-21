#outputs blank spaces for letters to be placed in the secret phrase and replaces the blank
#spaces with correct letters

def blanks(wordspace):
    wordspace_string = "".join(wordspace)
    return wordspace_string


#print(blanks(["_", "E", "_", "_", "_"]))