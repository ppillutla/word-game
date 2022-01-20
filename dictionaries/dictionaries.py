import json

four_letter_words = []
five_letter_words = []
six_letter_words = []
seven_letter_words = []

def load_words():
    with open('./words_dictionary.json') as word_file:
        words = list(json.load(word_file).keys())
        return words


def get_seven_letter_words(words):
    seven_letter_words = list(filter(lambda word: len(word) == 7, words))
    return seven_letter_words


def get_six_letter_words(words):
    six_letter_words = list(filter(lambda word: len(word) == 6, words))
    return six_letter_words


def get_five_letter_words(words):
    five_letter_words = list(filter(lambda word: len(word) == 5, words))
    return five_letter_words


def get_four_letter_words(words):
    four_letter_words = list(filter(lambda word: len(word) == 4, words))
    return four_letter_words


def main():
    words = load_words()
    four_letter_words = get_four_letter_words(words)
    five_letter_words = get_five_letter_words(words)
    six_letter_words = get_six_letter_words(words)
    seven_letter_words = get_seven_letter_words(words)
