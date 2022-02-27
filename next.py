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

list_5 = []
while True:
    number = int(input('Введите 0 для завершения ввода \nВведите число:'))
    list_5.append(number)
    if number == 0:
        break
print(list_5)
if 777 in list_5:
    var = True
    print(var)
else:
    var = False
    print(var)






