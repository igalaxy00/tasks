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
    bet = 1
    win = 0
    lose = 0
    capital = 1
    game_number = 0
    game_length = 0
    overall_length = 0
    experiment = 10000000
    winnings = 0  # Ожидаемый выигрыш/проигрыш если - то казино в плюсе на эти деньги
    for i in range(experiment):
        game_length += 1
        if capital == 0:
            game_number += 1
            capital = 1
            overall_length += game_length
            game_length = 0
        lets_play = round()
        if lets_play:
            win += 1
            winnings += bet
            capital += bet
        if not lets_play:
            winnings -= bet
            capital -= bet

    print("Chance to win " + str(win / experiment))

    print("Expected Value " + str(winnings))  # Ожидаемый выигрыш/проигрыш если - то казино в плюсе на эти деньги

    EV_per_Unit = winnings / (experiment * bet)
    print("EV per Unit " + str(EV_per_Unit))  # Ожидаемый выигрыш/проигрыш на одну ставку

    House_Edge = EV_per_Unit * 100
    print("House Edge " + str(House_Edge))  # Преимущество /доход заведения (house advantage/house edge, H.A.)

    RTP = 1 + winnings / (experiment * bet)
    print("Return to Player " + str(RTP))  # Процент возврата (Return To Player, RTP)

    EV_per_Unit_Squared = EV_per_Unit ** 2
    EV_per_Squared_Unit = (win / experiment) + ((experiment - win) / experiment)
    VAR = EV_per_Squared_Unit - EV_per_Unit_Squared  # Дисперсия - возможно
    print("Возможно дисперсия " + str(VAR))

    Standart_Deviation = VAR ** 0.5
    print("Среднекватратичное отклонение " + str(Standart_Deviation))

    EV_Units = EV_per_Unit * experiment
    SD_Units = Standart_Deviation * (experiment ** 0.5)
    print("Средний суммарный выигрыш " + str(EV_Units) + "\n"
          + "Его СКО " + str(SD_Units))

    z = 1.65 
    VI = z * Standart_Deviation
    print("Индекс волатильности игры " + str(VI))

    print("Средняя продолжительность игры " + str(overall_length / game_number))


if __name__ == '__main__':
    game()
