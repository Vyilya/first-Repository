# print("Список гостей")
# guestsList = [] # список гостей
# reg = False
# # цикл для регистрации
# while reg == False:
#     # если гостей меньше 5 то предлагать завершить регистрацию нельзя
#     if len(guestsList) < 5:
#         choice = int(input("1-добавить гостя\n2-Удалить гостя\n3-просмотр гостей"))
#     else:
#         choice = int(input("1-добавить гостя\n2-Удалить гостя\n3-просмотр гостей\n4- закончить вести список гостей"))
#     # если пользователь выберает 1, то идет проверка на количество гостей
#     # добавить гостя можно только если гостей не больше 10
#     if choice == 1:
#         if len(guestsList) < 10:
#             nameGuest = str(input("введите имя гостя: "))
#             guestsList.append(nameGuest)
#         else:
#             print("Список переполнен: кол-во гостей не может превышать более 10")
#     # Если пользователь выбрал 2, то он может удалить гостя, только если есть хотя бы один гость
#     elif choice == 2:
#         if len(guestsList) > 0:
#             textGuest = ""
#             # Цикл просмотра гостей  
#             for i in range(0,len(guestsList)):
#                 textGuest += f"{i} - {guestsList[i]}"
#             # цикл для проверки гостей т.к мы можем удалить только гостя который есть в списке 
#             print(textGuest)
#             nameGuest = str(input("введите имя гостя: "))
#             for i in range(0,len(guestsList)):
#                 if nameGuest == guestsList[i]:
#                     guestsList.remove(nameGuest)
#                     break
#         else:
#             print("вы не можете удалить гостей, список пуст")
#     elif choice == 3:
#         if len(guestsList) > 0:
#             textGuest = ""
#             # Цикл просмотра гостей  
#             for i in range(0,len(guestsList)):
#                 textGuest += f"{i} - {guestsList[i]}"
#             # цикл для проверки гостей т.к мы можем удалить только гостя который есть в списке 
#             print(textGuest)
#         else:
#             print("список гостей пуст")
#     elif choice == 4:
#         if len(guestsList) > 5 or len(guestsList) < 10:
#             break