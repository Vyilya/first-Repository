// Задание 1
// let x = +prompt ("введите число: ");
// let y = +prompt ("введите число: ");
// let s = +prompt ("введите число: ");
// console.log(x + y + s);
// console.log(x * y * s);

// Задание 2
// let x = +prompt("введите зп за месяц: ");
// let y = +prompt("введите сумму месяцного платежа по кредиту: ");
// let z = +prompt("введите задолженность за комунальные услуги: ");
// console.log(x-y-z,"остаток");

// Задание 3
// let x = +prompt("введите число: ");
// let y = +prompt("введите число: ");
// let z = +prompt("введите число: ");
// let s = +prompt("0 - сумма, 1 - произведение");

// if (s == 0){
//     console.log(x + y + z);
// }

// else if (s == 1){
//     console.log(x * y * z);
// }
// else{
//     console.log("введите корректное значение");
// }

// Задание 4
// let x = +prompt("введите число: ");
// let y = +prompt("введите число: ");
// let z = +prompt("введите число: ");

// let s = +prompt("0 - max, 1 - min, 2 - среднефрифметическое ");

// if (s == 0){
//     console.log(max(x,y,z));
// }
// else if (s == 1){
//     console.log(min(x,y,z));
// }

// else if (s == 2){
//     console.log((x + y + z) / 2);
// }
// else{
//     console.log("введите корректное значение");
// }

// Задание 5
// let x = +prompt("введите сколько метров: ");
// let s = +prompt("0 - мили, 1 - дюймы, 2 - ярды ");
// if (s == 0){
//     console.log(x * 0.000621);
// }

// else if (s == 1){
//     console.log(x * 39.37);
// }
// else if (s == 2){
//     console.log(x * 1.093613);
// }
// else {
//     console.log("введите корректное значение");
// }

// Задание 6
// let x = +prompt("укажите ваш возраст: ");
// if (x <= 2){
//     console.log("ребенок");
// }

// else if (x <= 18){
//     console.log("подросток");
// }

// else if (x <= 60){
//     console.log("взрослый");
// }
// else if (x >= 61){
//     console.log("пенсионер");
// }
// else{
//     console.log("введите корректное значение");
// }

// Задание 7
// let x = +prompt("введите число от 0 до 9: ");
// if (x == 0){
//     console.log(")")
// }
// else if (x == 1){
//     console.log("!");
// }
// else if (x == 2){
//     console.log("@");
// }
// else if (x == 3){
//     console.log("#");
// }
// else if (x == 4){
//     console.log("$");
// }
// else if (x == 5){
//     console.log("%");
// }
// else if (x == 6){
//     console.log("^");
// }
// else if (x == 7){
//     console.log("&");
// }
// else if (x == 8){
//     console.log("*");
// }
// else if (x == 9){
//     console.log("(");
// }
// else{
//     console.log("введите корректное значение");
// }

// Задание 8
// let x = +prompt("введите трехзначное число: ");
// if (Math.floor (x / 100) == x / 10 % 10){
//     console.log('Да');
// }
// else if (Math.floor(x / 100) == x % 10){
//     console.log('Да');
// }
// else if (Math.floor(x / 10) % 10 == x % 10){
//     console.log('Да');
// }
// else{
//     console.log('Нет');
// }

// Задание 9
// let x = +prompt("Введите год: ")
// if (x % 4 == 0){
//     console.log("Високосный")
// }

// else if (x % 100 == 0){
//     console.log("Обычный")
// }
// else if (x % 400 == 0){
//     console.log("Обычный");
// }
// else{
//     console.log("Обычный");
// }

// Задание 10
// let x = +prompt("Введите пятизначное число для проверки на палиндром: ")
// let  a = Math.floor (x /  10000);
// let  b = x % Math.floor (10000 / 1000);
// let  c = x % 10;
// let d = Math.floor (x % 100 / 10);
// if (a == c && b == d){
//     console.log("палиндром");
// }
// else {
//     console.log("не палиндром")
// }

