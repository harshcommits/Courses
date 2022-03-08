package main

import (
	"fmt"
)

func main() {
	const c = 3
	//const c int = 3
	fmt.Println(c + 3)

	//adding to float value; will not work if line 9 is used instead of line 8
	fmt.Println(c + 1.2)
	//fmt.Println(float32(c) + 1.3)  //line will work with line 9
}
