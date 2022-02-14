#Задание 1
# class Matrix:
#     def __init__(self, my_list):
#         self.my_list = my_list
#
#     def __str__(self):
#         for row in self.my_list:
#             for i in row:
#                 print(f"{i:4}", end="")
#             print()
#         return ''
#
#
#     def __add__(self, other):
#         for i in range(len(self.my_list)):
#             for i_2 in range(len(other.my_list[i])):
#                 self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
#         return Matrix.__str__(self)
#
#
# m = Matrix([[5, 3, 1], [-5, 2, 11], [0, 2, -1], [8, 1, -5]])
# new_m = Matrix([[-5, 0, 2], [-2, 10, 2], [0, 4, -2], [2, 3, -7]])
# print(m.__add__(new_m))

#Задание 2
# from abc import ABC, abstractmethod
#
# class clothes(ABC):
#
#     def __init__(self, param):
#         self.param = param
#
#     @property
#     def consumption(self):
#         return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'
#
#     @abstractmethod
#     def abstract(self):
#         return 'Smth vary abstract'
#
#
# class Coat(clothes):
#     def consumption(self):
#         return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'
#
#     def abstract(self):
#         return 'Smth vary abstract second'
#
#
# class Costume(clothes):
#     def consumption(self):
#         return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'
#
#     def abstract(self):
#         pass
#
#
# coat = Coat(100)
# costume = Costume(100)
# print(coat.consumption())
# print(costume.consumption())
# print(coat.abstract())
# print(costume.abstract())

#Задание 3
# class Kletka:
#     def __init__(self, size):
#         self.size = int(size)
#
#     def __add__(self, other):
#         return f'Число ячеек общей клетки: {self.size + other.size}'
#
#     def __sub__(self, other):
#         a = self.size - other.size
#         return f'Осталось {a} клеток после вычитания ' if a > 0 else 'Разность меньше 0'
#
#     def __truediv__(self, other):
#         b = self.size // other.size
#         return f'Осталось {b} целых клетки после деления '
#
#
#     def __mul__(self, other):
#         return f'Получили {self.size * other.size} клеток полсе умножения'
#
#     def make_order(self, row):
#         result = ''
#         for i in range(int(self.size / row)):
#             result += '*' * row + '\n'
#         result += '*' * (self.size % row) + '\n'
#         return result
#
#
# kletka = Kletka(11)
# kletka2 = Kletka(5)
# print(kletka + kletka2)
# print(kletka - kletka2)
# print(kletka / kletka2)
# print(kletka * kletka2)
# print(kletka.make_order(4))