// Задание 11
// let x = +prompt("введите количество USD: ")
// let s = +prompt("в какую валюту вы хотите перевести 0 - EUR, 1 - UAN, 2 - AZN ")
// if (s == 0){
//     console.log(x * 0.93145)
// }
// else if (s == 1){
//     console.log(x * 7.06)
// }

// else if (s == 2){
//     console.log(x * 1.7)
// }
// else{
//     console.log("введите корректное значение")
// }

// Задание 12
// let x = +prompt("введите сумму покупки: ")
// if (x >= 200 && x <= 300){
//     a = x - x * 0.03
//     console.log("сумма со скидкой: ", a)
// }

// else if (x > 300 && x <= 500){
//     b = x - x * 0.05
//     console.log("сумма со скидкой: ", b)
// }

// else if (x > 500){
//     c = x - x * 0.07
//     console.log("сумма со скидкой: ", c)
// }
// else{
//     console.log("введите корректное значение")
// }

// Задание 13
// let x = +prompt("введите длину окружности: ")
// let y = +prompt("введите периметр квадрата: ")
// if (x * 2 * (0.5) < 2 * y){
//     console.log("Поместится") 
// }
// else{
//     console.log("Не поместится")
// }

// Задание 13
// console.log("Зимой и летом одним цветом:\n", "1-ёлка\n", "2-палка\n", "3-тёрка\n");
// let answer = +prompt("Введите 1,2,3 :\n");
//  score = 0
// if (answer == "1"){
//     console.log("Вы выбрали верно, получи 2 бала");
//     score = score + 2
// }

// else{
//     console.log("Ответ не верный")
// }

// console.log("Висит груша нельзя скушать:\n", "1-лампочка\n", "2-груша\n", "3-тарелка\n")
// let answer = +prompt("Введите 1,2,3 :\n")
// # if answer == "1": 
// #     print(f"Вы выбрали верно, получи 2 бала")
// #     score = score + 2
// # else:
// #     print("Ответ не верный")
// # print("Без рук, без ног, А ворота открывает:\n", "1-ветер\n", "2-ключ\n", "3-елка\n")
// # answer = (input("Введите 1,2,3 :\n"))
// # if answer == "1": 
// #     print(f"Вы выбрали верно, получи 2 бала")
// #     score = score + 2
// # else:
// #     print("Ответ не верный")
// # print("У Вас очков: " , score)


// Задание 15

// let d = +prompt("Введите дату (ДД): ")
// let m = +prompt("Введите месяц (ММ): ")
// let y = +prompt("Введите год (ГГГГ): ")
// if (m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10){
//     if (d > 31){
//         console.log("Данные введены не верно!")
//     } 
//     else if (d == 31){
//         m = m + 1;
//         d = 1;
//         console.log(`${d}.${m}.${y}`)
//     }
//     else{
//         d = d + 1;
//         console.log(`${d}.${m}.${y}`)
//     } 
// }
    
// else if (m == 4 || m == 6 || m == 9 || m == 11){
//     if (d > 30){
//         console.log("Данные введены не верно!")
//     } 
//     else if (d == 30){
//         m = m + 1;
//         d = 1;
//         console.log(`${d}.${m}.${y}`)
//     }
//     else{
//         d = d + 1;
//         console.log(`${d}.${m}.${y}`)
//     }
// }
    
// else if (m == 2){
//     if (y % 4 == 0){
//         if (d > 29){
//             console.log("Данные введены не верно!")
//         }
//         else if (d == 29){
//             m = m + 1;
//             d = 1;
//             console.log(`${d}.${m}.${y}`)
//         }
//         else{
//             d = d + 1;
//             console.log(`${d}.${m}.${y}`)
//         }  
//     }
        
//     else{
//         if (d > 28){
//             console.log("Данные введены не верно!")
//         }
//         else if (d == 28){
//             m = m + 1;
//             d = 1;
//             console.log(`${d}.${m}.${y}`)
//         }
//         else{
//             d = d + 1;
//             console.log(`${d}.${m}.${y}`)
//         }
//     }
        
