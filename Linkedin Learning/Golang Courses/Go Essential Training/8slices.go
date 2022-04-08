package main

import (
	"fmt"
)

func main() {

	loons := []string{"bugs", "daffy", "taz"}
	fmt.Printf("loons = %v (type %T)\n", loons, loons)

	fmt.Println(len(loons))
	fmt.Println("---------")

	fmt.Println(loons[1:]) //prints values from index 1
	fmt.Println("---------")

	for i, name := range loons {
		fmt.Printf("%s at %d\n", name, i)
	}
	fmt.Println("------")

	//using above for loop without i variable
	for _, name := range loons {
		fmt.Println(name)
	}

}
