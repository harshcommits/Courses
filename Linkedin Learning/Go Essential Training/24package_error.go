package main

import (
	"fmt"
	"log"
	"os"
)

type Config struct {
}

func readConfig(path string) (*Config, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
		//return nil, errors.Wrap(err, "Can't open config file")
	}

	defer file.Close()

	cfg := &Config{}
	return cfg, nil
}

func setupLogging() {
	out, err := os.OpenFile("app.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644) //creates app.log with error
	if err != nil {
		return
	}

	log.SetOutput(out)
}

func main() {
	setupLogging()
	cfg, err := readConfig("/path/to/config.file")
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: %s\n", err)
		log.Printf("error: %+v\n", err)
		os.Exit(1)
	}

	fmt.Println(cfg)
}
