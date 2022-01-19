points = 0
target = ""  # TODO: pull from a dictionary API

check_types = {
    'naa': 0,
    'ehh': 1,
    'yer': 2
}
# todo use a real dict eventually, this is a placeholder
dictionary = ['router', 'pythons', 'amazing', 'jukebox', 'torment', 'popular', 'trample']


def driver(word):
    if len(word) == 7:
        checkWord(word)
    elif 2 < len(word) < 7:
        checkContainsWord(word)
    else:
        raise Exception('Invalid length')


def checkWord(guessed_word):
    if guessed_word in dictionary:
        guess_marked_up = []

        if guessed_word == target:
            for c in guessed_word:
                guess_marked_up.append([c, check_types['yer']])
            return guess_marked_up

        else:
            ehhs = []
            for i in range(len(guessed_word)):
                if guessed_word[i] == target[i]:
                    guess_marked_up.append([guessed_word[i], check_types['yer']])
                elif guessed_word[i] in target:
                    ehhs.append(guessed_word[i])
                else:
                    guess_marked_up.append([guessed_word[i], check_types['naa']])

            # figure out if all the ehhs are in target or if there are duplicate ehhs that are only found once in target
            target_ = [c for c in target]
            for e in ehhs:
                if e in target_:
                    target_.pop(target_.index(e))
                else:
                    ehhs.remove(e)
            # finally, add the remaining ehhs to the guess_marked_up list of tuples:
            for e in ehhs:
                guess_marked_up.append([guessed_word.index(e), check_types['ehh']])
            return guess_marked_up
    else:
        raise Exception('Word not in dictionary')

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
