package main

import (
	"fmt"
)

func main() {
	count := 0

	for a := 1000; a <= 9999; a++ {
		for b := a; b <= 9999; b++ { //remove repetition of transactions
			n := a * b

			//if a * b is even-ended
			s := fmt.Sprintf("%d", n)
			if s[0] == s[len(s)-1] {
				count++
			}
		}
	}

	//get the number
	fmt.Println(count)
}
