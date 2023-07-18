# Задание 1

# x = input("Укажите имя: ")
# y = input("Укажите фамилию: ")
# z = input("Укажите возраст: ")
# t = input("Укажите год рождения: ")

# print(f"Имя - {x}\nФамилия - {y}\nВозраст - {z}\nГод - {t}\n")

# Задание 2 

# pyty = int(input("Выбери путь: 0 - прямо, 1 - на право, 2 - на лево: "))
# x = True
# while x == True: 
#     if pyty == 0:
#         q1 = input(f"Зимой и летом одним цветом: ")
#         if q1 == "ёлка" or q1 == "елка":
#             print("Ответ верный проходи")
#         else:
#             print("Конец")
#             break
#     if pyty == 1:
#         q2 = input(f"Висит груша нельзя скушать: ")
#         if q2 == "лампочка":
#             print("Ответ верный проходи")
#         else:
#             print("Конец")
#             break
#     if pyty == 2:
#         q3 = input("Что выше леса поднимается да без огня горит: ")
#         if q3 == "солнце":
#             print("Ответ верный проходи")
#         else:
#             print("Конец")
#             break

# Задание 3 


# from random import randint
# n1 = randint(0,10)
# # n2 = randint(40,120)
# # x = int(input("Выбери игру: 0 - от 0 до 10, 1 - от 40 до 120: "))
# k = int(input("Введите число от 0 до 10: "))
# # y = int(input("Введите число от 40 до 120: "))
# while k !=n1:
#         if k < n1:
#             print("Число больше")
            
#         elif k > n1:
#             print("Число меньше")
#             k = int(input("Повторите попытку: "))
#         else:
#             print("Вы угадали")
# print(n1)
# print(k)




#Задание 4 

# weekList = [
#     {
#         "weekday" : "Понедельник",
#         "lesson1" : "Математика",
#         "lesson2" : "Физика",
#         "lesson3" : "Информатика",
#         "lesson4" : "Физкультура",
#         "vyhodnoy" : "",

#     },
#     {
#         "weekday" : "Вторник",
#         "lesson1" : "Математика",
#         "lesson2" : "Физика",
#         "lesson3" : "Информатика",
#         "lesson4" : "",
#         "vyhodnoy" : "",
#     },
#     {
#         "weekday" : "Среда",
#         "lesson1" : "Литература",
#         "lesson2" : "Физика",
#         "lesson3" : "Информатика",
#         "lesson4" : "Математика",
#         "vyhodnoy" : "",
#     },
#     {
#         "weekday" : "Четверг",
#         "lesson1" : "Литература",
#         "lesson2" : "Физика",
#         "lesson3" : "Информатика",
#         "lesson4" : "Черчение",
#         "vyhodnoy" : "",
#     },
#     {
#         "weekday" : "Пятница",
#         "lesson1" : "Литература",
#         "lesson2" : "Физика",
#         "lesson3" : "Ин. язык",
#         "lesson4" : "Математика",
#         "vyhodnoy" : "",
#     },
#     {
#         "weekday" : "Суббота",
#         "lesson1" : "",
#         "lesson2" : "",
#         "lesson3" : "",
#         "lesson4" : "",
#         "vyhodnoy" : "Выходной",
#     },
#     {
#         "weekday" : "Воскресение",
#         "lesson1" : "",
#         "lesson2" : "",
#         "lesson3" : "",
#         "lesson4" : "",
#         "vyhodnoy" : "Выходной",
#     },    
# ]
# for i in range(0,len(weekList)):
#     print(f"День недели - {weekList[i]['weekday']}")
#     print(f"1 - {weekList[i]['lesson1']}")
#     print(f"2 - {weekList[i]['lesson2']}")
#     print(f"3 - {weekList[i]['lesson3']}")
#     print(f"4 - {weekList[i]['lesson4']}")
#     print(f"{weekList[i]['vyhodnoy']}")



    
