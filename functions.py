"""Функции"""


# def user(username, password):
#     print(f'Привет {username}!\nПароль: {password}')
#
# name = 'Denis'
# user('Denis', '181881')
# def get_name(first_name, middle_name, last_name):


#      """Возращает аккуратно отформатированные имя и фамилию"""
#      if middle_name:
#          full_name = f'{first_name} {middle_name} {last_name}'
#      else:
#          full_name = f'{first_name} {last_name}'
#      return full_name.title()
#
# user = get_name(first_name='Denis', last_name='Hamenkov', middle_name='JUBHN')
# print(user)


# def build_user(first_name, last_name, age=None):
#     user = {'name': first_name, 'surname': last_name}
#     if age:
#         user['age'] = age
#
#     return user
#
# user_ = build_user('Denis', 'Hamenkov', 15)
# print(user_)

# def users(names):
#     for name in names:
#         print(f'Hello, {name.title()}')
# name_ = ['Denis', 'alex', '']

# def fact(number):
#     if number == 0:
#         print('Факториал из нуля не извлекается')
#     elif number == 1:
#         return number
#     else:
#         return number * fact(number-1)
#
# print(fact(7))

# def print_score(name, *score):
#     print(f'Имя: {name}')
#     for score in score:
#         print(score)
#
# print_score('Denis', 3, 4, 2, 7, 6, 0)

# def draw_triangle():
#     for i in range(1, 11):
#         print('*' * i)
#
# draw_triangle()

