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