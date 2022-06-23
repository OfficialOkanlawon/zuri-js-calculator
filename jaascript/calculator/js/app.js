// // Calculator task


let num1 = prompt('enter the first number')
let operation = prompt('enter arithemetic operation')
let num2 = prompt('enter the second number')


let value1 = parseInt(num1)
let value2 = parseInt(num2)
if (isNaN(num1) || isNaN(num2)){
    alert('Wrong input, digits only')
} 
else{
let answer = eval(`${value1}${operation}${value2}`)
alert(`${value1} ${operation} ${value2} \n${answer}`)
}