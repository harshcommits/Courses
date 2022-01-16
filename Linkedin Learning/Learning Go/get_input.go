package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter text: ")
	input, _ := reader.ReadString('\n') //_ used to declare variables to be ignored; used as error variable
	fmt.Println("You entered:", input)

}
