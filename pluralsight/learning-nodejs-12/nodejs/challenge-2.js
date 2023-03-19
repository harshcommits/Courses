let counter = 0;

const intervalID = setInterval(() => {
    console.log("Hello World!");
    counter += 1

    if (counter == 5) {
        console.log("Done");
        clearInterval(intervalID)
    }
}, 1000);