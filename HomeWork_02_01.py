import math
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:
# 67.82 -> 23
# (-0.56) -> 11

num = input('Введите число:\n')
list_num = list(num)
print(list_num)
semple_list= []
for i in range(0, len(list_num)):
    if list_num[i].isdigit():
        semple_list.append(int(list_num[i]))
print(semple_list)
sum_numbers = sum(semple_list)
print(num, ' -> ', sum_numbers)
