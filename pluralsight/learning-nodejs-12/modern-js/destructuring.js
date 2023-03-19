// const PI = Math.PI;
// const E = Math.E;
// const SQRT2 = Math.SQRT2;

// the below statement works the same as above 3
const { PI, E, SQRT2 } = Math;

//with require
// const { readFile } = require('fs');

const circle = {
    label: 'circleX',
    radius: 2,
};

// here, the function circleArea just uses the radius attribute from the circle object via de-structuring
const circleArea = ({ radius }, { precision = 2 } = {}) => // precision (no. of decimal places ) dynamically declared
    (PI * radius * radius).toFixed(precision);

console.log(
    circleArea(circle)
);

// modifying precision on the fly
console.log(
    circleArea(circle, { precision: 5 })
);

// assign multiple values by de-structuring
const [first, second,, fourth] = [10, 20, 39, 40];
console.log(fourth); // prints 40, since no variable for 39 defined