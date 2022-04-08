package main

import (
	"fmt"
	"math"
)

type Square struct {
	length float64
}

func (s *Square) Area() float64 {
	return s.length * s.length
}

type Circle struct {
	radius float64
}

func (circle *Circle) Area() float64 {
	return math.Pi * circle.radius * circle.radius
}

func sumAreas(shapes []Shape) float64 {
	total := 0.0

	for _, shape := range shapes {
		total += shape.Area()
	}

	return total
}

type Shape interface {
	Area() float64
}

func main() {
	s := &Square{20}
	fmt.Println(s.Area())

	c := &Circle{10}
	fmt.Println(c.Area())

	shapes := []Shape{s, c}
	sum := sumAreas(shapes)
	fmt.Println(sum)
}
