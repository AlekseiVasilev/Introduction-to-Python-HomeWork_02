import random, math
# По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого.
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты.
# Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга.
# Процесс продолжается с места остановки аналогичным образом до последнего человека в круге. Составьте алгоритм, который проводит эту игру.
# Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep.
# Определите номер этого человека и количество монет, которые оказались у него в конце игры.

# P.S. рекомендации по выполнению 4-го задания.
# 1. представьте список людей в виде списка индексов: [0,1,2,3,4...];
# 2. работайте одновременно со списком монет;
# 3. не надо писать сложных систем для "Процесс продолжается с места остановки". Достаточно использовать срезы: переместите оставшуюся часть списка вперед
# 4. после каждого выбывшего пусть работает input: хотите продолжать или выйти из цикла игры?

# Остальное - это списки, циклы и условия, поэтому надеюсь, вы справитесь;)

# Не стал удалять печать в теле программы, если потом буду вспоминать как это работает, пригодиться.

players = int(input('Введите количество человек: \n'))
syllables_in_rhyme = int(input('Введите количество слогов в считалке: \n'))

# players = 6
# syllables_in_rhyme = 4

players_list = []
coin_list = []
retiring_player = 0
lost_money = 0

for choice_in_circle in range(1, players+1):
    players_list.append(choice_in_circle)

coin_list = [0] * len(players_list)

def removal_player(list, retiring):
    mod_players_list = []
    if retiring == 0 or retiring == len(list)-1:
        del list[retiring_player]
        # print(list, '=') # Временная строка
        return list
    else:
        mod_players_list.extend(list[retiring+1:])
        mod_players_list.extend(list[:retiring])
        list = mod_players_list
        # print(list, '-') # Временная строка
        return list


while len(players_list) > 1:
    for circle_repeats in range(0, math.ceil(syllables_in_rhyme/len(players_list))): # когда стал применять деление без остатка и целочисленное деление стали теряться итерации
        for choice_in_circle in range(0, len(players_list)):
            if choice_in_circle < (syllables_in_rhyme - 1) - circle_repeats * len(players_list):
                coin_list[choice_in_circle] += 1
                # print('Проход - ', circle_repeats + 1, '; Игрок - ', players_list[choice_in_circle], '; Монет у игрока - ', coin_list[choice_in_circle]) # Временная строка
            elif choice_in_circle == (syllables_in_rhyme - 1) - circle_repeats * len(players_list):
                coin_list[choice_in_circle] += 1
                lost_money = coin_list[choice_in_circle]
                retiring_player = choice_in_circle
                # print('Проход - ', circle_repeats + 1, '; Игрок - ', players_list[choice_in_circle], '; Монет у игрока - ', coin_list[choice_in_circle], '; Выбывает игрок № ', players_list[retiring_player]) # Временная строка
            else:
                coin_list[choice_in_circle] += 2
                # print('Проход - ', circle_repeats + 1, '; Игрок - ', players_list[choice_in_circle], '; Монет у игрока - ', coin_list[choice_in_circle]) # Временная строка

    # print(players_list, syllables_in_rhyme, coin_list) # Временная строка

    players_list = removal_player(players_list, retiring_player)
    # print('Измененный лист: ',players_list) # Временная строка

    if len(coin_list)-1 == retiring_player:
        coin_list[0] += lost_money
        # print('сработал if ') # Временная строка
    else:
        coin_list[retiring_player+1] +=lost_money
        # print('сработал  else ') # Временная строка

    coin_list = removal_player(coin_list, retiring_player)


print('Выиграл игрок № ', players_list[0], ', Собрано монет: ', coin_list[0]) # Временная строка

# all_people, all_money = get_people_money_lists()
# stop_word = ""
# while len(all_people) != 1:
#     all_people, all_money = game(all_people, all_money)
#     show_results(all_people, all_money)
#     input('Для продолжения нажмите Enter')
