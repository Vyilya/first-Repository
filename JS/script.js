// console.log("Hello")
// let one = 1
// const pi = 3.14
// console.log(one)
// one = 2

// let int = 1;
// let str = "1";
// let bool = true || false;
// let massiv = [1,2,3,4,5,6];
// let obj = {
//     "name" : "name",
//     "age" : 22,
// }
// class Auto{
//     constructor(name,age){
//         this.name = name;
//         this.age = age;
//     }
//     changeName(){
//         console.log(this.name)
//     }
// }
// class AutoV2 extends Auto{
//     constructor(name,age){
//         this.name = name;
//         this.age = age;
//     }
// }

// function sum(a,b){
//     return a + b
// }

// let sum2 = (a,b) => {
//     return a + b
// }

// console.log(sum(2,3))

// let x = prompt("Введите ваше имя"); // строка
// let y = +prompt("Введите только число"); // число +
// console.log(x,y)

// let i = 0;

// while(i < 10){
//     i++;
//     console.log(i)
// }
// for(let i = 0; i < 10; i++){
//     console.log(i)
// }

// let z = 2;
// let k = 2;

// if(z < k){
//     console.log("z < k")
// }
// else if(k < z){
//     console.log("k < z")
// }
// else if(k == z){
//     console.log("k = z")
// }
// else{
//     console.log("ошибка")
// }

// let hi = "hihihiihihsidihi"
// console.log(` ${hi}`)

// pyton  js
// or     ||
// and     &&


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


// УРОК 2
// let plus = document.getElementById("plus");
let plus = document.querySelector("#plus");
let minus = document.querySelector("#minus");
let out = document.querySelector("#out");
console.log(plus);
console.log(minus);
console.log(out);

// out.innerHTML = 123;

let title = document.querySelector("title");
title.innerHTML = "урок " + 2 

let i = 0;
function plusOut(){
    i++;
    out.innerHTML = i;
}

function minusOut(){
    i--;
    out.innerHTML = i;
}
// plusOut()
// plusOut()
// minusOut()

plus.addEventListener("click", plusOut)
minus.addEventListener("click", minusOut)

let number1 = document.querySelector("#number1")
let number2 = document.querySelector("#number2")

let calcPlus = document.querySelector("#calcPlus")
let calcMinus = document.querySelector("#calcMinus")
let calcMul = document.querySelector("#calcMul")
let calcDiv = document.querySelector("#calcDiv")

let otvet = document.querySelector("#otvet")


function fPlus(){

    otvet.innerHTML = Number(number1.value) + Number(number2.value)
    calcPlus.style.backgroundColor = "coral";
}

function fMinus(){
    otvet.innerHTML = Number(number1.value) - Number(number2.value)
    calcMinus.classList.add = ("coral");
}

function fMul(){
    otvet.innerHTML = Number(number1.value) * Number(number2.value)
}

function fDiv(){
    otvet.innerHTML = Number(number1.value) / Number(number2.value)
}

calcDiv.addEventListener("click" , fDiv)
calcMul.addEventListener("click" , fMul)
calcMinus.addEventListener("click" , fMinus)
calcPlus.addEventListener("click" , fPlus)

// let body = document.body;

// body.style.backgroundColor = "blue";