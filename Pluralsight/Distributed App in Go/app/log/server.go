package log

import (
	stlog "log"
	"os"
)

var log *stlog.Logger

type fileLog string

func (f1 fileLog) Write(data []byte) (int, error) {
	f, err := os.OpenFile(string(f1), os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0600)
	if err != nil {
		return 0, err
	}
	defer f.Close()
	return f.Write(data)
}

func Run(destination string) {
	log = stLog.New(fileLog())
}
