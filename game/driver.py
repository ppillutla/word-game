from word-game.Game import Game

game = Game()

while not game.found:
    # take guess input from user
    guess = input("Guess: ")
    if len(guess) == 7:
        checked_word = game.check_word(guess)
        # todo: do something with the return value (it will be each letter marked yes, no, sorta)
    elif 3 < len(guess) < 7:
        checked_word = game.check_contains_word(guess, len(guess))
        # todo: do something with the return value (it will be each letter marked yes, no, sorta)
        print('Current points: ', game.points)
    else:
        raise Exception('Invalid length')

print('Congrats! You found the target word: ', game.target)
print('Total points accumulated: ', game.points)