// }
    
// else if (m == 12){
//     if (d > 31){
//         console.log("Данные введены не верно!")
//     }
//     else if (d == 31){
//         m = 1;
//         d = 1;
//         y = y + 1;
//         console.log(`${d}.${m}.${y}`)
//     }
        
//     else{
//         d = d + 1;
//         console.log(`${d}${m}${y}`)
//     }
// }

// else{
//     console.log("Данные введены не верно!")
// }

// Задание 16

// let start = +prompt("Введите начало диапазона: ");
// let end = +prompt("Введите конец диапазона: ");
// for (i = start; i <= end; i++){
//     if (i % 7 == 0){
//         console.log(i)
//     }
// }

// Задание 17

// let start = +prompt("Введите начало диапазона: ");
// let end = +prompt("Введите конец диапазона: ");
// console.log("Все числа диапазона");
// for (i = start; i <= end; i++){
//     console.log(i)
// }          
// console.log("Все числа кратные 7");
// for (i = start; i <= end; i++){
//     if (i % 7 == 0){
//         console.log(i)
//     }       
// }
// console.log("Количество чисел кратных 5");
// let n = 1;
// for (i = start; i <= end; i++){
//     if (i % 5 == 0){
//         console.log(n);
//         n +=1
//     }  
// }
// console.log("Все числа диапазона в обратном порядке")
// for (i = start - 1; i <= end; i++){
//     console.log(end);
//     end = end - 1
// }    
    
// Задание 18

// let start = +prompt("Введите начало диапазона: ");
// let end = +prompt("Введите конец диапазона: ");
// while (start < end){
//     start++;
//     if (start % 3 == 0 && start % 5 != 0){
//         console.log("Fizz")
//     }
//     else if (start % 5 == 0 && start % 3 != 0){
//         console.log("Buzz")
//     }
//     else if (start % 3 == 0 && start % 5 == 0){
//         console.log("Fizz Buzz")
//     }
//     else if (start % 3 != 0 && start % 5 != 0){
//         console.log(start)
//     }
// }
    
// Задание 18

// console.log("Регистрация персонажа");
// let reg = 0;
// let gender = "";
// let role = "";
// let race = "";
// while (reg == 0){
//     let reg_gender = 0;
//     while (reg_gender == 0){
//         gender = +prompt("Выберите пол персонажа\n1 - М\n2 - Ж\n>  ");
//         if (gender == 1){
//             gender = "Мужской";
//             reg_gender=1
//         } 
//         else if (gender == 2){
//             gender = "Женский";
//             reg_gender=1;
//         }
//         else{
//             console.log("Ошибка: Выберите из перечисленного")
//         }
//         if (reg_gender == 1){
//             let reg_race = 0;
//             while (reg_race == 0){
//                 race = +prompt("Выберите рассу персонажа\n1 - Человек\n2 - Эльф\n3 - Гном\n4 - Назад\n5 - К началу\n>  ");
//                 if (race == 1){
//                     race = "Человек";
//                     reg_race = 1
//                 }  
//                 else if (race == 2){
//                     race = "Эльф";
//                     reg_race = 1
//                 }
//                 else if (race == 3){
//                     race = "Гном";
//                     reg_race = 1
//                 }
                    
