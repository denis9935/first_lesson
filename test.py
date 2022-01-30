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
string = 'Сидел барсук в своей норе и ел картошечку пюре'
a = '!'
c = 'по'

print(len(string))
print(string + a)

if c in string:
    print(f'{c} есть!')
else:
    print(f'{c} нет!')