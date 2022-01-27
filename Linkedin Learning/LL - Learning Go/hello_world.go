package main

import "fmt"

//this is a constant declaration; it's done out of function scope
// here it is explicitly defined as int
const aConst int = 64

func main() {

	var aString string = "This is Go!"
	fmt.Println(aString)
	fmt.Printf("The variable type is %T\n", aString)

	var aInteger int = 42
	fmt.Println(aInteger)

	var defaultInt int
	fmt.Println(defaultInt)

	var anotherString = "This is another string"
	fmt.Println(anotherString)
	fmt.Printf("The variable type is %T\n", anotherString)

	//below line uses the := operator to avoid using var keyword
	novarString := "This is a string without var"
	fmt.Println(novarString)
	fmt.Printf("The variable type is %T\n", novarString)

	fmt.Println(aConst)
	fmt.Printf("The variable type is %T\n", aConst)
}
