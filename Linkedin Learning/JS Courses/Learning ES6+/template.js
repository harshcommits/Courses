//function without template string
function print(firstName) {
    console.log("Prompt message for ", firstName)
}

print("Harsh")

//fucntion with template string
function print_template(myName) {
    console.log(`Template string output for ${myName}`);
}

print_template("Harsh Jha")

function template_spaces(param1, param2) {
    let shipping = 10.44
    console.log(`Hi ${param1}! Checking spaces:
        Total: ${param2}
        Shipping: ${shipping}
        Grand Total: ${param2 + shipping}
    `);
}

template_spaces("Harsh", 100)