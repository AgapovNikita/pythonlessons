#Задание 1
# from datetime import date
#
# class Data:
#     def __init__(self, data):
#         self.data = data.split('-')
#
#     @classmethod
#     def type(cls, data):
#         day, month, year = [int(i) for i in data.split('-')]
#         return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
#
#     @staticmethod
#     def valid(data):
#         try:
#             day, month, year = data.split('-')
#             date(int(year), int(month), int(day))
#             return 'Есть такая дата!'
#         except ValueError:
#             return 'Указана неправильная дата!'
#
# print(Data.type('25-03-2022'))
# print(Data.valid('22-02-2015'))

#Задание 2
# class OwnError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# try:
#     num_1 = int(input('Введите делимое: '))
#     num_2 = int(input('Введите делитель: '))
#     if num_2 == 0:
#         raise OwnError("Делить на ноль нельзя!")
#     else:
#         res = num_1 / num_2
#         print(res)
# except ValueError:
#     print("Вы ввели не число")
# except OwnError as err:
#     print(err)

#Задание 3
# class Error(Exception):
#     def __init__(self):
#         pass
#
# class CheckNumber:
#     def __init__(self):
#         self.my_list = []
#
#     def CheckValue(self):
#         global number
#         while True:
#             try:
#                 try:
#                     number = int(input('Введите число: '))
#                     ex = input(f'"{number}" добавлен в список.\nДля продолжения введите любой символ, для остановки введите слово stop:  ').lower()
#                     self.my_list.append(number)
#                     if ex == 'stop':
#                         print(self.my_list)
#                         break
#                 except ValueError:
#                     raise Error
#
#             except Error:
#                 ex = input(f"Вы ввели не число! Хотите продолжить? y/n: ").lower()
#                 if ex == 'n':
#                     print(self.my_list)
#                     break
#                 else:
#                     self.CheckValue()
#
# a = CheckNumber()
# a.CheckValue()

#Задание 4,5,6
# class OfficeTech:
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.items = {'Модель устройства: ': self.name, 'Цена: ': self.price, 'Количество: ': self.quantity}
#
#     def orgtech(self):
#         try:
#             name = input(f'Введите модель устройства: ')
#             price = int(input(f'Введите цену: '))
#             quantity = int(input(f'Введите количество: '))
#             item = {'Модель устройства': name, 'Цена за ед': price, 'Количество': quantity}
#             self.items.update(item)
#             print(self.items)
#         except ValueError:
#             print('Недопустимое значение!')
#
#
# class Printer(OfficeTech):
#     pass
#
# class Scanner(OfficeTech):
#     pass
#
# class Xerox(OfficeTech):
#     pass
#
# p = Printer('Hp', 2, 300)
# s = Scanner('Canon', 54000, 10)
# x = Xerox('Xerox', 7000, 15)
# p.orgtech()
# s.orgtech()
# x.orgtech()

#Задание 7
# class ComplexNumber:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __add__(self, other):
#         return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'
#
#     def __mul__(self, other):
#         return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {(self.b * other.a)+(self.a * other.b)} * i'
#
# num_1 = ComplexNumber(5, 7)
# num_2 = ComplexNumber(10, 5)
# print(num_1 + num_2)
# print(num_1 * num_2)