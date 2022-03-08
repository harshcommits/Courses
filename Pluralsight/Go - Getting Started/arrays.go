package main

import (
	"fmt"
)

func main() {
	var arr [3]int
	arr[0] = 1
	arr[1] = 2
	fmt.Println(arr[0])

	arr2 := [3]int{1, 3, 4}
	fmt.Println(arr2)
}
