// script doesn't timeout until the loop below is finished

setTimeout(
    () => console.log("Hell after 0.5 seconds, MAYBE!"),
    500,
);

for (let i = 0; i < 1e10; i++) {
    // Block node synchronously
}