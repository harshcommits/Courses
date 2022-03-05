package main

import "fmt"

func main() {
	var conferenceName = "Go Conference"
	const conferenceTickets = 50

	fmt.Printf("Welcome to the %s Booking screen\nGet the tickets here.", conferenceName)
	//fmt.Println(conferenceTickets, "tickets available")
	fmt.Printf("%v tickets are available.", conferenceTickets)

}
