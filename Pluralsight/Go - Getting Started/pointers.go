package main

import "fmt"

func main() {

	firstName := "Harsh"
	fmt.Println(firstName)

	ptr := &firstName
	fmt.Println(ptr, *ptr)

	firstName = "Jatin"
	fmt.Println(ptr, *ptr) //ptr has same value in both cases since it's the same memory address;
	//points to different values though
}
