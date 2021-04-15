import random
import numpy as np
import matplotlib.pyplot as plt
import math


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
    if point in (7, 11):  # выигрыш
        # проверка ставки
        return True
    if point in (2, 3):  # проигрыш
        # проверка ставки
        return False

    if point == 12:
        return

    # 5 - point
    while round:  # пока не выыпадет 5 или 7
        # ставка
        roll_result = roll()

        if roll_result == 12:
            return

        if roll_result == point:
            # проверка ставки
            return True
        if roll_result == 7:
            # проверка ставки
            return False


EV_UNIT = 0
average_winings = []
round_history = []
list_intervals_down = []
list_intervals_up = []
mat_ojidanie = 0

experiment = 5000000

win_bet = []
lose_bet = []


def game():
    bet = 1

    capital = 1
    game_number = 0
    game_length = 0
    overall_length = 0

    win = 0
    winnings = 0

    # loses = 0  # Ожидаемый выигрыш/проигрыш если - то казино в плюсе на эти деньги
    for i in range(experiment):

        game_length += 1

        if capital == 0:
            game_number += 1
            capital = 1
            overall_length += game_length
            game_length = 0

        lets_play = round()

        if lets_play is None:
            round_history.append(0)
            average_winings.append(winnings / (experiment * bet))
            continue

        if lets_play:
            lose_bet.append(-1)
            round_history.append(-1)
            winnings -= bet
            capital -= bet
        if not lets_play:
            win_bet.append(1)
            round_history.append(1)
            win += 1
            winnings += bet
            capital += bet

        average_winings.append(winnings / (experiment * bet))

    # Построение дов. вероятности
    disp = np.var(round_history)
    for i in range(0, len(round_history) - 1):
        list_intervals_down.append(average_winings[i + 1] - (1.65 / math.sqrt(i + 1)) * disp)
        list_intervals_up.append(average_winings[i + 1] + (1.65 / math.sqrt(i + 1)) * disp)

    # Вывод результатов
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
    VAR = np.var(round_history)  # Дисперсия - возможно
    print("Возможно дисперсия " + str(VAR))

    print("Дисперсия 2 " + str(np.var(round_history)))

    Standart_Deviation = VAR ** 0.5
    print("Среднекватратичное отклонение " + str(Standart_Deviation))

    EV_Units = EV_per_Unit * experiment

    SD_Units = Standart_Deviation * (experiment ** 0.5)
    print("Средний суммарный выигрыш " + str(EV_Units) + "\n"
          + "Его СКО " + str(SD_Units))

    z = 1.65
    VI = z * Standart_Deviation

    confidence_interval_low = RTP - VI / math.sqrt(experiment)
    confidence_interval_up = RTP + VI / math.sqrt(experiment)

    print("дов интервал" + str(confidence_interval_low))
    print("дов интервал врх" + str(confidence_interval_up))
    print("Индекс волатильности игры " + str(VI))
    print("Средняя продолжительность игры " + str(overall_length / game_number))


def build_graphic():
    # -------график доверительной вероятности----
    # plt.title("График доверительной вероятности")
    # plt.hlines(mat_ojidanie, 0, 10000)
    # plt.plot(list_intervals_down)
    # plt.plot(list_intervals_up)

    # -------график средних выигрышей--------
    plt.plot(average_winings)
    # медиана
    # plt.hlines(np.median(average_winings), 0, experiment*100, colors='r', label='Медиана')
    # график стремится к мат ожиданию
    a = np.std(average_winings)
    # plt.hlines(a, 0, experiment*100, colors='b', label='Ско')
    # plt.hlines(-a, 0, experiment*100, colors='b', label='-Ско')

    # -------график рапспределения выигрышей---------

    plt.show()


if __name__ == '__main__':
    game()
    build_graphic()
