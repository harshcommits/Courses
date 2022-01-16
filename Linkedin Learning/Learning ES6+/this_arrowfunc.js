let person = {
    first: "Angie",
    hobbies: ["sew", "run", "sleep"],
    printHobbies: function () {
        //let _this = this; //workaround to avoid line 6 if arrow function not used
        //this.hobbies.forEach(function (hobby) {
        this.hobbies.forEach((hobby) => { //alternative to line 6, without using line 5 as workaround
              let string = `${this.first} likes to ${hobby}`; //this.first returns undefined unless arrow function used
//            let string = `${_this.first} likes to ${hobby}`; //here it returns value after adding line 5
            console.log(string);
        });
    }
};

person.printHobbies();