function* director() {
    yield "three";
    yield "two";
    yield "one";
    yield "Action!";

}

let countdown = director();

console.log(countdown.next().value);  //prints three
console.log(countdown.next().value);  //prints two
console.log(countdown.next().value);  //prints one
console.log(countdown.next().value);  //prints "Action!"; another command would print undefined