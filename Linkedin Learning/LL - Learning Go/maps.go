package main

import (
	"fmt"
	"sort"
)

func main() {

	states := make(map[string]string)
	states["DL"] = "Delhi"
	states["HR"] = "Haryana"
	states["MH"] = "Maharashtra"
	fmt.Println(states)

	delhi := states["DL"]
	fmt.Println(delhi)

	delete(states, "MH")
	states["PJ"] = "Punjab"
	fmt.Println(states)

	//list all states
	for k, v := range states {

		fmt.Printf("%v, %v\n", k, v)
	}

	//list keys in order
	keys := make([]string, len(states))
	i := 0
	for k := range states {
		keys[i] = k
		i++
	}
	fmt.Println(keys)
	sort.Strings(keys)
	fmt.Println(keys)

	for i := range keys {
		fmt.Println(states[keys[i]])
	}

	//maps are not in any order; can be done by creating a slice and then sorting it

}
