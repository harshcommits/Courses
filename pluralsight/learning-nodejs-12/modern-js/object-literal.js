const mystery = "answer"

const obj = {
    p1: 10,
    p2: 20,
    f1() {},
    f2: () => {},
    [mystery]: 42, // dynamic property; need more reading on this
};

// statement below generates undefined; as mystery is key which assigns value to answer
console.log(obj.mystery);

// another way of looking at below function, this prints 42:
console.log(obj[mystery]);

// this one prints value successfully
console.log(obj.answer);