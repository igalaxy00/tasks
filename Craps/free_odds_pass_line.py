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
    # пас лайн
    if point in (7, 11):  # выигрыш
        # проверка ставки
        return -1111111111111111111111111
    if point in (2, 3, 12):  # проигрыш
        # проверка ставки
        return 0 # паслайн не сыграл

    # 5 - point
    # фри одс
    while round:  # пока не выыпадет 5 или 7
        # ставка
        roll_result = roll()
        if roll_result == point:
            # проверка ставки
            return point
        if roll_result == 7:
            # проверка ставки
            return 2 # не сыграл паслайн и фри одс


EV_UNIT = 0
average_winings = []
round_history = []
list_intervals_down = []
list_intervals_up = []
mat_ojidanie = 0

experiment = 1_000_000



win_chance = 0


def game():
    bet = 1
    win = 0

    capital = 1
    game_number = 0
    game_length = 0
    overall_length = 0

    winnings = 0  # Ожидаемый выигрыш/проигрыш если - то казино в плюсе на эти деньги
    for i in range(experiment):

        ####
        game_length += 1
        if capital <= 0:
            game_number += 1
            capital = 1
            overall_length += game_length
            game_length = 0
        lets_play = round()


        if lets_play== -1111111111111111111111111:# дефолтный паслайн
            round_history.append(1)
            win += 1
            winnings += bet
            capital += bet


        if lets_play in (4, 10):#сделали 4 10
            round_history.append(bet*2)
            win += 1
            winnings += bet*2+1
            capital += bet*2+1

        if lets_play in (5, 9):#сделали 5 9
            round_history.append(bet*1.5)
            win += 1
            winnings += bet*1.5+1
            capital += bet*1.5+1

        if lets_play in (6, 8):#сделали 6 8
            round_history.append(bet*1.2)
            win += 1
            winnings += bet*1.2+1
            capital += bet*1.2+1


        if lets_play == 2:# для фри одс
            round_history.append(-1)
            winnings -= bet+1
            capital -= bet+1

        if lets_play == 0:# для пас лайна
            round_history.append(-1)
            winnings -= bet
            capital -= bet



        average_winings.append(winnings / (experiment * bet))

    # Построение дов. вероятности
    disp = np.var(round_history)
    for i in range(0, len(round_history) - 1):
        list_intervals_down.append(average_winings[i + 1] - (1.65 / math.sqrt(i + 1)) * disp)
        list_intervals_up.append(average_winings[i + 1] + (1.65 / math.sqrt(i + 1)) * disp)

    # Вывод результатов
    win_chance = win / experiment
    print("Chance to win " + str(win_chance))
    print("Expected Value " + str(winnings))  # Ожидаемый выигрыш/проигрыш если - то казино в плюсе на эти деньги

    EV_per_Unit = winnings / (experiment * bet)

    print("EV per Unit " + str(EV_per_Unit))  # Ожидаемый выигрыш/проигрыш на одну ставку
    House_Edge = EV_per_Unit * 100
    print("House Edge " + str(House_Edge))  # Преимущество /доход заведения (house advantage/house edge, H.A.)

    RTP = 1 + winnings / (experiment * bet)
    print("Return to Player " + str(RTP))  # Процент возврата (Return To Player, RTP)


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


#def build_graphic():
    # -------график доверительной вероятности----
    # plt.title("График доверительной вероятности")
    # plt.hlines(mat_ojidanie, 0, 10000)
    # plt.plot(list_intervals_down)
    # plt.plot(list_intervals_up)

    # -------график средних выигрышей--------
    # plt.plot(l)
    # # медиана
    # plt.hlines(np.median(l), 0, experiment, colors='r', label='Медиана')
    # # график стремится к мат ожиданию
    # a = np.std(l)
    # plt.hlines(a, 0, experiment, colors='b', label='Ско')
    # plt.hlines(-a, 0, experiment, colors='b', label='-Ско')
    #
    # # -------график рапспределения выигрышей---------
    # plt.title("График рапспределения выигрышей")
    # # plt.vlines(-1, 0, 0.51)
    # # plt.vlines(1, 0, 0.49)
    #
    # # plt.hlines(0.5, win_chance, 1)
    # # plt.hlines(0.6, 1 - win_chance, 1)
    # plt.legend()
    # plt.show()


if __name__ == '__main__':
    game()
    #build_graphic()
