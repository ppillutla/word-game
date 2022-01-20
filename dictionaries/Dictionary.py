import json


def load_words():
    with open('./words_dictionary.json') as word_file:
        return list(json.load(word_file).keys())


def set_seven_letter_words(words):
    return list(filter(lambda word: len(word) == 7, words))


def set_six_letter_words(words):
    return list(filter(lambda word: len(word) == 6, words))


def set_five_letter_words(words):
    return list(filter(lambda word: len(word) == 5, words))


def set_four_letter_words(words):
    return list(filter(lambda word: len(word) == 4, words))


class Dictionary(object):
    words = load_words()
    four_letter_words = set_four_letter_words(words)
    five_letter_words = set_five_letter_words(words)
    six_letter_words = set_six_letter_words(words)
    seven_letter_words = set_seven_letter_words(words)
