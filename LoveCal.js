let yourName = prompt('Enter your name ').toUpperCase()
let herName = prompt('Enter her name ').toUpperCase()
let result = Math.floor(Math.random() * 100)
console.log(` Between ${yourName} and ${herName}  is ${result}%`)

const getPercent = ()=>{
    if (result < 10 && result > 90){
        console.log('Your love is like coke and mentos ')
    } else if (result > 40 && result <=50){
        console.log('Cool ! True Love ')
    }else 
    {
        console.log(`Your percent is ${result} %`)
    }
} 

getPercent()