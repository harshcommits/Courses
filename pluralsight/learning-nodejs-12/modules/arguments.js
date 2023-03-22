function dynamicArgsFunctions() {
    console.log(arguments); // will print all the arguments passed
}

dynamicArgsFunctions(1, 2, 3, 4);

// the following line will print 5 arguments, even though there's nothing passed. Run the code to get an idea
// they are; function(exports, module, require, __filename, __dirname)

console.log(arguments);