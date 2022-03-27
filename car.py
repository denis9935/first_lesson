# class Car:
#     """Модель автомобиля и ее описание"""
#
#     def __init__(self, model, year, cash):
#         self.model = model
#         self.year = year
#         self.cash = cash
#         self.odometer = 0
#
#     def description(self, odometer=None):
#         if self.year >= 2021:
#             print(f'Модель: {self.model}, Год выпуска: {self.year}, стоимость: {self.cash}, пробег: {self.odometer}')
#         else:
#             self.odometer = odometer
#             print(f'Модель: {self.model}, Год выпуска: {self.year}, стоимость: {self.cash}, пробег: {self.odometer}')
#
#     def edit_odometer(self, km):
#         self.odometer += km
#
#
# my_car = Car('BMW', 2015, 50000)
#
# my_car.edit_odometer(25000)
# my_car.description()
