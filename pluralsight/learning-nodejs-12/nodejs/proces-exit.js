setTimeout(() => process.exit(), 3000);

process.on('exit', () => {
    console.log("Process shall exit now!");
});

console.log("Hello!");