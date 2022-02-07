#Задание 1
# from sys import argv
#
# script_name, name, virabotka, stavka, premia = argv
# virabotka = int(virabotka)
# stavka = int(stavka)
# premia = int(premia)
#
# print("Имя скрипта: ", script_name)
# print("Имя работника: ", name)
# print("Зарплата: ", virabotka * stavka + premia)
# #python lesson_4.py nikita 3 3 3 - ввод в терминале пайтона.

#Задание 2
# from random import randint
#
# numbers = [randint(1, 500) for i in range(20)]
# print(numbers)
# result = []
# for i in range(len(numbers) - 1):
#     if numbers[i] < numbers[i+1]:
#         result.append(numbers[i+1])
# print(result)

#Задание 3
# spisok= [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
# print(spisok)

#Задание 4
# from random import randint
# numbers = [randint(1, 30) for i in range(10)] + [randint(1, 30) for i in range(10)]
# print(numbers)
# new_numbers = []
# for i in numbers:
#     if numbers.count(i) == 1:
#         new_numbers.append(i)
# print(new_numbers)

#Задание 5
# from functools import reduce
# result = reduce(lambda x, y: x*y, [i for i in range(100, 1001) if i % 2 == 0])
# print(result)

#Задание 6
# from itertools import count, cycle
#
# spisok = []
# for i in count(7):
#     if i > 15:
#         break
#     else:
#         spisok.append(i)
# a = 0
# for el in cycle(spisok):
#     if a > 50:
#         break
#     print(el)
#     a += 1

#Задание 7
# def fact(n):
#     a = 1
#     for i in range(1, n+1):
#         a *= i
#         yield a
#
# for el in fact(4):
#     print(el)