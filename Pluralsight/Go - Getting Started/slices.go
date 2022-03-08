package main

import (
	"fmt"
)

func main() {
	arr := [3]int{1, 2, 3}
	fmt.Println(arr)

	slice := arr[:]
	fmt.Println(slice)

	arr[1] = 43
	slice[2] = 21

	fmt.Println("Array: ", arr)
	fmt.Println("Slice: ", slice)

	fmt.Println(slice[1:2])
}
