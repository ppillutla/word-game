from word-game.dictionaries.Dictionary import Dictionary
import random


class Game(object):
    def __init__(self):
        self.points = 0
        self.found = False
        self.check_types = {
            'naa': 0,
            'ehh': 1,
            'yer': 2
        }

        dictionary = Dictionary()
        four_letter_words = dictionary.four_letter_words
        five_letter_words = dictionary.five_letter_words
        six_letter_words = dictionary.six_letter_words
        seven_letter_words = dictionary.seven_letter_words

        self.dicts = {
            4: four_letter_words,
            5: five_letter_words,
            6: six_letter_words,
            7: seven_letter_words
        }

        self.target = random.choice(self.dicts[7])
        self.target_letter_count = {}
        for c in self.target:
            if self.target_letter_count.get(c):
                self.target_letter_count[c] = self.target_letter_count.get(c) + 1
            else:
                self.target_letter_count[c] = 1

    def check_word(self, guessed_word):
        if guessed_word in self.dicts[7]:
            guess_marked_up = []

            if guessed_word == self.target:
                self.found = True
                self.points += 10
                for c in guessed_word:
                    guess_marked_up.append([c, self.check_types['yer']])
                return guess_marked_up

            else:
                ehhs = []
                for i in range(len(guessed_word)):
                    if guessed_word[i] == self.target[i]:
                        guess_marked_up.append([guessed_word[i], self.check_types['yer']])
                    elif guessed_word[i] in self.target:
                        ehhs.append(guessed_word[i])
                    else:
                        guess_marked_up.append([guessed_word[i], self.check_types['naa']])

                self.determine_ehhs(ehhs, guess_marked_up)
                return guess_marked_up
        else:
            print('Word not in dictionary')

    def determine_ehhs(self, ehhs, guess_marked_up):
        # figure out if all the ehhs are in target or if there are duplicate ehhs that are only found once in target
        # clone the target word into char array
        target_ = [c for c in self.target]
        # for each item in our marked up guess
        for item in guess_marked_up:
            # if the guessed letter is a yer
            if item[1] == self.check_types['yer']:
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
            guess_marked_up.append([e, self.check_types['ehh']])

    def check_contains_word(self, guessed_word, length):
        # check if guess is in the dictionary of words
        dictionary = self.dicts[length]
        if guessed_word not in dictionary:
            print('Invalid word')

        # check if guess has a subset of the letters from target
        guess_count = {}
        for c in guessed_word:
            if guess_count.get(c):
                guess_count[c] = guess_count.get(c) + 1
            else:
                guess_count[c] = 1

        for key in guess_count:
            if self.target_letter_count.get(key) != guess_count[key]:
                print('Your guess is not contained in the target word!')

        # if we've gotten this far, it means the guessed word can be formed
        # with only a subset of letters from the target word
        self.points += length

        guess_marked_up = []
        for letter in guessed_word:
            guess_marked_up.append([letter, self.check_types['ehh']])

        return guess_marked_up
