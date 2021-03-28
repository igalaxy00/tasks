import random
import Bets


def roll():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die2 + die1


# ставка
# рол
# подсчет
def bet(i):
    print("bet")


def round():
    point = roll()
    round = True
    if point in (7, 11):
        return True
    if point in (2, 3, 12):
        return False
    while round:
        roll_result = roll()
        if roll_result == point:
            return True
        if roll_result == 7:
            return False


def game():
    bet(1)
    win = 0
    lose = 0
    experiment = 100000
    for i in range(experiment):
        lets_play = round()
        if lets_play == True:
            win += 1
        if lets_play == False:
            lose += 1
    print(win / experiment)
    print(lose / experiment)


game()
