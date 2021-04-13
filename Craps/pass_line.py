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
    if point in (2, 3, 12):  # проигрыш
        # проверка ставки
        return False
    # 5 - point
    while round:  # пока не выыпадет 5 или 7
        # ставка
        roll_result = roll()
        if roll_result == point:
            # проверка ставки
            return True
        if roll_result == 7:
            # проверка ставки
            return False


EV_UNIT = 0
l = []
l1 = []
test = []
list_intervals_down = []
list_intervals_up = []
mat_ojidanie = 0

experiment = 100000


def game():
    bet = 1
    win = 0
    d = 0

    capital = 1
    game_number = 0
    game_length = 0
    overall_length = 0

    winnings = 0  # Ожидаемый выигрыш/проигрыш если - то казино в плюсе на эти деньги
    for i in range(experiment):

        ####
        game_length += 1
        if capital == 0:
            game_number += 1
            capital = 1
            overall_length += game_length
            game_length = 0
        lets_play = round()
        if lets_play:
            test.append(1)
            win += 1
            winnings += bet
            capital += bet
        if not lets_play:
            test.append(-1)
            winnings -= bet
            capital -= bet
        l.append(winnings / (experiment * bet))

    for i in range(0, len(test) - 1):
        list_intervals_down.append(l[i + 1] - (1.65 / math.sqrt(i + 1)) * np.var(test))
        list_intervals_up.append(l[i + 1] + (1.65 / math.sqrt(i + 1)) * np.var(test))

    print("Chance to win " + str(win / experiment))

    print("Expected Value " + str(winnings))  # Ожидаемый выигрыш/проигрыш если - то казино в плюсе на эти деньги

    EV_per_Unit = winnings / (experiment * bet)
    mat_ojidanie = winnings / (experiment * bet)
    print("EV per Unit " + str(EV_per_Unit))  # Ожидаемый выигрыш/проигрыш на одну ставку

    House_Edge = EV_per_Unit * 100
    print("House Edge " + str(House_Edge))  # Преимущество /доход заведения (house advantage/house edge, H.A.)

    RTP = 1 + winnings / (experiment * bet)
    print("Return to Player " + str(RTP))  # Процент возврата (Return To Player, RTP)

    EV_per_Unit_Squared = EV_per_Unit ** 2
    EV_per_Squared_Unit = (win / experiment) + ((experiment - win) / experiment)
    VAR = EV_per_Squared_Unit - EV_per_Unit_Squared  # Дисперсия - возможно
    print("Возможно дисперсия " + str(VAR))

    print("Дисперсия 2 " + str(np.var(test)))

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
    # ГраФИК Доверительной вероятности
    plt.title("График доверительной вероятности")
    plt.hlines(mat_ojidanie, 0, 10000)
    plt.plot(list_intervals_down)
    plt.plot(list_intervals_up)
    plt.show()
    # график средних выигрышей
    plt.title("График средних выигрышей")
    l
    plt.plot(l, label='График средних выигрышей')
    # медиана
    #plt.hlines(np.median(l), 0, experiment*100, colors='r', label='Медиана')
    # график стремится к мат ожиданию

    a = np.std(l)
   #plt.hlines(a, 0, experiment*100, colors='b', label='Ско')
    #plt.hlines(-a, 0, experiment*100, colors='b', label='-Ско')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    game()
    build_graphic()
