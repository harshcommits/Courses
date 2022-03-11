package main

import (
	"fmt"
)

func doubleAt(values []int, i int) {
	values[i] *= 2
}

func double(n int) {
	n *= 2
	fmt.Println(n)
}

func doublePtr(n *int) {
	*n *= 2
}

func main() {
	values := []int{1, 2, 3, 4}
	doubleAt(values, 2)
	fmt.Println(values)

	double(10) //prints 20; since the value in function is 10*2=20

	val := 10
	double(val)
	fmt.Println(val) //prints 10; since integer is called by value, the value doesn't change outside of function

	//above gymnastics can be avoided using pointers
	doublePtr(&val)
	fmt.Println(val) //prints 20; since it's referring to the updated value, not the original int
}