//                 else if (race == 4){
//                     reg_gender = 0;
//                     break
//                 }
//                 else if (race == 5){
//                     reg_gender = 0
//                     break
//                 }
//                 else{
//                     console.log("Ошибка: Выберите из перечисленного")
//                 }
//                 if (reg_race == 1){
//                     reg_role = 0;
//                     if (race == "Человек"){
//                         while (reg_role == 0){
//                             role = +prompt("Выберите роль пресонажа\n1 - Мечник\n2 - Лучник\n3 - Кавалерист\n4 - Назад\n5 - К началу\n>  ");
//                             if (role == 1){
//                                 role = "Мечник";
//                                 reg_role = 1
//                             }
//                             else if (role == 2){
//                                 role = "Лучник";
//                                 reg_role = 1
//                             }  
//                             else if (role == 3){
//                                 role = "Кавалерист";
//                                 reg_role = 1
//                             }
//                             else if (role == 4){
//                                 reg_race = 0
//                                 break
//                             }
//                             else if (role == 5){
//                                 reg_gender = 0;
//                                 break
//                             }
//                             else{
//                                 console.log("Ошибка: Выберите из перечисленного")
//                             }   
//                         }
//                     }
//                     else if (race == "Эльф"){
//                         while (reg_role == 0){
//                             role = +prompt("Выберите роль пресонажа\n1 - Мечник\n2 - Лучник\n3 - Кавалерист\n4 - Назад\n5 - К началу\n>  ");
//                             if (role == 1){
//                                 role = "Мечник";
//                                 reg_role = 1
//                             }
//                             else if (role == 2){
//                                 role = "Лучник";
//                                 reg_role = 1
//                             } 
//                             else if (role == 3){
//                                 role = "Кавалерист";
//                                 reg_role = 1
//                             }
                                
//                             else if (role == 4){
//                                 reg_race = 0;
//                                 break
//                             }
                                
//                             else if (role == 5){
//                                 reg_gender = 0;
//                                 break
//                             }
//                             else{
//                                 console.log("Ошибка: Выберите из перечисленного")
//                             }
//                         }    
//                     }       
//                     else if (race == "Гном"){
//                         while (reg_role == 0){
//                             role = +prompt("Выберите роль персонажа\n1 - Мечник\n2 - Копейщик\n3 - Арбалетчик\n4 - Назад\n5 - К началу\n>  ");
//                             if (role == 1){
//                                 role = "Мечник";
//                                 reg_role = 1
//                             }
//                             else if (role == 2){
//                                 role = "Копейщик";
//                                 reg_role = 1
//                             }
//                             else if (role == 3){
//                                 role = "Арбалетчик";
//                                 reg_role = 1
//                             }
//                             else if (role == 4){
//                                 reg_race = 0;
//                                 break
//                             }
//                             else if (role == 5){
//                                 reg_gender = 0
//                                 break
//                             }
//                             else{
//                                 console.log("Ошибка: Выберите из перечисленного")
//                             }
                                
//                         }
                            
//                     }
                        
//                 }
                    
//             }
                
//         }
            
//     }
//     let myName = prompt("Введите имя: ");
//     let reg_name = 0;
//     while (reg_name == 0){
//         let info = +prompt("Вывести информацию о персонаже?\n1 - Да\n2 - Нет\n>  ");
//         if (info == 1){
//             console.log("Информация о персонаже: ");
//             console.log("Имя: ",myName);
//             console.log("Пол: ",gender);
//             console.log("Раса: ",race);
//             console.log("Роль: ",role);
//             break
//         }
//         else if (info == 2){
//             console.log("Персонаж не создан!");
//             break
//         }
//         else{
//             console.log("Ошибка: Выберите из перечисленного")
//         }       
//     }
//     reg+=1
// }

// Задание 19

// let numberList = [5, 16, 7, 24, 3];
// let numberList1 = [11, 3, 52, 5, 13];

// console.log("Все элементы списков");
// let numberList2 = [...numberList, ...numberList1];
// console.log(numberList2);
// console.log("------------------------------------");
// console.log("Все элементы списков без повторений");
// console.log(new Set(numberList2));
// console.log("------------------------------------");

// console.log("Общие элементы списков");
// let numberList3 = [];
// for (i of numberList){
//     for (j of numberList1){
//         if (i == j){
//             numberList3.push(i);
//             break
//         }
//     } 
// }
// console.log(numberList3);
// console.log("------------------------------------");

