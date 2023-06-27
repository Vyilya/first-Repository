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