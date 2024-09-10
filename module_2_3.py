# 1-й Вариант решения с ограничением до первого отрицательного числа
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
print('Положительные числа с ограничением до первого отрицательного числа:')
print(len(my_list))
while i < len(my_list):
    if my_list[i] == 0:
        i = i + 1
    elif my_list[i] >= 0:
        print(my_list[i])
        i = i + 1
    else:
        break
print(' ')

# 2-й Вариант решения с ограничением до конца списка
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
print('Положительные числа из всего списка:')
while i < len(my_list):
    if my_list[i] == 0 or my_list[i] < 0:
        i = i + 1
    elif my_list[i] >= 0:
        print(my_list[i])
        i = i + 1
    else:
        break
