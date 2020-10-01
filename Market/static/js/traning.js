function sum(a, b) {
    return a + b
}

function mnozh(a) {
    return a * 4
}

function deler(a, b, c) {
    return (a + b + c)/3
}

function sev() {
    return 7
}

function fiver(a) {
    return a%5
}

console.log(fiver(5))

function priv(a) {
    return a.replace(' ', 'privet')
}

console.log(priv('fdsfdsf fdfdsfsdf'))

function dictor(a, b) {
    delete a['a']
    a['c'] = b
    return a
}

console.log(dictor({'a': 8, 'b': 6}, 7))

function nu(a){
   if (a<=34) {
    console.log('Lyubov')
}
else {
    console.log('My_name')
}
}

nu('enter a number', 43)

function summer() {
    a = Number(prompt('enter number'))
    b = Number(prompt('enter number'))
    if (a + b === 5) {
        return (a + b) / 2
    }
    else {
        return (a + b)
    }
}

console.log(summer())

console.log(parseInt(ten, 10))