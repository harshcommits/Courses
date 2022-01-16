package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {

	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Value 1: ")
	input1, _ := reader.ReadString('\n')
	num1, err := strconv.ParseFloat(strings.TrimSpace(input1), 64)
	if err != nil {
		panic("The value must be a number")
	}

	fmt.Println("Value 2: ")
	input2, _ := reader.ReadString('\n')
	num2, err := strconv.ParseFloat(strings.TrimSpace(input2), 64)
	if err != nil {
		panic("The value must be a number")
	}

	result := num1 + num2 //GOOS can be used in 'go run' command to build for different OS; need reading

	fmt.Println("Result is: ", result)

}
