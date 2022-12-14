package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

func populateRandomValues(columns int, rows int) [][]int {
	m := make([][]int, rows)
	for i := 0; i < rows; i++ {
		for j := 0; j < columns; j++ {
			m[i] = append(m[i], rand.Intn(10))
		}
	}
	return m
}
func populateZeroValues(columns int, rows int) [][]int {
	m := make([][]int, rows)
	for i := 0; i < rows; i++ {
		for j := 0; j < columns; j++ {
			m[i] = append(m[i], 0)
		}
	}
	return m
}
func main() {
	rand.Seed(time.Now().UnixNano())

	columns, _ := strconv.ParseInt(os.Args[1], 10, 32)
	rows, _ := strconv.ParseInt(os.Args[2], 10, 32)

	// Define two matrices
	matrix_1 := populateRandomValues(int(rows), int(columns))
	matrix_2 := populateRandomValues(int(columns), int(rows))

	start := time.Now()

	// Create a new matrix to store the result of the multiplication
	matrix_3 := populateZeroValues(int(columns), int(columns))

	// Loop through each element of matrixA
	for i := 0; i < len(matrix_1); i++ {
		for j := 0; j < len(matrix_2[i]); j++ {
			// Multiply the element of matrixA by the corresponding
			// element of matrixB and add the result to the element
			// of matrixC
			for k := 0; k < len(matrix_2); k++ {
				matrix_3[i][j] += matrix_1[i][k] * matrix_2[k][j]
			}
		}
	}
	fmt.Printf("time %f\n", time.Since(start).Seconds())

	// Print dimentions
	//fmt.Println(columns)
	//fmt.Println(rows)
	// // Print the matrix
	//fmt.Println(matrix_1)
	//fmt.Println(matrix_2)
	// // Print the result matrix
	//fmt.Println(matrix_3)
}
