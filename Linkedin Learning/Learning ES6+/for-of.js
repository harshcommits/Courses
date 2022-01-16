for (let letter of "Javascript") {
    console.log(letter);    
}

let topics = new Map();
topics.set("HTML", "/topics/html");
topics.set("CSS", "/topics/css");
topics.set("Javascript", "/topics/javascript");

for (let topic of topics.values()) { //use topics.entries to get key-value pairs in maps
    console.log(topic)
}
