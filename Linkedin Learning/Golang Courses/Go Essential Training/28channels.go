package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan int)

	/*this will block
	<-ch
	fmt.Println("Here")
	*/

	go func() {
		//send number of the channel
		ch <- 353
	}()

	//get from the channel
	val := <-ch
	fmt.Printf("got %d\n", val)
	fmt.Println("----")

	go func() {
		for i := 0; i < 3; i++ {
			fmt.Printf("Sending %d\n", i)
			ch <- i
			time.Sleep(time.Second)
		}
	}()

	for i := 0; i < 3; i++ {
		val := <-ch
		fmt.Printf("received %d\n", val)
	}

}
