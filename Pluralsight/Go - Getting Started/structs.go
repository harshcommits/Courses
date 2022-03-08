package main

import (
	"fmt"
)

func main() {

	type user struct {
		ID        int    //prints 0 by default
		firstName string //prints blank by default
	}

	var u user
	fmt.Println(u)

	//adding values to struct
	u.ID = 1
	u.firstName = "Harsh"

	//printing new values
	fmt.Println(u)

	u2 := user{ID: 2, firstName: "Arthur"}
	fmt.Println(u2)

}
