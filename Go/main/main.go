package main

import "fmt"
import "..\Hello\Hello"

func main() {
	fmt.Println("My favorite number is")
	Hello.HelloWorld()
}