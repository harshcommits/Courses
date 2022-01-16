package main

import (
	"fmt"
)

func main() {

	colors := []string{"Red", "Green", "Blue"}
	fmt.Println(colors)

	for i := 0; i < len(colors); i++ {
		fmt.Println(colors[i])
	}

	fmt.Println("Second Loop")
	//better loop using range
	for i := range colors {
		fmt.Println(colors[i])
	}

	//
	fmt.Println("third loop")

	for index, color := range colors {
		fmt.Println(index, color)
	}

	//using for as a while loop
	value := 1
	for value < 10 {
		fmt.Println("Value: ", value)
		value++
	}

	sum := 1
	for sum < 1000 {
		sum += sum
		fmt.Println("Sum: ", sum)
		if sum > 20 {
			goto theEnd
		}
	}

theEnd: //goto labels; the location where goto statement jumps to
	fmt.Println("Value exceeded 20, hence jumping out of loop")

}
