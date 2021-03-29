import random


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
    # ставка
    if point in (7, 11):
        # проверка ставки
        return True
    if point in (2, 3, 12):
        # проверка ставки
        return False
    while round:
        # ставка
        roll_result = roll()
        if roll_result == point:
            # проверка ставки
            return True
        if roll_result == 7:
            # проверка ставки
            return False


def game():
    bet = 2
    win = 0
    lose = 0
    experiment = 1000000
    winnings = 0  # Ожидаемый выигрыш/проигрыш если - то казино в плюсе на эти деньги
    for i in range(experiment):
        lets_play = round()
        if lets_play == True:
            win += 1
            winnings += bet
        if lets_play == False:
            winnings -= bet

    print(winnings)  # Ожидаемый выигрыш/проигрыш если - то казино в плюсе на эти деньги

    EV_per_Unit = winnings / (experiment * bet)
    print(EV_per_Unit)  # Ожидаемый выигрыш/проигрыш на одну ставку

    House_Edge = EV_per_Unit * 100
    print(House_Edge)  # Преимущество /доход заведения (house advantage/house edge, H.A.)

    RTP = 1 + winnings / (experiment * bet)
    print(RTP)  # Процент возврата (Return To Player, RTP)

    win_chance = win / experiment
    VAR = 0
    for i in range(experiment):
        VAR += ((bet - winnings) ** 2) * win_chance
    print(VAR)

if __name__ == '__main__':
    game()
