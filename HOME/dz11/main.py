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