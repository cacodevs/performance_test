package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"sync"
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

	// Create a WaitGroup to wait for all goroutines to finish
	var wg sync.WaitGroup

	// Loop through each element of matrixA
	for i := 0; i < len(matrix_1); i++ {
		for j := 0; j < len(matrix_2[i]); j++ {
			// Increment the WaitGroup counter
			wg.Add(1)
			go func(i, j int) {
				for k := 0; k < len(matrix_2); k++ {
					matrix_3[i][j] += matrix_1[i][k] * matrix_2[k][j]
				}

				// Decrement the WaitGroup counter
				wg.Done()
			}(i, j)
		}
	}

	// Wait for all goroutines to finish
	wg.Wait()

	fmt.Printf("time %f\n", time.Since(start).Seconds())

	// // Print the matrix
	// fmt.Println(matrix_1)
	// fmt.Println(matrix_2)

	// // Print the result matrix
	// fmt.Println(matrix_3)
}