// console.log("Уникальные элементы списков");
// let numberList4 = [];
// for (i of numberList1){
//     if (!(i in numberList)){
//         numberList4.push(i);
//     }  
// }
// for (i of numberList){
//     if (!(i in numberList1)){
//         numberList4.push(i);
//     }
// }
// console.log(numberList4);
// console.log("------------------------------------");

// console.log("Максимальные и минимальные элементы обоих списков");
// let numberList5 = [Math.max(...numberList), Math.min(...numberList), Math.max(...numberList1), Math.min(...numberList1)];
// console.log(numberList5);
// console.log("------------------------------------");

// Задание 19

// console.log("Регистрация гостей");
// let guestList = [];
// let blackList = ["Костя", "Федя", "Петя"];
// let vybor = "";
// while (true){
//     if (guestList.length <= 5){
//         vybor = +prompt("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n> ");
//     } 
//     else{
//         vybor = +prompt("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n4 - Закончить приглашение?\n> ");
//     }
        
//     if (vybor == 1){
//         if (guestList.length < 10){
//             let guest_name = prompt("Введите имя: ");
//             if (!(guest_name in blackList)){
//                 guestList.push(guest_name);
//             }
//             else{
//                 console.log("Данный гость в черном списке!");
//             }
//         }
//         else{
//             console.log("Список гостей заполнен!");
//         }
//     }
        
//     else if (vybor == 2){
//         if (guestList.length > 0){
//             guest_name = prompt("Введите имя гостя: ");
//             guestList = guestList.filter(item => item !== guest_name);
//         }

//         else{
//             console.log("Список пуст!");
//         }
//     }
//     else if (vybor == 3){
//         if (guestList.length > 0){
//             textGuest = "";
//             console.log("Список гостей: ");
//             for (i = 0; i <= guestList.length; i++){
//                 textGuest += `${i + 1} - ${guestList[i]}\n`
//             }  
//             console.log(textGuest)
//         }
//         else{
//             console.log("Список пуст!")
//         }
//     }  
//     else if (vybor == 4){
//         if (5 < guestList.length && guestList.length < 10){
//             break
//         }   
//     }
// }
    
// Задание 20

// console.log("Регистрация гостей");
// guestList = [];
// let vybor = "";
// while (true){
//     if (guestList.length <= 5){
//         vybor = +prompt("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n> ");
//     } 
//     else{
//         vybor = +prompt("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n4 - Закончить приглашение?\n> ");
//     }
//     if (vybor == 1){
//         if (guestList.length < 10){
//             let guestName = prompt("Введите имя гостя: ");
//             let guestAge = +prompt("Введите возраст гостя: ");
//             let infoGuest = {
//                 "guestName" : guestName,
//                 "guestAge" : guestAge,
//             }
//             if (guestAge <= 10){
//                 console.log("Нельзя приглашать гостей младше 10 лет включительно!\n")
//             }
                
//             else{
//                 guestList.push(infoGuest);
//                 console.log("Гость добавлен\n")
//             }
//         }
//         else{
//             console.log("Список гостей заполнен!")
//         }  
//     }
//     else if (vybor == 2){
//         if (guestList.length > 0){
//             guestName = prompt("Введите имя гостя: ");
//             guestAge = +prompt("Введите возраст гостя: ");
//             guestList = guestList.filter(item => item !== guest_name);
//             ("Гость удален\n")
//         }
//         else{
//             ("Список пуст!")
//         }
//     }
//     else if (vybor == 3){
//         if (guestList.length > 0){
//             let textGuest = "";
//             let textGuest1 = "";
//             console.log("Список гостей: ");
//             let n = 0;
//             for (i = 0; i <= guestList.length; i++){
//                  textGuest += `${i + 1} - ${guestList[i].guestName}\n`
//                 if (guestList[i].guestAge >= 18){
//                     n = n + 1;
//                     textGuest += `${n} - Имя: ${guestList[i].guestName}\n    Возраст: ${guestList[i].guestAge}\n`
//                 }
//             }
//             console.log("Взрослые:\n");
//             console.log(textGuest);
//             for (i = 0; i <= guestList.length; i++){
//                 if (guestList[i].guestAge < 18){
//                     n = n + 1;
//                     textGuest1 += `${n} - Имя: ${guestList[i].guestName}\n    Возраст: ${guestList[i].guestAge}\n` 
//                 }
//             }
//             console.log("Дети:\n");
//             console.log(textGuest1);
//         } 
//         else{
//             console.log("Список пуст!")
//         }
//     }
//     else if (vybor == 4){
//         if (5 < guestList.length < 10){
//             break
//         }   
//     }     
// }

