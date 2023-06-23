# print ("Hello word")
# x = 5
# print (x*2)
# print (x*3)
# print (x*4)
# print (x*5)
# print (x*6)
# print (x*7)
# print (x*8)
# print (x*9)

# type_int = 1 # целые числа (int)
# type_float = 1.23 # числа с точкой
# type_str = "Строки пишутся в кавычках"
# type_bool_one = True # булевы значения истина (правда)
# type_bool_two = False # булевы значения ложь
# type_none = None

# a = 123 #int
# print (a * 2, type(a)) #int
# a = str(a) # str
# print (a * 2, type(a)) #str
# a = float(f) # float
# print (a * 2, type(a)) #float

# b = "123"
# print (b, type(b)) 
# b = int (b)
# print (b, type(b))
# b = 2

# c = int(input("Мы умножим ваше число на два")) # input по умолчанию строковый с int числовым
# print(c* 2)

# print("Заполните Информацию")
# myName = input("Введите имя: ")
# firstName = input("Введите фамилию: ")
# Age = int(input("Укажите возраст: "))
# Jop = input ("Место работы: ")

# print("Информация о пользователе")
# print("Имя: ", myName)
# print("Фамилия: ", firstName)
# print("Возраст :", Age )
# print("Работа: ", Jop)

# myName = "Илья"
# print("Привет" + " " + myName) # Конкатенация складываем строки
# print(f"Привет {myName}") # шаблон строки
# print("Привет"," ","мир!")

# x = int(input("введите число: "))
# print(x // 10) # // - деление до целого
# print(x % 10) # % - остаток

# a = 2
# b = 3
# h = a / b * 10
# print(int(h))
# print(type(h))

# x = int(input("введите число: "))

# x1 = (x % 10)
# x = x // 10
# x2 = (x % 10)
# x = x // 10
# x3 = (x % 10)
# print(x1)
# print(x2)
# print(x3)
# sum = (x1+x2+x3)
# print(sum)

# x = int(input("введите число: "))
# z = int(input("введите число: "))
# y = str(x)+str(z)
# y = int (y)
# print (y)

# a = 5
# b = 10
# print(a>b)
# print(a<b)

# a = 5
# b = 10
# if (a < b and b > 10) or a == 5: #True
#     print("if выполнился")
# # if a > b: #False
# #     print("if 2 выполнился")
# else:
#     print("else выполнился")
    
    
# a = 5
# b = 10
# if a > b:
#     print("if выполнился") #True
# elif a < b:
#     print("elif выполнился")
# else:
#     print("else выполнился")

    
# login = input("Ведите логин: ")
# password = input("Ведите пароль: ")
# if login == "admin":
#     if password == "admin":
#         print("Вход выполнен")

#     else:
#         print("Не верный логин или пароль : 2 условие")
#         # help = input("Сообщение для тех поддержки")
# else:
#     print("Не верный логин или пароль : 1 условие")

# q1 = input("Зимой и летом одним цветом: ")
# score = 0
# if q1 == "ёлка" or q1 == "елка":
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ не верный")
    
# q2 = input("Висит груша нельзя скушать: ")
# if q2 == "лампочка":
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ не верный")
    
# q3 = input("Что выше леса поднимается да без огня горит: ")
# if q3 == "солнце":
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ не верный")

# q4 = input("Без рук, без ног, А ворота открывает: ")
# if q4 == "ветер":
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ не верный")
# q5 = input("На дворе горой, а в избе водой: ")
# if q5 == "снег":
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ не верный")
# print("У Вас очков: " , score)

# if score >= 3:
#     x = input("Хотите ответить на доп. вопрос? ")
#     if x == ("да" or "yes"):
#        y = input("Ах, не трогайте меня!Обожгу и без огня: ")
#        if y == "крапива":
#         print("Ответ верный, игра окончена")
#        else:
#         print("Игра Окончена, все очки сгорели")             
#     else:
#         print("Игра Окончена")

# != - не равно

# x = int(input("введите число: "))
# if x % 2 == 0:
#     print("четное")
# else:
#     print("неченое")

