package main

import (
	"fmt"
)

func main() {

	poodle := Dog{"Poodle", 10}
	fmt.Println(poodle)
	fmt.Printf("%+v\n", poodle)
	fmt.Printf("Breed: %v\nWeight: %v\n", poodle.Breed, poodle.Weight)
	poodle.Weight = 9 //update field value for type dog
	fmt.Printf("Breed: %v\nWeight: %v\n", poodle.Breed, poodle.Weight)

}

// dog struct definition
type Dog struct {
	Breed  string
	Weight int
}
