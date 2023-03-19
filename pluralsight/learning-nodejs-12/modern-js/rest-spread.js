const [first, ...restOfItems] = [10, 20, 30, 40];
console.log(restOfItems); // prints separate array of values other than 10


const data = {
    temp1: '001',
    temp2: '002',
    firstName: 'John',
    lastName: 'Doe',
};

const { temp1, temp2, ...person } = data;

const newArray = [...restOfItems]; // an array created from items other than 10
console.log(newArray);

const newObject = {
    ...person,
};