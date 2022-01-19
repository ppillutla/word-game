points = 0
target = "" # TODO: pull from a dictionary API

def driver(word):
    if len(word) == 7:
        checkWord(word)
    elif 2 < len(word) < 7:
        checkContainsWord(word)
    else:
        error()


def checkWord(word):
    if word == target:
        return True
    # check if any letters are correctly placed 
        # add to marked letters list
    # check if any letters are correct but incorrectly placed 
        # add to marked letters list
    # return marked letters 
    return

def checkContainsWord(word):
    # check if the word can be made using the letters in target
    # if yes: 
    #   add 1 point per letter
    # if no: 
    #   return errorNotContained
    return

def error():
    return

def errorNotContained():
    return
