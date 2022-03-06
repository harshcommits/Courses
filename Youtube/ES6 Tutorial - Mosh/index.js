function runhello() {
    for (let i = 0; i < 5; i++) {
        console.log(i);
    }

    console.log("Outside the loop", i); //prints 5 when var used; fails when we use let
}

runhello();