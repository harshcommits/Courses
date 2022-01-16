class Vehicle {
    constructor(description, wheels) {
        this.description = description;
        this.wheels = wheels;
    }

    describeYourself() {
        console.log(
            `I am a ${this.description} with ${this.wheels} wheels!`
        );
    }
}

let skiivan = new Vehicle("Cool Ski Van", 4);

console.log(skiivan)
skiivan.describeYourself(skiivan)

//inheritance

class semiTruck extends Vehicle {
    constructor() {
        super("semi truck", 18)
    }
}

let grocerySemi = new semiTruck();
grocerySemi.describeYourself();