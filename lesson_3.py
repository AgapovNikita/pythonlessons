#Задание 1
# def devision ():
#     return arg_1 / arg_2
# arg_1 = int(input('Введите первое число: '))
# arg_2 = int(input('Введите второе число: '))
# if arg_2 == 0:
#     print('Делить на ноль нельзя')
# else:
#     print(devision())

#Задание 2
# def zapros ():
#     name = input('Введите cвое имя: ')
#     surname = input('Введите вашу фамилию: ')
#     year = input('Введите год рождения: ')
#     city = input('Введите городв проживания: ')
#     email = input('Введите ваш E-mail: ')
#     phone = input('Введите номер вашего телефона: ')
#     return (name + ' ' + surname + ' ' + year + ' ' + city + ' ' + email + ' ' + phone)
# print(zapros())

#Задание 3
# def sum ():
#     arg_1 = int(input('Введите первое число: '))
#     arg_2 = int(input('Введите ворое число: '))
#     arg_3 = int(input('Введите третье число: '))
#     elements = [arg_1, arg_2, arg_3]
#     elements.sort(reverse=True)
#     return elements[0] + elements[1]
# print(sum())

#Задание 4
# def func():
#     a = int(input('Введите число: '))
#     b = int(input('Введите орицательную степень: '))
#     i = -1
#     result = a
#     while i > b:
#         result = result * a
#         i = i - 1
#     return (1 / result)
# print(func())

#Задание 5
# total = 0
# while True:
#     spisok = list(input('Введите числа через пробел, либо знак "&" для завершения подсчета: ').split())
#     if spisok[-1] != '&':
#         total += sum(map(int, spisok))
#         print(total)
#     else:
#         del spisok[-1]
#         total += sum(map(int, spisok))
#         print(total)
#         break

# #Задание 6
# def capital():
#     a = input('Введите слово: ')
#     return(a.title())
# print(capital())

#Задание 7
# def capital(a):
#      return(a.title())
#
# text = input('Введите слова через пробел: ')
# print(capital(text))