# x = int(input("введите число: "))
# y = int(input("введите число: "))
# s = int(input("0 - сумма, 1 - раздница, 2 - средняя, 3 - произведение: "))
# if s == 0:
#     print(x + y)
# elif s == 1:
#     print(x - y)
# elif s == 2:
#     print(x + y / 2)
# elif s == 3:
#     print(x * y)
# else:
#     print("введите корректное значение")

#ЗАДАЧА 3 Пользователь вводит с клавиатуры номер месяца программа выводит на экран надпись: Winter (если введено
# значение 1,2 или 12), Spring (если введено значение от 3
# до 5), Summer (если введено значение от 6 до 8), Autumn
# (если введено значение от 9 до 11).
# Если пользователь ввел значение не в диапазоне от 1
# до 12 требуется вывести сообщение об ошибке.

# x = int(input("Введите число месяца (от 1 до 12): "))
# if x == 1 or x == 2 or x == 12:
#     print("Зима")
# elif x == 3 or x == 4 or x == 5:
#     print("Весна")
# elif x == 6 or x == 7 or x == 8:
#     print("Лето")
# elif x == 9 or x == 10 or x == 11:
#     print("Осень")
# else:
#     print("Ошибка")

# ЗАДАЧА
# Високосные года делятся нацело на 4. Однако из этого правила есть исключение: столетия, которые не делятся нацело на 400, високосными не являются.
# В високосном годе 366 дней, в обычном 365.
# Если год не делится на 4, значит он обычный.
# Иначе надо проверить не делится ли год на 100.
# Если не делится, значит это не столетие и можно сделать вывод, что год високосный.
# Если делится на 100, значит это столетие и его следует проверить его делимость на 400.
# Если год делится на 400, то он високосный.
# Иначе год обычный.

# x = int(input("Введите год: "))
# if x % 4 == 0:
#     print("Високосный")
# elif x % 100 == 0:
#     if x % 400 == 0:
#         print("Обычный")
#     else:
#         print("Високосный")
# else:
#     print("Обычный")

# Задача: 
# Треугольник существует только тогда, когда сумма длин любых его двух сторон больше третьей стороны. Иначе две стороны просто «укладываются» на третьей.
# Треугольник является разносторонним, если все его стороны имеют разную длину; треугольник будет равнобедренным, если любые две его стороны равны между собой, но отличны от третьей; и треугольник является равносторонним, когда все его стороны равны.
# Прежде чем выяснять вид треугольника, необходимо удостовериться, что треугольник существует.
# Если треугольник существует, то можно сначала проверить на неравенство три его стороны. Если они не равны друг другу, то треугольник разносторонний. Если это не так, то следующим шагом будет проверка на равенство всех сторон треугольника. Если все стороны равны, делается вывод о том, что треугольник равносторонний. Иначе остается только один вариант — равнобедренный треугольник.

# a = int(input("введите число: "))
# b = int(input("введите число: "))
# c = int(input("введите число: "))
# if a + b > c and a + c > b and c + b > a:
#     print("Треугольник существует")
#     if a != b and a != c and c != b:
#          print("Треугольник разносторонний")   
#     elif a == b and a == c and c == b:
#         print("Треугольник равносторонний")
#     else:
#         print("Треугольник равнобедренный")
# else:
#     print("Треугольник не существует")

# nameGame = "Подземелья"
# print("Добро пожаловать \n 'Подземелья'")


# print("Выберите пол персонажа:\n", "ж-женский\n", "м-Мужской")
# gender = str(input("Введите ж или м :\n"))
# if gender == "М" or gender == "м":
#   gender = "Мужской"
# elif gender == "Ж" or gender == "ж":
#   gender = "Женский"
# print(f"Вы выбрали {gender} пол")

# print("Выберете расу персонажа ч-человек,\n э-эльф")
# race = str(input("Введите ч или э:\n"))
# if race == "ч" or race == "Ч":
#   race = "Человек"
# elif race == "э" or race == "Э":
#   race = "Эльф"
  
#   print(f"Вы выбрали рассу {race}")

