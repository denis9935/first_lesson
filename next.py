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
# print(list_6)
