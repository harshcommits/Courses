package main

import (
	"fmt"
)

func main() {
	nums := []int{16, 8, 88, 23, 21}

	max := nums[0]

	/*
		initialize first value in array, and compare other values with it to get max value
	*/

	for _, value := range nums[1:] {
		if value > max {
			max = value
		}
	}

	fmt.Println(max)
}
