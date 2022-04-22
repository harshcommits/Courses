package main

import (
	"fmt"
)

type Dog struct {
	Breed  string
	Weight int
}

func main() {

	poodle := Dog{"Poodle", 10}
	fmt.Println(poodle)
	fmt.Printf("%+v\n", poodle) //shows data as key-value pairs
	fmt.Printf("Breed: %v\nWeight: %v\n", poodle.Breed, poodle.Weight)

}