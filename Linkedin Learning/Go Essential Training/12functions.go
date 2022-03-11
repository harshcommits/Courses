package main

import (
	"fmt"
)

func add(a int, b int) int {
	return a + b
}

func divmod(a int, b int) (int, int) {
	return a / b, a % b
}

func main() {
	value := add(1, 2)
	fmt.Println(value)

	div, mod := divmod(7, 2)
	fmt.Printf("div=%d, mod=%d", div, mod)
}
