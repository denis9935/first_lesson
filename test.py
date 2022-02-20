# print('Hello')
#
# fname = 'Denis'
# lname = 'Hamenkov'
#
# print(fname, lname

# input('Нажмите Enter')

# a = input('Введите свое имя: ')
# b = int(input('Введите ваш вопрос: '))
#
# print(type(a))
# print(type(b))

# print('''"Тут что-то не так, не будь я д'Артаньян"- подумал он."''')

# """list (список) -> [], изменяемый
# tuple (кортеж) ->, НЕизменяемый"""
#
# list = ['Denis', 'Hamenkov', 15]
# list.append('123')
# list.append(123)
#
# tuple = ('Denis', 'Hamenkov', 15)
#
# # tuple.append(123)
#
# # print(tuple)
# print(list)
# string = "всем привет, я ЛЮБЛЮ phyton!"

# print(f'Исходняя фраза: {string}')
# # print(f'Исходняя фраза: '+string)
#
# print(f'\nКогда я кричу: {string.upper()}')
#
# print(f'\nКогда я  говорю шепотом: {string.lower()}')
#
# print(f'\nС заглавных букв: {string.title()}')
#
# print(f'\nС заменой: {string.replace("ЛЮБЛЮ", "ОБОЖАЮ")}')
#
# input('Введите Entr')

# string = 'denis', 'hamenkov', 15
# print(string[0])
# print(string[1])
# print(string[2])
#
# print(string[-1])
# print(string[-2])
# print(string[-3])
#string = 'Сидел барсук в своей норе и ел картошечку пюре'
#a = '!'
#c = 'по'

#print(len(string))
#print(string + a)

#if c in string:
 #   print(f'{c} есть!')
#else:
 #   print(f'{c} нет!')
#"""***************      Условные операторы     *****************"""
# x = 5
#
#
# if x == :
#     print('Верно')
#
# elif x == 4:
#     print(4)
#
# elif x == 3:
#     print(3)
#
# else:
#     print('Ничего не верно')

# if x > 0:
# print('Число больше нуля')
#     if x == 5:
#         print('Число равно 4')
#
#     print('Едем дальше')

# if x > 0:
#     print('Число больше нуля')
#
# elif x == 4:
#     print('Число равно 0')
#
# print('Едем дальше')

# x = 0
# y = 5
#
# if x >= 0 and y >= 0:
#     print('Оба числа больше 0')
#
# if x == 5 or y == 5:
#     print('Какое-то из чисел равно 5')
#
# if x != 5:
#     print('x не равно 5')

# health = 25
#
# if health <= 0:
#     print('Персонаж мертв')
#
# else:
#     print('Персонаж жив')

# password = input('Введите пароль: ')
#
# if password == '777atom':
#     print('Пароль верный')
# else:
#     print('Пароль не верный')
# x = 6
# if x % 2 == 0 :
#     print('Число четное')
# else:
#     print('Число нечетное')
# x = 5675
# if x % 5 == 0 :
#     print('Делится')
# else:
#     print('Не делится')
# x = 2020
# if x % 4 == 0:
#     print('Год високосный')
# else:
#     print('Год не високосный')
# x = int(input('Введите x: '))
# y = int(input('Введите y: '))
# if x > 0 and y > 0:
#     print('1 четверть')
# if x < 0 and y > 0:
#     print('2 четверть')
# if x < 0 and y < 0:
#     print('3 четверть')
# if x > 0 and y < 0:
#     print('4 четверть')
# x = int(input('Ведите свой месяц рождения (число): '))
# if 0 < x > 13:
# if x  < 3 or x == 12:
#     print('За окном падал белый снег')
# elif x  > 2 and x < 6:
#     print('Птицы пели прекрасные песни')
# elif x >5 and x < 9 :
#     print('Солнце светило ярче чем когда-либо')
# elif x > 8 and x < 12:
#     print('Урожай был невероятен')
# else:
#     print('Бан')
# password = int(input('Введите пароль'))

"""Цикл for функция range"""

# numbers = 1, 2, 3, 4
#
# for i in numbers:
#     print(i)

# for i in range(10, 1, -1):
#     print(i)

# start = int(input('Введите начальное число последовательности: '))
# stop = int(input('Введите конечное число последовательности: '))
#
# for number in range(stop, start, -1):
#   if number %5 == 0:
#     if number %10 == 0:
#       continue
#     print(number)
#
# string = 'Привет Андрей!'
#
# for i in string:
#    print(i)

# for i in range(0,6):
#   if i == 3 or i == 6:
#     continue
#   print(i)
# start = int(input('Введите начальное число последовательности: '))
# stop = int(input('Введите конечное число последовательности: '))
#
# ort = 0
# pol = 0
#
# for number in range(start,stop):
#     if number < 0:
#         ort += number
#     else:
#         pol += number
#
# print(f'Сумма положительных чисел: {pol}')
# print(f'Сумма отрицательных чисел: {ort}')

# start = int(input('Введите начальное число последовательности: '))
# stop = int(input('Введите конечное число последовательности: '))
#
# quantity = 0
# sum_of_numbers = 0
#
# for number in range(start,stop):
#    sum_of_numbers += number
#    quantity += 1
#
# final = sum_of_numbers // quantity
#
#
# print(f'Среднее арифметическое последовательности от {start} до {stop}: {final}')

# number_of_string = 0
#
# for i in range(1, 6):
#   number_of_string += 1
#   print(f'Строка {number_of_string} 0')

# n = int(input('Введите число: '))
#
# for i in range(1, n+1):
#   if n > 7:
#     break
#   if i == 1:
#     print('Красный')
#   if i == 2:
#     print('Оранжевый')
#   if i == 3:
#     print('Желтый')
#   if i == 4:
#     print('Зеленый')
#   if i == 5:
#     print('Голубой')
#   if i == 6:
#     print('Синий')
#   if i == 7:
#     print('Фиолетовый')
#
#
# if n > 7 or n < 1:
#     print('Радуга состоит из 7 цветов')
# n = int(input('Введите число: '))
#
# print(f'{n} * 1 = {n * 1}')
# print(f'{n} * 2 = {n * 2}')
# print(f'{n} * 3 = {n * 3}')
# print(f'{n} * 4 = {n * 4}')
# print(f'{n} * 5 = {n * 5}')
# print(f'{n} * 6 = {n * 6}')
# print(f'{n} * 7 = {n * 7}')
# print(f'{n} * 8 = {n * 8}')
# print(f'{n} * 9 = {n * 9}')
# print(f'{n} * 10 = {n * 10}')


# for i in range(1, 11):
#   print(f'{n} x {i} = {n * i}')

# a = 'Denis', 'Hamenkov'
#
# # for i in a:
# #   print(i)
# #   for j in a:
# #     print(j)