# if race == "Человек":
#   scoreRole = 0  # галочка для выбора класса
#   print("Выберете класс:\n", "1-Воин", "2-Лучник", "3-Жрец", "4-Маг")
#   role = input("введите 1,2,3 или 4 для выбора класса:")
#   if role == "1":
#     role = "Воин\n"
#   elif role == "2":
#     role = "Лучник\n"
#   elif role == "3":
#     role = "Жрец\n"
#   elif role == "4":
#     role = "Маг\n"

# elif race == "Эльф":
#     print("Выберете класс:\n", "1-Воин\n", "2-Лучник\n", "3-Темный Колдун\n",
#           "4-Паладин\n")
#     role = input("введите 1,2,3 или 4 для выбора класса")
#     if role == "1":
#       role = "Воин"
#     elif role == "2":
#       role = "Лучник"
#     elif role == "3":
#       role = "Темный Колдун"
#     elif role == "4":
#       role = "Паладин"
# print(f"Вы выбрали класс:{role}")

# name = str(input("Введите имя вашего персонажа"))
# print("\nИнформация о персонаже:\n"
#         f"пол персонажа {gender}\n"
#         f"Раса персонажа {race}\n"
#         f"Класс:{role}\n"
#         f"Имя:{name}\n")

# myName = "Ilya"
# for i in range(0,5):
#    print(myName, i)

# start = int(input("Введите начальное значение: "))
# end = int(input("введите конечное значение: "))
# for i in range(start,end + 1):
#    print(i)

# myName = "Ilya"
# # for i in range(0,2 + 1):
# #     print(i)
# for i in myName:
#     print(i)
#     if i == "y":
#         break

# for i in range(0,29):
#       if i % 2 !=0:
#            print(i)

# a = 2
# b = 3
# if a + b == 5:
#     for i in range(0,10):
#         print((a+b)*i)

# x = int(input("введите число на проверку: "))
# for i in range(2,x+1):
#     print(f"делим число {x} на {i}")
#     print(f"остаток {x % i}")
#     if x % i == 0 and x !=i:
#         print("число сложное")
#         break
#     elif i == x:
#         print("число простое")
        
# for x in range(0,100):
#     if x % 2 == 0 and x % 7 == 0:
#         print(x)

# x = int(input("введите число для получения таблицы умножения: "))
# for i in range(2,10):
#     print(f"{x} * {i} = {x * i}")

# sum = 0
# for i in range(5,8):
#     sum = sum + i
#     print(sum)

# i = 0
# b = 10
# while i < 10 and b > 0:
#     print(i)
#     print(b)
#     i = i + 1
#     b = b - 3

# i = 0
# while i != 11 and i < 100:
#     print(i)
#     i = i + 23

# i = 0
# print("первый цикл")
# while True:
#     print(i)
#     i = i + 1
#     if i > 10:
#         i = 0
#         break
# print("второй цикл")   
# x = True
# while x == True:
#     print(i)
#     i = i + 1
#     if i > 15:
#         x = False

# myName = "Il'ya"
# print(len(myName))
# i = 0
# while i < len(myName):
#     print(i)
#     i+=1
        

# name = "Hello Word"
# for i in name:
#     print(i)

# name = "Hello Word"
# for i in range(1,11):
#     print(name)

# i = 1
# while i<=10:
#     print(i)
#     i=i+1
# i = 1
# while i<=10:
#     print(i)
#     i=i+1
#     break
# i = 1
# while i<=10:
#     if i != 5:
#        print(i)
#     i=i+1
#     continue

# i = 1
# while 1 == 1:
#    print("Бесконечный цикл")


# for x in range(2,10):
#     print(f" 2 * {x} = {2 * x}")

# принцип работы часов
# for i in range(1,10): # i = 1
#     for j in range(1,10): # j = 1
#         print(i , j)

# import time
# for h in range(0,24): # h = 0
#     for m in range(0,60): # m = 1
#         for s in range(0,60): # s = 1
#             print(f"ч:{h} м:{m} с:{s}")
#             time.sleep(1)

# import time
# h = 0
# while h < 24:
#     m = 0
#     while m < 60:
#         s = 0
#         while s < 60:
#             print(f"ч:{h} м:{m} с:{s}")
#             time.sleep(1)
#             s += 1
#         m += 1
#     h += 1