// Задание 21

// let myName = prompt("Введите ваше имя: ")
// let mySurname = prompt("Введите вашу фамилию: ")
// let myAge = prompt("Введите ваш возраст: ")
// myByear = prompt("Введите ваш год рождения: ")
// console.log(`Карточка пользователя:\nИмя:  ${myName}\nФамилия:  ${mySurname}\nВозраст:  ${myAge}\nГод рождения:  ${myByear}`)

// Задание 22

// let vybor = +prompt("Выберите загадку(1, 2 или 3): ");
// if (vybor == 1){
//     console.log("Кто его раздевает, тот слезы проливает. Что это?")
//     let otvet = prompt("Введите ответ: ");
//     if (otvet == "Лук"){
//         console.log("Верно!")
//     }
//     else{
//         console.log("Не верно!")
//     }
// }
// else if (vybor == 2){
//     console.log("Зимой и летом одним цветом. Что это?");
//     otvet = prompt("Введите ответ: ");
//     if (otvet == "Елка"){
//         console.log("Верно!")
//     }
//     else{
//         console.log("Не верно!")
//     }
// }
// else if (vybor == 3){
//     console.log("Два конца, два кольца, посередине гвоздик. Что это?");
//     otvet = prompt("Введите ответ: ");
//     if (otvet == "Ножницы");
//         console.log("Верно!")
//     else{
//         console.log("Не верно!")
//     }
// }  
// else{
//     console.log("Ошибка выбора!")
// }
    

// Задание 23

// let uch = Math.floor(Math.random() * 11);
// let popytka = 1;
// let vybnum = +prompt("Введите число от 0 до 10\n>");
// popytka += 1;
// while (vybnum != uch){
//     vybnum = +prompt("Повторите попытку\n>");
//     if (uch < vybnum){
//         console.log("Ваше число больше!");
//         popytka += 1
//     }
        
//     else if (uch > vybnum){
//         console.log("Ваше число меньше!");
//         popytka += 1
//     }
//     else{
//         console.log(`Вы угадали, это число ${uch}!\nВы использовали ${popytka} попыток `);
//         popytka += 1;
//         break
//     }
        
// }
    

// Задание 24 

// let weekList = [
//     {
//         "weekday" : "Понедельник",
//         "lesson1" : "Математика",
//         "lesson2" : "Физика",
//         "lesson3" : "Информатика",
//         "lesson4" : "Физкультура",
//         "vyhodnoy" : "",

