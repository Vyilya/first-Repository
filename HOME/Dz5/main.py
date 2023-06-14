genderList = ["Мужской", "Женский"]
raceList = ["Человек", "Эльф", "Гном", "Орк","Тролль"]
roleList = ["Воин","Лучник","Маг"]
print(raceList[2])
textRace = ""
for i in range ( 0 , len(raceList)): 
    textRace += f"{i} - {raceList[i]}\n"
textRace += f"{len(raceList)} - назад\n"
print("Регистрация персонажа")
reg = False
while reg == False: # цикл для регестрации
    # все переменные которые имеют приставку reg отвечают за отметку
    reg_gender = False
    while reg_gender == False:
        gender = input("Выберете пол персонажа\n1-муж\n2-жен\n: ")
        if gender == "1":
            gender = "Мужской"
            reg_gender=True
        elif gender == "2":
            gender = "Женский"
            reg_gender=True
        else:
            print("Ошибка: Выберете из перечис ленного")
        if reg_gender == True:
            reg_race = False # созали галочку - (нет)
            while reg_race == False: # выполнять пока False
                # принимает только число
                print(12)
                myRace = int(input(f"Выберете расу:\n{textRace}"))
                if myRace > len(raceList) or myRace < 0:
                    print("Ошибка: выбери из перечисленного")
                else:
                    for i in range ( 0 , len(raceList)):
                        if myRace == i:
                            race = raceList[i]
                            reg_race = True
                            print("вы выбрали",race)
                            break
                if myRace == len(raceList):
                        reg_gender = False
                        break
    reg = True