# dd = int(input("d"))
# mm = int(input("m"))
# yy = int(input("y"))
# if mm == 4 or mm == 6 or mm == 9 or mm == 11:
#     if dd >= 30:
#         mm+=1
#         dd=1
#         print(dd,mm,yy)
#     elif dd < 30:
#         dd+=1
#         print(dd,mm,yy)
# elif mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10:
#     if dd >= 31:
#         mm+=1
#         dd=1
#         print(dd,mm,yy)
#     elif dd < 31:
#         dd+=1
#         print(dd,mm,yy)
# elif mm == 12:
#     if dd >= 31:
#         mm=1
#         dd=1
#         yy+=1
#         print(dd,mm,yy)
#     elif dd < 31:
#         dd+=1
#         print(dd,mm,yy)
# elif mm == 2:
#     if yy % 4 == 0:
#         if dd >= 29:
#             mm=+1
#             dd=1
#             yy+=1
#             print(dd,mm,yy)
#     elif dd < 29:
#         dd+=1
#         print(dd,mm,yy)
#     else:
#         if dd >= 28:
#             mm=+1
#             dd=1
#             yy+=1
#             print(dd,mm,yy)
#         elif dd < 28:
#             dd+=1
#             print(dd,mm,yy)
        


# -------------------------------------------------------------------
# Использование циклов внутри циклов, возврат значений + условия.

# print("Регистрация персанажа")

# reg = 0
# while reg < 1:
#     reg_gender = 0
#     while reg_gender < 1:
#         gender = input("Выберете пол персанажа\n1-муж\n2-жен\n: ")
#         if gender == "1":
#             gender = "Мужской"
#             reg_gender+=1
#         elif gender == "2":
#             gender = "Женский"
#             reg_gender+=1
#         else:
#             print("Выберете из перечисленного")
#         if reg_gender == 1:
#             reg_race = 0 
#             while reg_race < 1:
#                 race = input("0 <-назад Выберете рассу персанажа\n1-Человек\n2-Эльф\n: ")
#                 if race == "1":
#                     race = "Человек"
#                     reg_race+=1
#                 elif race == "2":
#                     race = "Эльф"
#                     reg_race+=1
#                 elif race == "0":
#                     reg_gender = 0
#                     break
#                 else:
#                     print("Ошибка:Выберете из перечисленного")
#                 if reg_race == 1:
#                     reg_role = 0
#                     if race == "Человек":
#                         while reg_role == 0:
#                             role = input("0 <-назад Выберете рассу персанажа\n1-Воин\n2-Лучник\n: ")
#                             if role == "1":
#                                 reg_role == 1
#                     elif race == "Эльф":
#                         pass
                    
#     reg+=1


# МEТОДЫ

# myName = "Ilya"
# v = 90
# t = 1
# s = v*t

#                 0           1
# genderList = ["Мужской", "Женский"]
# print(genderList[0])
#             0 1 2 3  4  5  6  7  8  9
# numberList = [3,4,8,47,9,945,5,445,7,84]
# numberList.sort
# print(len(numberList))


# raceList = ["Человек", "Эльф"]
# print(raceList, "Создали список")
# raceList.append("Гном")
# print(raceList, "raceList.append(\"Гном\")")
# raceList.pop(1)
# print(raceList, "raceList.pop(1)")
# raceList.clear()
# print(raceList, "raceList.clear()")

# newList = []
# numberList = [3,4,8,47,9,945,5,445,7,84]
# print(numberList)
# for i in range(0,len(numberList)):
#     # numberList[i] = numberList[i]**2
#     if numberList[i] % 2 != 0:
#         newList.append(numberList[i])
# print(newList)

# listN = [
#          [1,2,3,4,5],
#          [6,7,8,9,10],
#          ]
# for i in range(0, len(listN)):
#     print(listN[i])
#     for j in range(0,len(listN[i])):
#         print(listN[i][j])


