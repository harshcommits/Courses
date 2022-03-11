package main

import (
	"fmt"
)

func main() {

	for i := 0; i < 3; i++ {
		fmt.Println(i)
	}

	fmt.Println("------------") //exit loop at a particular condition
	for i := 0; i < 3; i++ {
		if i > 1 {
			break
		}
		fmt.Println(i)
	}

	fmt.Println("------------") //skip loop for a particular condition
	for i := 0; i < 3; i++ {
		if i < 1 {
			continue
		}
		fmt.Println(i)
	}

	fmt.Println("------------") //while loop implementation
	a := 0
	for a < 3 {
		fmt.Println(a)
		a++
	}

	fmt.Println("------------") //infinte loop breaking out at a particular condition
	b := 0
	for {
		if b > 2 {
			break
		}
		fmt.Println(b)
		b++
	}

}
