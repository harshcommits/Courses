function add(x, y) {
    console.log(x + y);
}

add(1, 3);

function haveFun(
    //default values for parameters
    activityName = "Hiking", 
    time = 3
) {
    console.log(`Today I will go ${activityName} for ${time} hours`);
}

haveFun("biking", 2.5);
haveFun("cooking");