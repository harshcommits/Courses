package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	rand.Seed(time.Now().Unix())
	dow := rand.Intn(7) + 1
	fmt.Println("Day", dow)

	var result string

	//	another way to declare variable and switch statement in one line
	//	switch dow := rand.Intn(7) + 1; dow {
	switch dow {
	case 1:
		result = "It's Sunday"
		fallthrough //skips through the case and goes to the next one; here it prints default irrespective of value
	case 2:
		result = "It's Monday"
		fallthrough
	default:
		result = "It's some other day!"
	}

	fmt.Println(result)

}
