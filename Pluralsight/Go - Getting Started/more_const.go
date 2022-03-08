package main

import (
	"fmt"
)

const (
	first = iota + 6 //iota represents successive integer constants; 0 in this case
	//second = 2 << iota //bitwise operator, prints 4; need more reading
	second // prints 7; need more reading
)

func main() {
	fmt.Println(first, second)
}
