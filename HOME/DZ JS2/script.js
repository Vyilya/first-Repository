let a = document.querySelector('#a');
let b = document.querySelector('#b');
let c = document.querySelector('#c');

let answerD = document.querySelector('#answerD');
let answerx1 = document.querySelector('#answer1');
let answerx2 = document.querySelector('#answer2');

let resh = document.querySelector('#resh');

function D(){
   answerD.innerHTML = Number(b.value)**2 - 4*Number(a.value)*Number(c.value)
}

function x1(){
   answerx1.innerHTML = (Number(-b.value) + Math.sqrt(answerD.innerHTML))/2*Number(a.value)
}

function x2(){
   answerx2.innerHTML = (Number(-b.value) - Math.sqrt(answerD.innerHTML))/2*Number(a.value)
}

resh.addEventListener("click", D);
resh.addEventListener("click", x1);
resh.addEventListener("click", x2);

let body = document.body;