const vacation = {
    destination: "Chile",
    travelers: 2,
    activity: "skiiing",
    cost: "so much!"
};

function marketing({ destination, activity }) {
    return `Come to ${destination} and do ${activity}`;
};

console.log(marketing(vacation));

//const sandwich = {

//object sandwich after destructuring
const { title, price } = {
    title: "Reuben",
    price: 7,
    description: "A classic",
    ingredients: [
        "bread",
        "corned beef",
        "dressing",
        "sauerkraut",
        "cheese"
    ]
};

//console.log(sandwich.title)
console.log(title) //getting output from destructured object
//console.log(sandwich.price)
console.log(price)