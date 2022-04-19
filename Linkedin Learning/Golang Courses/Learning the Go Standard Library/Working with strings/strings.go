package main

import (
	"fmt"
)

func main() {

	s := "Testing"

	//print length
	fmt.Println(len(s))

	//iterate over each letter
	for _, ch := range s {
		fmt.Print(string(ch), ",")
	}
	fmt.Print("\n")

	//using operators < > == !=
	fmt.Println("dog" < "cat") //false; since c before d
	fmt.Println("dog" < "horse")

}
