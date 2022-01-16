const path = require("path");
//const util = require("util");
const { log } = require("util"); //another way to write line 2
const { getHeapStatistics } = require("v8");

const diruploads = path.join(__dirname, "www", "files", "uploads");
console.log(diruploads);

//util.log(path.basename(__filename));
//util.log("^ The name of current file");

log(getHeapStatistics()); //can do this instead of util.log