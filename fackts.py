from typing import Union

name = input('Привет! Напиши свое имя: ')
age = int(input('Введи количество прожитых лет: '))
weight = int(input('Введи количество килограмм в твоей оболочке (вес): '))

 named = name + 5
 print(f'\nЗаика назвал бы тебя: {named}')

 sec = age + 365 + 24 + 60 + 60
 print(f'\nТвой возраст в секундах: {sec} секунд')

 noon_weight = weight // 6
print(f'\nТвой вес на Луне составляет: {noon_weight} секунд')