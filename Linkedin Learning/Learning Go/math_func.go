package main

import (
	"fmt"
	"math"
)

func main() {
	i1, i2, i3 := 12, 45, 68
	intSum := i1 + i2 + i3
	fmt.Println("Integer sum: ", intSum)

	f1, f2, f3 := 12.4, 44.3, 32.7
	floatSum := f1 + f2 + f3
	fmt.Println("Float sum: ", floatSum)

	floatSum = math.Round(floatSum) //:= not used since floatSum is defined in line 14
	fmt.Println("The sum is now: ", floatSum)

	circleRadius := 15.5
	circumference := circleRadius * 2 * math.Pi
	fmt.Printf("Circumference: %.2f\n", circumference) //%.2f print 2 values after decimal point

}
