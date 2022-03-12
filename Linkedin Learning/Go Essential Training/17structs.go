package main

import (
	"fmt"
)

type Trade struct {
	Symbol string
	Volume int
	Price  float64
	Buy    bool
}

func main() {

	t1 := Trade{"MSFT", 10, 99.44, true}
	fmt.Println(t1)

	fmt.Printf("%+v\n", t1)

	fmt.Println(t1.Symbol)

	t2 := Trade{
		Symbol: "GOOG",
		Volume: 2,
		Price:  91.44,
		Buy:    true,
	}

	fmt.Printf("%+v\n", t2)
}
