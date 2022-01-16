const id = Symbol(); //acts as unique identifier for variables; available in ES6+ syntax

const courseInfo = {
    title: "Javascript",
    topic: ["strings", "arrays", "objects"],
    id: "course-info"
};

courseInfo[id] = 4123; 
console.log(courseInfo)