// standard function definition

const X = function() {
    // "this" here is the caller of X
};

// same thing in arrow function

const Y = () => {
    // "this" here is not the caller of Y

    // It's the same this found in Y's scope
}

this.id = 'exports';
console.log(this);

// testing this with functions

const testObj = {
    func1: function() {
        console.log('func1', this);
    },

    func2: () => {
        console.log('func2', this);
    },
};

testObj.func1(); // outputs all of testObj function
testObj.func2(); // outputs only the value of this when first defined

// reducing lines in arrow functions

// Method 1
const square1 = (a) => {
    return a*a;
};

// Method 2
const square2 = (a) => a * a;

// Method 3
const square3 = a => a * a;

// example of above usecase
console.log([1, 2, 3, 4].map(a => a * a));