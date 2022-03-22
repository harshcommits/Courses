// => - arrow function
/*
normal function declaration

let studentList = function(students) {
    console.log(students);
}
*/

//same function as above written as arrow function below:

let studentList = (students) => console.log(students)
studentList(["Student 1", "Student 2", "Student 3"]);

//another example with arrow functions

let list = ["apple", "banana", "cherry"];
list.map((item) => console.log(item));