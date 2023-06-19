# import random as rnd
 
# def random_arr(n):
#     return [rnd.randint(0, 10) for i in range(n)]
# l1 = random_arr(10)
# l2 = random_arr(10)
 
# # Задача 1
# l3 = l1 + l2
 
# # Задача 2
# l4 = list(set(l3))
 
# # Задача 3
# l5 = [i for i in l3 if i in l1 and i in l2]
 
# # Задача 4
# l6 = [i for i in l1 if i not in l2] + [i for i in l2 if i not in l1]
 
# # Задача 5
# a = sorted(l1)
# b = sorted(l2)
# l7 = [a[0], a[-1], b[0], b[-1]]

# print("Первый список",l1)
# print("Первый список",l2)
# print("Общий список", l3)
# print("Список уникальных чисел",l4)
# print("Список с общими чисел", l5)
# print("Списоодинаковых чисел без повторения", l6)
# print("Мин и макс значения списков", l7)