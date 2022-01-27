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

	fmt.Println("Operation(+ - * /): ")
	operation, _ := reader.ReadString('\n')
	action := strings.TrimSpace(operation)
	//fmt.Println(action)

	switch action {
	case "+":
		fmt.Println("The result is: ", add(num1, num2))
	case "-":
		fmt.Println("The result is: ", subtract(num1, num2))
	case "*":
		fmt.Println("The result is: ", multiply(num1, num2))
	case "/":
		fmt.Println("The result is: ", add(num1, num2))
	default:
		panic("Invalid value entered")
	}

}

func add(value1 float64, value2 float64) float64 {
	result := value1 + value2
	return result
}

func subtract(value1 float64, value2 float64) float64 {
	result := value1 - value2
	return result
}

func multiply(value1 float64, value2 float64) float64 {
	result := value1 * value2
	return result
}

func divide(value1 float64, value2 float64) float64 {
	result := value1 / value2
	return result
}
