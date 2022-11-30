import random
# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

numbers_len = int(input('Введите длину списка: \n'))
numbers = []
modified_numbers = []
for i in range(numbers_len):
    numbers.append(random.randint(-99,99))
# print(numbers)
for i in range(numbers_len):
    if numbers[i] >= 0:
        modified_numbers.append(numbers[i])
    else:
        modified_numbers.append(numbers[i])
        modified_numbers.append(0)

print('Пусть N = ',numbers_len,', Тогда: ', numbers, ' => ', modified_numbers)
