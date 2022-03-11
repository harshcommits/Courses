package main

import (
	"fmt"
)

func main() {
	x := 10

	if x > 5 {
		fmt.Println("X is big")
	}

	if x > 100 {
		fmt.Println("x is very big")
	} else { // else needs to be in same line as if closing brace
		fmt.Println("x is not that big")
	}
}
