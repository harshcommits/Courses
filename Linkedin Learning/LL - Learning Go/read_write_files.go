package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"os"
)

func main() {

	content := "Hello from Go!"
	file, err := os.Create("./testfile.txt")
	checkError(err)
	length, err := io.WriteString(file, content)
	checkError(err)
	fmt.Printf("Wrote a file with %v characters\n", length)
	defer file.Close()
	defer readFile("./testfile.txt") //defer wait until all is done and then executes the command

}

func readFile(fileName string) {
	data, err := ioutil.ReadFile(fileName)
	checkError(err)
	fmt.Println("Text read from the file: ", string(data)) //converting data to string since readfile returns bytes
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
