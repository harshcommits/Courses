package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"os"
)

var data = `
{
	"user": "Scrooge McDuck",
	"type": "deposit",
	"amount": 100000.3
}
`

//Request form for bank transaction
type Request struct {
	Login  string  `json:"user"`
	Type   string  `json:"type"`
	Amount float64 `json:"amount"`
}

func main() {
	rdr := bytes.NewBufferString(data) //simulate a file/socket

	//decode request
	dec := json.NewDecoder(rdr)

	req := &Request{}
	if err := dec.Decode(req); err != nil {
		log.Fatalf("error: can't decode - %s", err)
	}

	fmt.Printf("got: %+v\n", req)

	//create response
	prevBalance := 850000.0
	resp := map[string]interface{}{ //here map has string keys and empty interface as values, which allows any type
		"ok":      true,
		"balance": prevBalance + req.Amount,
	}

	//encode response
	enc := json.NewEncoder(os.Stdout)
	if err := enc.Encode(resp); err != nil {
		log.Fatalf("error: can't encode - %s", err)
	}
}