# genderList = ["Мужской", "Женский"] 
# raceList = ["Человек", "Эльф", "Гном", "Орк", "Тролль"]
# roleList = ["Воин", "Лучник", "Маг"]
# textGender = ""
# for i in range(0, len(genderList)): # повторять от 0 до колличества рас
#     textGender += f"{i} - {genderList[i]}\n" # в пустую строку каждый раз будет прописываться порядковый номер 
#     # расы и его значение к примеру вывод после 2х повторений будет выглядеть так:
#     # № - значение
#     # 0 - человек
#     # 1 - эльф  
#     # т.к.          № 0        № 1
#     # raceList = ["Человек", "Эльф", "Гном", "Орк", "Тролль"]
# reg = False # регестрация не завершена 
# while reg == False:
#     reg_gender = False
#     while reg_gender == False:
#     myGender = int(input(f"Выберете пол: \n{textGender}"))
#     if myGender >= len(genderList) or myGender < 0:
#             print("Ошибка: выбери из перечисленного")
#     else:
#         for i in range (0, len(genderList)):
#             if myGender == i:
#                 myGender = genderList[i]
#                 reg_gender = True
#                 print("Вы выбрали пол:",myGender)            
#                 break  
# textRace = ""
# for i in range(0, len(raceList)):
#     textRace += f"{i} - {raceList[i]}\n"
# # textRace += f"{len(raceList)} назад"
# reg_race = False
# while reg_race == False:
#     myRace = int(input(f"Выберете расу: \n{textRace}"))
#     if myRace > len(raceList) or myRace < 0:
#             print("Ошибка: выбери из перечисленного")
#     # elif myRace == len(raceList):
#     #             reg_race = False
#     #             break
#     else:
#         for i in range (0, len(raceList)):
#             if myRace == i:
#                 myRace = raceList[i]
#                 reg_race = True
#                 print("Вы выбрали расу:",myRace)            
#                 break

# genderList = ["Мужской", "Женский"]
# raceList = ["Человек", "Эльф", "Гном", "Орк","Тролль"]
# roleList = ["Воин","Лучник","Маг"]
# print(raceList[2])
# textRace = ""
# for i in range ( 0 , len(raceList)): 
#     textRace += f"{i} - {raceList[i]}\n"
# textRace += f"{len(raceList)} - назад\n"
# print("Регистрация персонажа")
# reg = False
# while reg == False: # цикл для регестрации
#     # все переменные которые имеют приставку reg отвечают за отметку
#     reg_gender = False
#     while reg_gender == False:
#         gender = input("Выберете пол персонажа\n1-муж\n2-жен\n: ")
#         if gender == "1":
#             gender = "Мужской"
#             reg_gender=True
#         elif gender == "2":
#             gender = "Женский"
#             reg_gender=True
#         else:
#             print("Ошибка: Выберете из перечис ленного")
#         if reg_gender == True:
#             reg_race = False # созали галочку - (нет)
#             while reg_race == False: # выполнять пока False
#                 # принимает только число
#                 print(12)
#                 myRace = int(input(f"Выберете расу:\n{textRace}"))
#                 if myRace > len(raceList) or myRace < 0:
#                     print("Ошибка: выбери из перечисленного")
#                 else:
#                     for i in range ( 0 , len(raceList)):
#                         if myRace == i:
#                             race = raceList[i]
#                             reg_race = True
#                             print("вы выбрали",race)
#                             break
#                 if myRace == len(raceList):
#                         reg_gender = False
#                         break
#     reg = True


# задача
# саши и маша собирают яблоки на компот т.к. саша сильнее маши он должен собрать 6 яблок а маша должна собрать 3 яблока
# для компота нужно 8 яблок, обязательно что бы маша и саша принесли 8 яблок, 9е могут оставить себе

# result = False # False - яблоки не собраны
# masha = 0 # кол-во собранных яблок
# sasha = 0 # кол-во собранных яблок

# while result == False: # собирать яблоки пока у маши и саши не будет 8 шт
#     sasha = int(input("Сколько яблок собрал саша? "))
#     if sasha <= 6: # если саша собрал мень чем 6 яблок он должен продолжить собирать
#         print(f"Саша должен собрать еще {6 - sasha} яблока")
#     else:
#         print("Саша не может унести яблоки и все потерял")
#         sasha = 0
#     masha = int(input("Сколько яблок собрала маша? "))
#     if masha <= 3: # если маша собрал мень чем 3 яблок он должен продолжить собирать
#         print(f"Маша должена собрать еще {3 - masha} яблока")
#     else:
#         print("Маша не может унести яблоки и все потеряла")
#         masha = 0
#     if masha + sasha >=8:
#         result = True
#         print(f"Компот готов и осталось {(sasha+masha)-8} яблок")

