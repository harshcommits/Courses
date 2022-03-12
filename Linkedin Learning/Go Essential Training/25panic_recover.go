package main

import (
	"fmt"
	//"os"
)

func safeValue(vals []int, index int) int {
	defer func() {
		if err := recover(); err != nil {
			fmt.Printf("Error: %s\n", err)
		}
	}()

	return vals[index]
}

func main() {
	/*
		vals := []int{1, 2, 3}

			//following will cause panic
			v := vals[10]
			fmt.Println(v)

		file, err := os.Open("no-such-file")
		if err != nil {
			panic(err) //points to line number with the issue
		}

		defer file.Close()
		fmt.Println("file opened")
	*/

	v := safeValue([]int{1, 2, 3}, 10)
	fmt.Println(v) //prints 0; since there is no value set for the handler
}
