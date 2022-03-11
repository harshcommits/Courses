package main

import (
	"fmt"
)

func main() {
	/* elaborate way of declaring variables
	var x int
	var y int

	x = 1
	y = 2
	*/

	//alternate way
	x, y := 1, 2

	fmt.Printf("x=%v, type of %T\n", x, x)
	fmt.Printf("y=%v, type of %T\n", y, y)

	mean := float32((x + y) / 2)
	fmt.Printf("Result: %v, type of %T", mean, mean)
}
