package main

import (
	"fmt"
	"strings"
)

func main() {
	var nameFull = " Harsh" + " " + "Jha "
	//var firstName = strings.Fields(nameFull)
	fmt.Println(nameFull)
	fmt.Println(strings.Fields(nameFull))
}