# задача список гостей

# guestList = []
# textguest = ""
# for i in range(0, len(guestList)): 
#     textguest += f"{i} - {guestList[i]}\n" 
# reg = False
# while reg == False:
#     reg_guest = False
#     while reg_guest == False:
#         guest = input("Регистрация гостей\n1-Добавить гостя\n2-Удалить гостя\n3-Просмотр гостей: ")
#         if guest == "1":
#             guest = input("Ведите имя гостя: ")
#             guestList.append(guest)
#         elif guest == "2":
#             guest = input("Ведите имя гостя: ")
#             guestList.remove(guest)
#         elif guest == "3":
#             print(guestList)
#         else:
#             print("Ошибка: Выберете из перечисленного")
#     reg = True

#                 0         1
# productList = ["Каша" , "Вода"]
# print(productList[0])
# infoProduct = {
#     "nameProduct" : "Каша",
#     "price" : 120,
#     "sale" : 0.2,
# }
# print(f"{infoProduct['price']}\n{infoProduct['sale']}")

# myName = input("введите свое имя: ")
# myAge = int(input("Сколько вам лет? "))
# infoPerson = {
#     "namePerson" : myName,
#     "agePerson" : myAge,
#     "hobbyPerson" : ["Sport", "Programming"]
# }
# print(infoPerson)

# for key in infoPerson:
#     print(f"{key} - {infoPerson[key]}")

# productList = [
#     {
#         "nameProduct" : "Хлеб",
#         "price" : 55,
#         "count" : 37,
#         "category" : "Хлеб"
#     },
#     {
#         "nameProduct" : "Молоко",
#         "price" : 101,
#         "count" : 20,
#         "category" : "Молочка"
#     },
#     {
#         "nameProduct" : "Яйцо",
#         "price" : 151,
#         "count" : 80,
#         "category" : "Яйцо"
#     },
#     {
#         "nameProduct" : "Майонез",
#         "price" : 190,
#         "count" : 700,
#         "category" : "Молочка"
#     },
#     {
#         "nameProduct" : "Йогурт",
#         "price" : 900,
#         "count" : 400,
#         "category" : "Молочка"
#     },
#     {
#         "nameProduct" : "Кефир",
#         "price" : 99,
#         "count" : 6,
#         "category" : "Молочка"
#     },
# ]
# for i in range(0, len(productList)):
#     if productList[i]["category"] == "Молочка":
#         productList[i]["price"] = productList[i]["price"] * 2
#         print(f"Название товара - {productList[i]['nameProduct']}")
#         print(f"Цена - {productList[i]['price']}")
#         print(f"Кол-во - {productList[i]['count']}")
#         print("-----------------------------")

# guestList = []

# while True:
#     nameGuest = input("Введите имя гостя: ")
#     ageGuest = int(input("Введите возраст гостя: "))
#     # выше созданные переменные будут бобавлятся в объект infoGuest и вставлятся в соответствующие ключи
#     # infoGuest - хранит данные гостя
#     infoGuest = {
#         "nameGuest" : nameGuest,
#         "ageGuest" : ageGuest,
#     }
#     guestList.append(infoGuest)
#     if len(guestList) > 3:
#         break

# for i in range(0, len(guestList)):
#     print(f"Имя гостя - {guestList[i]['nameGuest']}")
#     print(f"Возраст гостя - {guestList[i]['ageGuest']}")
#     print("==================")

# ФУКЦИИ

# def f1(a,b):
#     c = a + b
#     print(c)
# f1(5,2)

# def f1(a):
#    c = a - 50
#    print(c)
#    return c
# asd = f1(100)
# print(asd)

# myInfo = {

# }

