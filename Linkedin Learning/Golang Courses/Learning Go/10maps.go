package main

import (
	"fmt"
)

func main() {
	states := make(map[string]string)
	fmt.Println(states)
	states["RJ"] = "Rajasthan"
	states["DL"] = "Delhi"
	states["BR"] = "Bihar"
	fmt.Println(states) //sorts by key by default

	for k, v := range states {
		fmt.Printf("%v: %v\n", k, v)
	}

	delhi := states["DL"]
	fmt.Println(delhi)

	delete(states, "BR")
	fmt.Println(states)
}
