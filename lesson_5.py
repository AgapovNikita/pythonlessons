# #Задание 1
# my_file = open("My_File.txt", "w+", encoding='utf-8')
# new_list = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n', ]
# my_file.writelines(new_list)
# my_file.close()
#
# my_file = open("My_File.txt", "a", encoding='utf-8')
# my_file.write("Привет, файл!")
# my_file.close()
#
# my_file = open("My_File.txt", "a", encoding='utf-8')
# new_list = ['\n']
# my_file.writelines(new_list)
# my_file.close()

# #Задание 2
# object = open('task_2.txt', 'r')
# lines = sum(1 for line in object)
# print('В файле', lines, 'строки')
#
# object = open('task_2.txt', 'r')
# a = 1
# while a < lines + 1:
#     words = object.readline().split()
#     print('В', a, 'строке', len(words), 'слов(а).')
#     a += 1
# object.close()

#Задание 3
# vedomost = {}
# with open("task_3.txt", encoding='utf-8') as file:
#     for line in file:
#         key, value = line.split()
#         vedomost[key] = int(value)
# print(vedomost)
# workers = len(vedomost.values())
# all_zp = sum(vedomost.values())
# middle_zp = all_zp / workers
# print('Средняя зарплата: ', middle_zp)
# print([i for i in vedomost if vedomost[i] < 20000])

#Задание 4
# with open('task_4.txt', 'r+', encoding="utf-8") as file:
#     lst = list()
#     for line in file.readlines():
#         lst.extend(line.split(' '))
#
# rus_lst = ["Один ", "Два ", "Три ", "Четыре "]
#
# a = 0
# for i in range(0, len(lst), 3):
#     lst[i] = rus_lst[a]
#     a += 1
# print(lst)
# out_f = open('task_04_rus.txt', 'w', encoding='utf-8')
# out_f.writelines(lst)

#Задание 5
# with open('task-5.txt', 'r') as object:
#     summa = object.readlines()
#     result = [sum(map(int, i.split())) for i in summa]
#     print(result)

#Задание 6
# file = open("task_6.txt", encoding='utf-8')
# predmet = file.read().split("\n")[:-1]
# print(predmet)
# dict = {}
# file = open("task_6.txt", encoding='utf-8')
# for item in predmet:
#     key = item.split(" ")[0]
#     value = sum(int(x) for x in file.readline().split() if x.isdigit())
#     dict[key] = value
# print(dict)

#Задание 7
