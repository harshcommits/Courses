package main

import (
	"fmt"
)

func main() {

	var colors [3]string
	colors[0] = "Red" //not using := since array type is already declared in prev. line by []
	colors[1] = "Green"
	colors[2] = "Blue"
	fmt.Println(colors)
	fmt.Println(colors[0])

	var numbers = [5]int{1, 2, 3, 4, 5}
	fmt.Println(numbers)

	fmt.Println("Number of colors: ", len(colors))
	fmt.Println("Number of numbers: ", len(numbers))

	//arrays are not re-sizable

}
