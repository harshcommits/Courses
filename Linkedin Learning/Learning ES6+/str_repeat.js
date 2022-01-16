let yell = "woo!";

let party = yell.repeat(20);
console.log(party);

let cat = {
    meow(times) {
        console.log("meow".repeat(times))
    },
    purr(times) {
        console.log("prr".repeat(times))
    }
}

cat.meow(4);
cat.purr(3);