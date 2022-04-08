package main

import (
	"fmt"
	"math"
)

func sqrt(n float64) (float64, error) {
	if n < 0 {
		return 0.0, fmt.Errorf("sqrt of negative value (%f)", n) //used for custom error statement
	}

	return math.Sqrt(n), nil //nil=null; used since there is nothing to return for error
}

func main() {
	s1, err := sqrt(2.0)
	if err != nil {
		fmt.Printf("ERROR: %s\n", err)
	} else {
		fmt.Println(s1)
	}

	s2, err := sqrt(-2.0)
	if err != nil {
		fmt.Printf("ERROR: %s\n", err)
	} else {
		fmt.Println(s2)
	}
}
