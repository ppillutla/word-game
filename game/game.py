import word-game.dictionaries

# initialize dictionaries
dictionaries.main()

points = 0
target = ""  # TODO: pull from a dictionary API

check_types = {
    'naa': 0,
    'ehh': 1,
    'yer': 2
}
# todo use a real dict eventually, this is a placeholder
# dictionary = ['router', 'pythons', 'amazing', 'jukebox', 'torment', 'popular', 'trample']

four_letter_words = dicts.four_letter_words(words)
five_letter_words = dicts.five_letter_words(words)
six_letter_words = dicts.six_letter_words(words)
seven_letter_words = dicts.seven_letter_words(words)

def driver(guess):
    if len(guess) == 7:
        checkWord(guess)
    elif 2 < len(guess) < 7:
        checkContainsWord(guess)
    else:
        raise Exception('Invalid length')


def checkWord(guessed_word):
    if guessed_word in seven_letter_words:
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

            _determine_ehhs(ehhs, guess_marked_up)
            return guess_marked_up
    else:
        raise Exception('Word not in dictionary')


def _determine_ehhs(ehhs, guess_marked_up):
    # figure out if all the ehhs are in target or if there are duplicate ehhs that are only found once in target
    # clone the target word into char array
    target_ = [c for c in target]
    # for each item in our marked up guess
    for item in guess_marked_up:
        # if the guessed letter is a yer
        if item[1] == check_types['yer']:
            # pop the yer out of the target
            target_.pop(target_.index(item[0]))
    # now target_ is left with only ehhs and naas
    # for each ehh in ehhs
    for e in ehhs:
        # if the ehh is in the target
        if e in target_:
            # pop the ehh out of the target
            target_.pop(target_.index(e))
        else:
            # if the ehh is not in the target, then we have already found this ehh most likely
            # (or we screwed something else up and we are just fixing it now...)
            ehhs.remove(e)
    # finally, add the remaining ehhs to the guess_marked_up list of tuples:
    for e in ehhs:
        # for each remaining ehh letter,
        # add it to our marked up guess list with the check_type of 'ehh'
        guess_marked_up.append([e, check_types['ehh']])

def checkContainsWord(guessed_word):
    target = 'squalid'
    count = {}
    for c in target:
        if count.get(c):
            count[c] = count.get(c) + 1
        else:
            count[c] = 1
    # check if guess is in the dictionary of words
    if guessed_word not in dictionary:
        raise Exception('Invalid word')
    # check if guess has a subset of the letters from target
    guess_count = {}
    for c in guessed_word:
        if guess_count.get(c):
            guess_count[c] = guess_count.get(c) + 1
        else:
            guess_count[c] = 1
    for key in guess_count:
        if count.get(key) != guess_count[key]: raise Exception('Your guess is not contained in the target word!')
    return True