//     },
//     {
//         "weekday" : "Вторник",
//         "lesson1" : "Математика",
//         "lesson2" : "Физика",
//         "lesson3" : "Информатика",
//         "lesson4" : "",
//         "vyhodnoy" : "",
//     },
//     {
//         "weekday" : "Среда",
//         "lesson1" : "Литература",
//         "lesson2" : "Физика",
//         "lesson3" : "",
//         "lesson4" : "",
//         "vyhodnoy" : "",
//     },
//     {
//         "weekday" : "Четверг",
//         "lesson1" : "Литература",
//         "lesson2" : "Физика",
//         "lesson3" : "Информатика",
//         "lesson4" : "Черчение",
//         "vyhodnoy" : "",
//     },
//     {
//         "weekday" : "Пятница",
//         "lesson1" : "Литература",
//         "lesson2" : "Физика",
//         "lesson3" : "Ин. язык",
//         "lesson4" : "",
//         "vyhodnoy" : "",
//     },
//     {
//         "weekday" : "Суббота",
//         "lesson1" : "",
//         "lesson2" : "",
//         "lesson3" : "",
//         "lesson4" : "",
//         "vyhodnoy" : "Выходной",
//     },
//     {
//         "weekday" : "Воскресение",
//         "lesson1" : "",
//         "lesson2" : "",
//         "lesson3" : "",
//         "lesson4" : "",
//         "vyhodnoy" : "Выходной",
//     },    
// ]
// for (i = 0; i <= weekList.length; i++){
//     if (weekList[i]["weekday"] == "Понедельник" || weekList[i]["weekday"] == "Четверг"){
//         console.log(`День недели - ${weekList[i]['weekday']}`);
//         console.log(`1 - ${weekList[i]['lesson1']}  8.00 - 10.15`);
//         console.log(`2 - ${weekList[i]['lesson2']}  10.20 - 11.25`);
//         console.log(`3 - ${weekList[i]['lesson3']}  11.30 - 12.25`);
//         console.log(`4 - ${weekList[i]['lesson4']}  13.00 - 14.00\n`);
//     } 
//     else if (weekList[i]["weekday"] == "Вторник" || weekList[i]["weekday"] == "Пятница"){
//         console.log(`День недели - ${weekList[i]['weekday']}`);
//         console.log(`1 - ${weekList[i]['lesson1']}  8.00 - 10.15`);
//         console.log(`2 - ${weekList[i]['lesson2']}  10.20 - 11.25`);
//         console.log(`3 - ${weekList[i]['lesson3']}  11.30 - 12.25\n`);
//     }
        
//     else if (weekList[i]["weekday"] == "Среда"){
//         console.log(`День недели - ${weekList[i]['weekday']}`);
//         console.log(`1 - ${weekList[i]['lesson1']}  8.00 - 10.15`);
//         console.log(`2 - ${weekList[i]['lesson2']}  10.20 - 11.25\n`);
//     }
        
//     else{
//         console.log(`День недели - ${weekList[i]['weekday']}`);
//         console.log(`${weekList[i]['vyhodnoy']}\n`)
//     }
// }

// Задание 25
    
// let regList = [];
// while (true){
//     let vybor = +prompt("Выберите действие\n1 - Регистрация\n2 - Вход\n");
//     if (vybor == 1){
//         console.log("Регистрация");
//         while (true){
//             let inforeg = {
//                 "namePerson" : "",
//                 "surnamePerson" : "",
//                 "loginPerson" : "",
//                 "passwordPerson" : "",
//                 }
//                 while (true){
//                     let myLogin = prompt("Введите логин: ");
//                     if (regList.length > 0){
//                         for (i = 0; i <= regList.length; i++){
//                             if (myLogin != regList[i]["loginPerson"]){
//                                 inforeg["loginPerson"] = myLogin
//                             }
//                             else if (regList.length - 1 == i){
//                                 console.log("Логин занят, введите другой!");
//                                 inforeg["loginPerson"] = "";
//                                 break
//                             }   
//                         }
//                     }
//                     else{
//                         inforeg["loginPerson"] = myLogin;
//                     }
//                     if (inforeg["loginPerson"].length > 0){
//                         break
//                     }   
//                 }
//                 inforeg["passwordPerson"] = prompt("Введите пароль: ");
//                 inforeg["namePerson"] = prompt("Введите имя: ");
//                 inforeg["surnamePerson"] = prompt("Введите фамилию: ");
                
