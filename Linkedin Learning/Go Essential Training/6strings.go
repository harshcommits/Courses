package main

import (
	"fmt"
)

func main() {
	book := "The colour of magic" //strings are immutable
	fmt.Println(book)

	fmt.Println(len(book))

	fmt.Printf("book[0] = %v (type %T)\n", book[0], book[0]) //prints book[0] = 84 (type uint8)

	//multi-line string
	poem := `The road
	goes one
	way or the other
	`

	fmt.Println(poem)
}
