class Person {
    constructor(name) {
        this.name = name;
    }
    greet() {
        console.log(`Hello, ${this.name}`);
    }
}

class Student extends Person {
    constructor(name, level) {
        super(name);
        this.level = level;
    }
    greet() {
        console.log(`Hello ${this.name} from ${this.level}`);
    }
}

const a1 = new Person("Harsh");
const a2 = new Student("Mira", "10th Grade");
const a3 = new Student("Ira", "11th Grade");

a3.greet = () => console.log("I am special!");

a1.greet();
a2.greet();
a3.greet();