//                 let p = +prompt("Подтвердить регистрацию?\n1 - Да\n2 - Отмена\n");
//                 if (p == 1){
//                     ("Вы зарегестрированы!");
//                     regList.push(inforeg);
//                     break  
//                 }
//                 else if (p == 2){
//                     console.log("Регистрация")
//                 }   
//         } 
//     }
//     else if (vybor == 2){
//         console.log("Вход");
//         myLogin = prompt("Введите логин: ");
//         let myPassword = prompt("Введите пароль: ");
//         for (i = 0; i <= regList.length; i++){
//             if (myLogin == regList[i]["loginPerson"] && myPassword == regList[i]["passwordPerson"]){
//                 console.log("Вход совершен успешно!");
//                 while (true){
//                     let vybor1 = +prompt("Выберите действие\n1 - Просмотр информации\n2 - Выйти\n3 - Редактировать данные\n");
//                     if (vybor1 == 1){
//                         console.log(`Имя - ${regList[i]['namePerson']}`);
//                         console.log(`Фамилия - ${regList[i]['surnamePerson']}`);
//                         (`Логин - ${regList[i]['loginPerson']}`)
//                     }
                            
//                     else if (vybor1 == 2){
//                         break
//                     }
//                     else if (vybor1 == 3){
//                         console.log("Редактирование данных");
//                         let reduct = +prompt("1 - Имя\n2 - Фамилия\n3 - Пароль\n");
//                         if (reduct == 1){
//                             console.log(`Ваше имя ${regList[i]['namePerson']}`);
//                             regList[i]["namePerson"] = prompt("Введите новое имя: ")
//                         }
//                         else if (reduct == 2){
//                             console.log(`Ваша фамилия ${regList[i]['surnamePerson']}`);
//                             regList[i]["surnamePerson"] = prompt("Введите новую фамилию: ")
//                         }
                            
//                         else if (reduct == 3){
//                             console.log(`Ваш пароль ${regList[i]['passwordPerson']}`);
//                             regList[i]["passwordPerson"] = prompt("Введите новый пароль: ")
//                         }   
//                     }  
//                 }
//                 break
//             }
//             else if (userList.length - 1 == i){
//                 console.log("Неверный логин или пароль")
//             }   
//         }    
//     } 
// }
    
// Задание 26

// let numberList = [1,2,3,4,5,6,7,8,9,22,11,10,6,5,22];

// function delNumber(massiv){
//     console.log("вошел", massiv, "кол-во",massiv.length);
//     for (i = 0; i <= massiv.length; i++){
//         if (i == massiv.length){
//             return massiv
//         } 
            
//         else if (massiv[i] % 2 == 0){
//             massiv.pop(i);
//             console.log("вышел", massiv);
//             delNumber(massiv)
//         }    
//     } 
// }
// delNumber(numberList)

// Задание 27

// let clientList = [
//     {
//         "myName" : "Александр",
//         "status" : "Оплачен"
//     },
//     {
//         "myName" : "Василий",
//         "status" : "Не оплачен"
//     },
//     {
//         "myName" : "Петр",
//         "status" : "Оплачен"
//     },
//     {
//         "myName" : "Арсений",
//         "status" : "Не оплачен"
//     },
//     {
//         "myName" : "Вадим",
//         "status" : "Оплачен"
//     },
//     {
//         "myName" : "Сергей",
//         "status" : "Не оплачен"
//     },
// ];

// function neopl(massiv){
//     console.log("Список");
//     console.log("Количество: ", massiv.length);
//     for (i = 0; i <= massiv.length; i++){
//         console.log(`Имя: ${clientList[i]["myName"]} | Статус: ${clientList[i]["status"]}`)
//     }
//     for (i = 0; i <= massiv.length; i++){
//         if (i == massiv.length){
//             return massiv
//         }
//         else if (clientList[i]["status"] == "Не оплачен"){
//             massiv.pop(i);
//             console.log("Список обновлен");
//             console.log("Количество: ", massiv.length);
//             for (i = 0; i <= massiv.length; i++){
//                 console.log(`Имя: ${clientList[i]['myName']} | Статус: ${clientList[i]['status']}`)
//             }  
//             console.log("---------------------------------");
//             neopl(massiv)
//         }   
//     }   
// } 
// neopl(clientList)