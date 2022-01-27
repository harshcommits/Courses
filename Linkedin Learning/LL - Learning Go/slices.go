package main

import (
	"fmt"
	"sort"
)

func main() {

	var colors = []string{"Red", "Green", "Blue"}
	fmt.Println(colors)
	colors = append(colors, "Purple")
	fmt.Println(colors)

	colors = append(colors[1:len(colors)]) //displays slice from index 1 to len(colors), i.e. final value
	fmt.Println(colors)

	//using make; need reading
	numbers := make([]int, 5) //we can remove the last '5' and append values
	numbers[0] = 23
	numbers[1] = 43
	numbers[2] = 45
	numbers[3] = 84
	numbers[4] = 12
	fmt.Println(numbers)

	numbers = append(numbers, 234)
	fmt.Println(numbers)

	sort.Ints(numbers) //need more reading on sort package
	fmt.Println(numbers)

}
