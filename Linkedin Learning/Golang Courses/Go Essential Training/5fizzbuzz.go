package main

import (
	"fmt"
)

func main() {
	fmt.Println("Enter the number for testing")

	a := 20

	for i := 1; i < a; i++ {
		if i%3 == 0 && i%5 != 0 {
			fmt.Printf("fizz\n")
		} else if i%5 == 0 && i%3 != 0 {
			fmt.Printf("buzz\n")
		} else if i%3 == 0 && i%5 == 0 {
			fmt.Printf("fizz buzz\n")
		} else {
			fmt.Printf("%v\n", i)
		}
	}

}
