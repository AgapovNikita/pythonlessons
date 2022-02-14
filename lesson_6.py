#Задание 1
# import time
# class TrafficLight:
#     TrafficLight_color = ''
#
#     def workihg(self, TrafficLight_color):
#         self.TrafficLight_color = TrafficLight_color
#
# a = TrafficLight()
# a.workihg('Red')
# print(a.TrafficLight_color)
# time.sleep(7)
# a.workihg('Yellow')
# print(a.TrafficLight_color)
# time.sleep(2)
# a.workihg('Green')
# print(a.TrafficLight_color)
# time.sleep(4)

#Задание 2
# class road:
#
#     def __init__(self, road_length, road_width, road_thickness):
#         self.road_length = road_length
#         self.road_width = road_width
#         self.road_thickness = road_thickness
#
#     def road_massa(self):
#         b = 25 * self.road_thickness * self.road_length * self.road_width
#         print('Нужно ', b, 'кг')
#
# a = road(10, 10 ,10)
# a.road_massa()

#Задание 3
# class Worker:
#
#     def __init__(self, name='', surname='', position='', wage=0, bonus=0):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {'wage': wage, 'bonus': bonus}
#
# class Position(Worker):
#
#     def get_full_name(self):
#         print('Полное имя работника: ', self.name + ' ' + self.surname)
#
#     def get_total_income(self):
#         print('Доход с учетом премии: ', self._income['wage'] + self._income['bonus'], 'рублей')
#
# a = Position('Петр', 'Иванов', 'доктор', 200, 100)
# a.get_full_name()
# a.get_total_income()

#Задание 4
# class Car:
#
#     def __init__(self, name, speed, color, is_police=False):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.is_police = is_police
#
#     def go(self):
#         return f'Машина {self.name} поехала.'
#
#     def stop(self):
#         return f'\nМашина {self.name} остановилась.'
#
#     def turn(self, direction):
#         return f'\nМашина {self.name} повернула {direction}'
#
#     def show_speed(self):
#         return f'Ваша скорость {self.speed}!'
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             return f'Вы превысили скорость! Ваша скорость {self.speed}!'
#         else:
#             return f'Вы двигаетесь с нормальной скоростью! Ваша скорость {self.speed}!'
#
# class SportCar(Car):
#     pass
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed > 40:
#             return f'Вы превысили скорость! Ваша скорость {self.speed}!'
#         else:
#             return f'Вы двигаетесь с нормальной скоростью! Ваша скорость {self.speed}!'
#
#
# class PoliceCar(Car):
#     pass
#
#
# a = TownCar('Mazda', 120, 'blue', False)
# print('\n' + a.go(), a.show_speed(), a.turn('налево'), a.turn('направо'), a.stop())
# b = SportCar('Ferrari', 250, 'red', False)
# print('\n' + b.go(), b.show_speed(), b.turn('направо'), b.turn('налево'), b.stop())
# c = WorkCar('Kamaz', 30, 'black', False)
# print('\n' + c.go(), c.show_speed(), c.turn('направо'), c.stop())
# d = PoliceCar('Kia', 60, 'white', True)
# print('\n' + d.go(), d.show_speed(), d.turn('налево'), d.stop())

#Задание 5
# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return f'Запуск отрисовки'
#
# class Pen(Stationery):
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
#
# class Pencil(Stationery):
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
#
# class Handle(Stationery):
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
#
# a = Pen('ручкой')
# print(a.draw())
# b = Pencil('карандашем')
# print(b.draw())
# c = Handle('маркером')
# print(c.draw())