# print(myInfo)
#           # myInfo 
# def regName(massiv, newName):
# #   myInfo["myName"] = newName
#     massiv["myName"] = newName
#     return massiv
# def regGender(massiv):
#     x = int(input("1-муж\n2-жен\n"))
#     if x == 1:
#         massiv["myGender"] = "Муж"
#     elif x == 2:
#         massiv["myGender"] = "Жен"
#         return massiv
# def globalReg(massiv):
#     # massiv = myInfo
#     regName(massiv,input("Ваше имя: "))
#     regGender(massiv)
#     return massiv
   

# newInfo = globalReg(myInfo)
# print(newInfo)



# mult = 0
# def f1(number):
#     x = int(input("введите число: "))
#     y = int(input("введите число: "))
#     z = int(input("введите число: "))
#     return number
# def f2(number):
#     s = int(input("0 - сумма, 1 - произведение: "))
#     if s == 0:
#         number = sum
#     elif s == 1:
#         number = mult
#         return number

# f1({})
# print(f1)


# 5 задание из контрольной


# [
#    { "userLogin" : admin,
#     "userPassword" : admin,
#     "userName" : Ilya,
#     "userFirstName" : Vybornov,
# }
# ] пример хранения данных пользователей 

usersList = [
    { 
    "userLogin" : "admin",
    "userPassword" : "admin",
    "userName" : "Ilya",
    "userFirstName" : "Vybornov",
},
] # Список пользователей

while True:
    x = int(input("Введите:\n1-регистрация нового пользователя\n2-Вход в личный кабинет "))
    if x == 1: # цикл для регистрации нового пользователя
        print("------Регистрация------")
        while True:
            regUser = { 
                "userLogin" : "",
                "userPassword" : "",
                "userName" : "",
                "userFirstName" : "",
            }
            while True:
                regLogin = input("Введите логин: ") 
                if len(usersList) > 0:
                    for i in range(0, len(usersList)):
                        if regLogin != usersList[i]["userLogin"]:
                            regUser["userLogin"] = regLogin
                        else:
                            print("Данный логин уже занят\nвведите другой ")
                            regUser["userLogin"] = ""
                            break
                else:
                    regUser["userLogin"] = regLogin
                if len (regUser["userLogin"]) > 0:
                    break
            regUser["userPassword"] = input("Введите пароль нового пользователя: ")
            regUser["userName"] = input("Введите имя нового пользователя: ")
            regUser["userFirstName"] = input("Введите фамилию нового пользователя: ")
            print("Регистрация завершина")
            check = int(input("1 - подтвердить\n2 - ввести данные снова"))
            if check == 1:
                usersList.append(regUser)
                break
            elif check == 2:
                print("------Регистрация------")
    elif x == 2:
        print("-- Вход в ЛК")
        inLogin = input("Введите логин: ")
        inPassword = input("Введите пароль: ")
        for i in range(0, len(usersList)):
            if inLogin == usersList[i]["userLogin"] and inPassword == usersList[i]["userPassword"]:
                print("Вход выполнен")
                while True:
                    infoUser = int(input("1 - Посмотреть информацию\n2 - Редактировать информацию\n3 - Выход "))
                    if infoUser == 1:
                        print(f'Имя : {usersList[i]["userName"]}\n',
                              f'Фамилия : {usersList[i]["userFirstName"]}\n',
                              f'Логин : {usersList[i]["userLogin"]}\n'
                              f'Пароль : {usersList[i]["userPassword"]}\n')
                    elif infoUser == 2:
                        print("Редактирование данных")
                        upDate = int(input("1 - Имя\n2 - Фамилия\n3 - Пароль "))
                        if upDate == 1:
                            print(f'Ваше имя {usersList[i]["userName"]}')
                            usersList[i]["userName"] = input("новое имя")
                        elif upDate == 2:
                            print(f'Ваше фамилия {usersList[i]["userFirstName"]}')
                            usersList[i]["userFirstName"] = input("новая фамилия")
                        elif upDate == 3:
                            print(f'Ваш пароль {usersList[i]["userPassword"]}')
                            usersList[i]["userPassword"] = input("новый пароль")
                    elif infoUser == 3:
                        break
                break
            elif len(usersList) - 1 == i:
                print("Неверный логин или пароль")
