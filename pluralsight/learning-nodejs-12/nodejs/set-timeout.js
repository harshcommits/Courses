setTimeout(
    () => {
        console.log("Hello after 4 seconds");
    },
    4 * 1000
);

// set timeout with function

const func = () => {
    console.log("2 second timeout from function");
};

setTimeout(func, 2 * 1000)

// set timeout function with value

const rocks = who => {
    console.log(who + " rocks");
};

setTimeout(rocks, 3 * 1000, "Pluralsight"); // Pluralsight is the value for argument who