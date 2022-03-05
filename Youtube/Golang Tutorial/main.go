package main

import "fmt"

func main() {
	var conferenceName = "Go Conference"
	const conferenceTickets = 50

	fmt.Println("Welcome to the", conferenceName, "Booking screen\nGet the tickets here.")
	fmt.Println(conferenceTickets, "tickets available")
}
