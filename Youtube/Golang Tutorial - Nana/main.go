package main

import (
	"fmt"
	"strings"
)

func main() {
	var conferenceName string = "Go Conference"
	//	conferenceName := "Go Conference"	allows you to declare variable with values without any keywords; can't be used for constants
	const conferenceTickets int = 50
	var remainingTickets uint

	fmt.Printf("Welcome to the %v Booking screen\nGet the tickets here.", conferenceName)
	//fmt.Println(conferenceTickets, "tickets available")
	fmt.Printf("%v tickets are available. %v tickets remaining\n", conferenceTickets, remainingTickets)

	bookings := []string{} //array definition; only single data type elements
	fmt.Println(bookings)

	//declare variables without assigning values; requires specifying data type
	var userName string
	var userTickets uint

	//get input
	fmt.Println("Enter the values for username and tickets")
	fmt.Scan(&userName) //variable taken in as a pointer
	fmt.Scan(&userTickets)

	fmt.Printf("User %v bought %v tickets\n", userName, userTickets)
	bookings = append(bookings, userName)

	fmt.Println("List of users who booked the tickets: ")
	for i, booking := range bookings {
		booking = bookings[i]
		fmt.Println(booking)

	}

}
