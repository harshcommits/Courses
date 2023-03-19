{
    // block scope
    {
        // Nested block scope
    }
}

if (true) {
    // block scope
}

for (var i = 1; i <= 10; i++) {
    // block scope
}

console.log(i); // preints 11, even outside for loop; hence suggested to use let/const instead

function sum(a, b) {
    // function scope
    var result = a + b;
}

sum(4, 3);