const theOneFunc = duration => {
    console.log("Hello after " + duration + " seconds");
};

setTimeout(theOneFunc, 4*1000, 4);
setTimeout(theOneFunc, 8*1000, 8);
 