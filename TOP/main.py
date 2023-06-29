# Делегирование + мышлениее ооп

# Двигатель и его функции
# def start():
#     print("Запуск")

# def stop():
#     print("Стоп")

# Engine = {
#     "start" : start,
#     "stop" : stop,
# }

# # Engine["start"]()
# # Engine["stop"]()
# def open():
#     print("Капот открыт")
# def close():
#     print("Капот закрыт")

# Bonnet = {
#     "open" : open,
#     "close" : close,
# }

# # Основа авто
# Car = {
#     "color" : "",
#     "marka" : "",
#     "Engine" : "",
#     "Bonnet" : Bonnet,
# }

# auto = Car
# auto["marka"] = "audi"
# auto["color"] = "green"
# auto["Engine"] = Engine
# auto["Engine"]["start"]()


# Основная функция
# def Car (marka,color):
#     thisMarka = marka
#     thisColor = color
#     activelist = {
#         "showMarka" : showMarka
#     }

# def showMarka(param):
#     print(param)
        
# auto = Car("audi","green")

# -------------------------------------------------------------

# import copy

# # Создание перса
# def attack(param):
#     print(param)

# # def shoot():
# #     print("выстрел")

# Person = {
#     "name" : "Vyilya",
#     "gender" : "Мужской",
#     "actions" : {
#         "attack" : attack
#     }
# }

# # Создание расы на основе Person
# Human = copy.deepcopy(Person)
# Human["race"] = "Человек"
# Human["skills"] = ["Быстрый бег", "Красноречие"]

# Orc = copy.deepcopy(Person)
# Orc["race"] = "Орк"
# Orc["skills"] = ["Сила", "Быстрый бег"]

# # Создание ролей на основе race
# Warrior = copy.deepcopy(Human) or copy.deepcopy(Orc)
# Warrior["role"] = "Воин"
# Warrior["desc"] = "Моя бить, моя ломать"

# Archer = copy.deepcopy(Human)
# Archer["role"] = "Лучник"
# Archer["desc"] = "Стреляй ---->>>"
# Archer["actions"]["attack"]("Стрельба")

# Shaman = copy.deepcopy(Orc)
# Shaman["role"] = "Шаман"
# Shaman["desc"] = "Ставить тоемы"
# Shaman["ataka"] = "Заклинание"
# Shaman["actions"]["attack"] = attack(Shaman["attack"])


# print(Person)
# print("-----------------------")
# print(Human)
# print("-----------------------")
# print(Orc)
# print("-----------------------")
# print(Warrior)
# print("-----------------------")
# print(Archer)
# print("-----------------------")
# print(Shaman)
# print("-----------------------")

# myPerson = copy.deepcopy(Shaman)
# myPerson["actions"]["attack"]


# Классы

# class Car:
#     def __init__(self, color, marka, engine, door, light, wheel): # создание переменных для класса (объекта)
#         self.color = color
#         self.marka = marka
#         self.engine = engine
#         self.door = door
#         self.light = light
#         self.wheel = wheel
#     # методы - действия с определенным классом
#     def showColor(self):
#         print(self.color)

    
# class Engine:
#     def __init__(self, HP, volume):
#         self.HP = HP
#         self.volume = volume

#     def start(self):
#         print("Запуск")

#     def stop(self):
#         print("Стоп")

# class Door:
#     def __init__(self, glass, handle):
#         self.glass = glass
#         self.handle = handle

#     def open(self):
#         print("Открыть")

#     def close(self):
#         print("Закрыть")

# class Light:
#     def __init__(self, glass, bulb):
#         self.glass = glass
#         self.bulb = bulb

#     def on(self):
#         print("Фары включились")

#     def off(self):
#         print("Фары выключились")

# class Wheel:
#     def __init__(self, rubber, marka):
#         self.rubber = rubber
#         self.marka = marka

#     def turnleft(self):
#         print("Поворот на лево")

#     def turnright(self):
#         print("Поворот на право")

# myWheel = Wheel ("summer", "Hankook")
# myLight = Light ("usual", 50)
# myDoor = Door ("usual", "plastic")
# myEngine = Engine(120, 2.0)
# twoEngine = Engine(280, 2.2)
# myAuto = Car("green","audi",twoEngine, myDoor, myLight, myWheel)

# # print(myAuto.engine.HP)
# # myAuto.door.open()



# # Наследование 

# class SportCar(Car):
#     def __init__(self, color, marka, engine, door, light, wheel, abs):
#         self.abs = abs
#         super().__init__(color, marka, engine, door, light, wheel)

# class EngineSport(Engine):
#     def __init__(self, HP, volume, turbo):
#         self.turbo = turbo
#         super().__init__(HP, volume)

# lamboEngine = EngineSport(900,6,2)
# twoAuto = SportCar("blue","lambo", lamboEngine, myDoor, myLight, myWheel, True)

# print(twoAuto.engine.turbo)


# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

#     def activeSound(self):
#         print(self.sound)

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Мяу")

#     def purr(self):
#         print("Мурлыкает")

# class Dog(Animal):
#     def __init__(self, name,):
#         super().__init__(name, "Гав")

#     def digHole(self):
#         print("Копает яму")

# myCat = Cat ("Вася")
# myCat.purr()