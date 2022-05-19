"""Списки, множества, кортежи, словари"""

# .

# list_1 = list(range(1, 5))
# print(list_1)
#
# a = 1, 2, 3, 4
# list_2 = list(a)
# print(list_2)
# names = ['Denis', 'Steve', 'Artem', 'John']
# surnames = ['Troshkin', 'Ivanov', 'Ivanov', 'Petrov']
#
# # print(names[0])
#
# # count = 0
# # for name in names:
# #     print(f'Привет {name}')
# #     count +=1
# #     if count == 2:
# #         br
# # print(names + surnames)
# # names[1] = 'Oleg'
# # print(names)
# # names += ['Anna', 'Boris']
# # print(names)
# names.insert(1, 'Ivan')
# print(names)
# del names[0]
# print(names)
# list_3 = [1,3,8,9,4]
# # print(max(list_3))
#
# # list_3.sort(reverse=False  )
# # print(list_3)
# list_4 = [int(i) for i in input().split()]
# print(list_4)

# list_5 = []
# while True:
#     number = int(input('Введите 0 для завершения ввода \nВведите число:'))
#     list_5.append(number)
#     if number == 0:
#         break
# print(list_5)
# if 777 in list_5:
#     var = True
#     print(var)
# else:
#     var = False
#     print(var)
# list_ = [x for x in range(-5, 5 )]
# # print(list_)
# #
# # list_generator = [x**2 for x in list_ if x % 2 == 0 and x > 0]
# # print(list_generator)
#
# # list_4 = []
# # for x in list_:
# #     if x % 2 == 0:
# #         list_4.append(x**2)
# # print(list_4)
# #

# tuple = (1, 2, 3, 4, 5, 2, 2, 4)
# # print(tuple)
# # print(tuple[7])
# # print(len(tuple))
# # set(tuple)
# # print(tuple)
#

# # users = {'name_1': 'Denis', 'surname_1': 'Hamenkov'}
# #
# # users['name_2'] = 'Bogdan'
# # users['name_1'] = 'Ivan'
# #
# # del users['name_1']
# # print(users)
# # print(users['name_2'])
#

# favorite_food = {
#     'Иван': 'колбаса',
#     'Георгий': 'кукуруза',
#     'Василий': 'бураки',
#     'Андрей': 'колбаса',
# }
#
# food = favorite_food['Иван']
# print(f'Любимая еда Ивана - {food}')

# N = int(input('Введите число: '))
#
# count = 0
#
# for number in str(N):
#     count += int(number)
#
# print(count)


# n = int(input('Введите год: '))
# if n % 100 == 0:
#     print('Yes')
# else:
#     print('No')

# import random
# n = int(input('Введите размер списка: '))
# list_6 = [random.randint(0, 100) for i in range(n)]
# print(list


"""  Классы  """

# class  Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def sit(self):
#         """Собака содиться по каманде"""
#         print(f'{self.name} сел')
#
#     def run(self):
#         print(f'{self.name} побежала')
#
#     def get_info(self, age):
#         print(f'Имя: {self.name}\nВозраст: {age}')
#
# my_pet = Dog('Bobik')
#
# my_pet.get_info(5)
#
# my_pet_2= Dog('Sharik')
# my_pet_2.run()
# my_pet_2.get_info(6)

# class Reustaurant:
#     def __init__(self, reustaurant_name, cuisine_type):
#         self.name = reustaurant_name
#         self.cuisine = cuisine_type
#
#     def describe_reustaurant(self, city=None):
#         if city:
#             print(f'Название ресторана: {self.name} открыт')
#
#     def cusisine_(self):
#         print(f'Блюдо: {self.cuisine}')

"""Цикл While и модуль random"""
# a = 5
# while a > 0:
#     a -= 1
#     print(a)


# import random
# names = ['name_1', 'name_2', 'name_3', 'name_4',]
# winner = random.choice(names)
# print(winner)
"""Работа с файлами"""

# with open('file_name.txt', 'r', encoding='utf-8') as text_file:
#     # text_file.write('Hello world!')
#     file_info = text_file.read()
#     print(file_info)


# def sum_(num_1, num_2):
#     print(1)
#     lust_of_nums_1 = [int(num) for num in str(num_1)]
#     lust_of_nums_2 = [int(num) for num in str(num_2)]
#
#     if sum(lust_of_nums_1) % 7 == 0 and sum(lust_of_nums_2) % 7 == 0:
#         yield f'Билеты {sum(lust_of_nums_1)}, {sum(lust_of_nums_2)} счастливые'
#     # if sum(lust_of_nums_1) % 7 == 0:
#     #     print(f'Билет {sum(lust_of_nums_1)} счастливый')
#     # if sum(lust_of_nums_2) % 7 == 0:
#     #     print(f'Билет {sum(lust_of_nums_2)} счастливый')
#
# i = list(range(111111, 999999))
#
# for num in sum_(i, i+1):
#     print(num)

"""Функции"""

# users = []
#
# def det_username(username, date=None) -> list:
#     global users
#
#     if date:
#         users.apend(f'{username.title()}, {date})
#     else:
#         users.append(username.title())
#     return users
#
# get_username('Денис')
# get_username(username='Максим')
#
# users_1 = get_username('петр', '01.12.2012')
#
# users_1 = get_username('Петр')
#
# for name in users_1:
#     print(name)

# def sum_range(start, end):
#
#     list_ = range(start, end + 1)
#
#     print(sum(list_))
#
# sum_range(1, 5)

import time

def timer():
    def wrapper(func):
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'Время выполнения функции: {end_time - start_time}')
    return wrapper

@timer()
def get_name():
    name = input('Введите ваше имя:')
    print('Привет Денис')

