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

# class Animal(ABC):
#     @abstractmethod
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

# class Donkey(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Йа-йа")        

# myCat = Cat ("Вася")
# myCat.purr()

# myDonkey = Donkey("Осел")
# myDonkey.activeSound()

# class Human(ABC):
#     @abstractmethod
#     def __init__(self, name, nationality):
#         self.name = name
#         self.nationality = nationality

# class Man(Human):
#     def __init__(self, name, nationality):
#         self.gender = "Мужской"
#         super().__init__(name, nationality)

# class Woman(Human):
#     def __init__(self, name, nationality):
#         self.gender = "Женский"
#         super().__init__(name, nationality)

# man = Man("Илья","Китаец")
# woman = Woman("Маня","Албанка")
        

# class Grandfather(ABC):
#     @abstractmethod
#     def __init__(self, name, hairColor):
#         self.name = name
#         self.hairColor = hairColor
#     def cookingBorscht(self):
#         print("Готовил вкусный борщ")
#     def repairCar(self):
#         print("ремонтировал авто")

# class Father(Grandfather):
#     def __init__(self, name, hairColor):
#         super().__init__(name, hairColor)


# Ilya = Grandfather("Илья", "Русый")
# Ilya.cookingBorscht()

# Mishail = Father("Михаил", "Русый")
# Mishail.cookingBorscht()


# class Bird():
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound
#     def eat(self):
#         print("Едят")
#     def hunting(self):
#         print("охотится")

#     def activeSound(self):
#         print(self.sound)

# class nofly(Bird):
#     def __init__(self, name, sound=""):
#         super().__init__(name, sound)
#     def goes(self):
#         print("ходит")

# class fly(nofly):
#     def __init__(self, name, sound=""):
#         super().__init__(name, sound)
#     def fly(self):
#         print("Летает")

# class crow(fly):
#     def __init__(self, name):
#         super().__init__(name,"Кар-кар")

# crow = crow("Вася")
# crow.activeSound()

# class Grandfather(): 
#     def __init__(self, name, hairColor):
#         self.name = name
#         self.hairColor = hairColor       
#     def cookingBorscht(self):
#         print("Готовил вкусный борщ")
#     def repairCar(self):
#         print("ремонтировал авто")

# class Father(Grandfather):
#     def __init__(self, name, hairColor):
#         super().__init__(name, hairColor)

# Ilya = Grandfather("Илья" , "русый")
# Ilya.cookingBorscht()
# Misha = Father("Миша" , "русый")
# Misha.cookingBorscht()

# from abc import ABC, abstractmethod


# base_list - база данных как SQL , не может хранить классов, функции и методы хранится где то на сервере.

# base_list = [
#     {
#         "first_name" : "Илья",
#         "last_name" : "Выборнов",
#         "birthday" : "19.11.1989",
#         "gender" : "Мужской",
#         "login" : "Vyilya",
#         "password" : "admin",
#     },
#     {
#         "first_name" : "Виталий",
#         "last_name" : "Васин",
#         "birthday" : "25.01.1999",
#         "gender" : "Мужской",
#         "login" : "Vasa",
#         "password" : "12345" ,  
#     },
#     {
#         "first_name" : "Вася",
#         "last_name" : "Ванин",
#         "birthday" : "17.11.1985",
#         "gender" : "Мужской",
#         "login" : "Vаni2",
#         "password" : "12345",
        
#     },
#     {
#         "first_name" : "Оксана",
#         "last_name" : "Олина",
#         "birthday" : "11.11.1979",
#         "gender" : "Женский",
#         "login" : "Vаni3",
#         "password" : "12345",
        
#     },
#     {
#         "first_name" : "Оля",
#         "last_name" : "Оксанина",
#         "birthday" : "01.01.1998",
#         "gender" : "Женский",
#         "login" : "Vаni4",
#         "password" : "12345",
        
#     },
# ]

# registered_users - обработанная БД с сервера, хранит в себе весь функционал пользователей, модераторов и админа.

# registered_users = [

# ]





# my_reg = Registration
# my_inLog = InLog
# my_person_list = [User,Moderator,Admin]
# my_base = []
# my_person_list[0](10, "admin" , "admin", "01.01.1970", "Мужской", "admin", "admin")
# myManager = Manager(my_reg,my_inLog,my_person_list,my_base)
# myManager.userModerAdmin[0](10, "admin" , "admin", "01.01.1970", "Мужской", "admin", "admin")
# myManager.inlog("admin", "admin")

# proverka = Registration()
# proverka.create_user()

# myAdmin = Admin(10, "admin" , "admin", "01.01.1970", "Мужской", "admin", "admin")
# myAdmin.create_users_list(base_list, registered_users)

# myLogin = InLog(input("Введите логин: "), input("Введите пароль: "))
# myLogin.log_in_account()

# myAdmin.blocking_user(registered_users)
# print(registered_users[0].update_first_name(input("введите новое имя: ")))
# print(registered_users[0].first_name)

# base_list = [
#     {
#         "first_name" : "Илья",
#         "last_name" : "Выборнов",
#         "birthday" : "19.11.1989",
#         "gender" : "Мужской",
#         "login" : "Vyilya",
#         "password" : "admin",
#     },
#     {
#         "first_name" : "Виталий",
#         "last_name" : "Васин",
#         "birthday" : "25.01.1999",
#         "gender" : "Мужской",
#         "login" : "Vasa",
#         "password" : "12345" ,  
#     },]

# primer = [
#     User(0,"name","last_name","01.01.2000", "Мужской","login","pass"),
#     User(1,"name","last_name","01.01.2000", "Мужской","login","pass"),
# ]



# r - только чтение файла read()
# w - полностью перезаписывает файл write()
# a - добавить в конец файла текст write()
# + - чтение и запись

# fileW = open("text.txt", "w", encoding="utf-8")
# fileW.write("Новый текст\n")
# fileW.write("Новый текст")
# fileW.close()

# fileR = open("text.txt", "r", encoding="utf-8")
# print(fileR.read())
# fileR.close()

import json
# открыли файл с возможностью чтения
base_list = open("base.json", "r", encoding="utf-8")
# открыли файл на чтение
base_list_read = base_list.read()
new_base = json.loads(base_list_read)
new_base.append  ({
        "first_name": "Собака",
        "last_name": "Колобака",
        "birthday": "18.08.1980",
        "gender": "Мужской",
        "login": "dog",
        "password": "admin"
    })
dumps_base = json.dumps(new_base, ensure_ascii=False)
file = open("base.json", "w", encoding="utf-8")
file.write(dumps_base)
# primer = '[{"first_name" : "Ilya", "age" : 33},{"first_name" : "Masha", "age" : 18}]'
# print(primer[0])
# massiv = json.loads(primer)
# print(massiv[0])