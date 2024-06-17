# class Car:
#     '''необязательная строка документации класса'''
#     print('я машина')
#
#
#
# print(Car.__doc__)


# class Car:
#     colour = 'blue'  # статический атрибут
#     number_of_cars = 0
#
#     def __init__(self, engine, power):  # инициализирует атрибуты класса
#         self.engine = engine  # динамический атрибут
#         self.power = power
#         Car.number_of_cars += 1  # счетчик машин
#
#
# print(Car.__dict__)  # просмотр атрибутов класса
# setattr(Car, 'engine', 1.6)  # добавляем статичный атрибут
#
# if __name__ == '__main__':  # запустить в текущей директории
#     lada = Car(8, 400)
#     print(lada.colour, lada.engine, lada.power)
#     uaz = Car(12, 300)
#     print(uaz.colour, uaz.engine, uaz.power)
#     print(Car.number_of_cars)
# print(lada.__dict__)

##14.1
# class Person:
#     def __init__(self, name: str, surname: str, age: int, pol: str):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.pol = pol
# if __name__ == '__main__':
#     vasya = Person('Vasya', 'Petrov', 29, 'man')
#     katya = Person('Katya', 'Kuoov', 34, 'female')
#     print(katya.pol)

##14.2
# class Porshe:
#     model = "911"
#     def __init__(self, colour: str, power: int):
#         self.colour = colour
#         self.power = power
# if __name__=='__main__':
#     fist_car = Porshe("green", 234)
#     second_car = Porshe('blue', 345)
#     print(fist_car.model, fist_car.colour, fist_car.power)
#     print(fist_car.__dict__)


##14.3
# class Person:
#     age = 1
#     pol = 'man'
#     def __init__(self, name: str, surname: str, age: int, pol: str):
#         self.name = name
#         self.surname = surname
#         # self.age = age
#         # self.pol = pol
#
# if __name__ == '__main__':
#     vasya = Person('Vasya', 'Petrov', 29, 'baby')
#     katya = Person('Katya', 'Kuoov', 34, 'female')
#     print(katya.pol, katya.age)
#     print(vasya.pol, vasya.age)


## Статитеский метод

# class Car:
#     colour = 'blue'  # статический атрибут
#     number_of_cars = 0
#
#     def __init__(self, engine, power):  # инициализирует атрибуты класса
#         self.color = color
#         self.engine = engine  # динамический атрибут
#         self.power = power
#         Car.number_of_cars += 1  # счетчик машин
#     def ruslan(self):
#         color = 'blue'
#         return self.faina(color)
#
#
#     @staticmethod
#     def faina(color):
#         color = "green"
#
#     @@property
#     def ppp(self):
#      ...
#     print(ppp)

##
class Car:
    def __init__(self, revenue, profit):
        self.revenue = revenue
        self.profit = profit

    def resultat(self):
        self.revenue += 20
        self.itog(self.revenue)
        return self.revenue

    @staticmethod
    def itog(argument):
        return argument - 15

    @classmethod
    def esly_ne_1_i_ne_2(cls):
        cls.itog()
