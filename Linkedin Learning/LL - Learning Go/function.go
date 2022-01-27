package main

import (
	"fmt"
)

func main() {

	fmt.Println("Different functions!!")
	doSomething()

	sum := addValues(5, 8)
	fmt.Println("2. The sum is: ", sum)

	multiSum, count := addAllValues(23, 34, 45)
	fmt.Println("The sum of values: ", multiSum)
	fmt.Println("The number of values: ", count)

}

func doSomething() {
	fmt.Println("1. Doing something")
}

func addValues(value1 int, value2 int) int {

	return value1 + value2

}

//function with arbitrary no. of arguments
func addAllValues(values ...int) (int, int) {

	total := 0
	for _, v := range values {
		total += v
	}
	return total, len(values)

}
