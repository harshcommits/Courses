const daytime = {
    breakfast: "oatmeal",
    lunch: "peanut butter and jelly"
};

const nighttime = "mac and cheese";

const backpackingMeals = {
    ...daytime, //using spread(...) operator
    nighttime
};

console.log(backpackingMeals);