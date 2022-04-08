package main

import (
	"fmt"
	"net/http"
	//"sync"
)

func returnType(url string, out chan string) {
	resp, err := http.Get(url)
	if err != nil {
		out <- fmt.Sprintf("%s -> error: %s", url, err)
		return
	}

	defer resp.Body.Close()
	ctype := resp.Header.Get("content-type")
	out <- fmt.Sprintf("%s -> %s\n", url, ctype)
}

func main() {
	urls := []string{
		"https://golang.org",
		"https://api.github.com",
		"https://httpbin.org/xml",
	}

	/*
		for _, url := range urls {
			returnType(url)
		}
	*/

	ch := make(chan string)

	for _, value := range urls {
		go returnType(value, ch)
	}

	for range urls {
		out := <-ch
		fmt.Println(out)
	}

}
