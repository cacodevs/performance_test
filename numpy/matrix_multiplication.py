import numpy as np
import sys
import time

def matrix_multiplication_numpy(matrix_1,):
  return 

def main():
  # Get dimmentions
  rows=int(sys.argv[1]) if len(sys.argv)>2 else 10 
  columns=int(sys.argv[2]) if len(sys.argv)>2 else 10 

  # Generate the matrix
  matrix_1 = np.random.randint(low=0, high=11, size=(rows, columns))
  matrix_2 = np.random.randint(low=0, high=11, size=(columns, rows))

  start_time=time.time()
  # Multiply the matrices
  matrix_result = np.matmul(matrix_1, matrix_2)
  end_time=time.time()
  print(end_time-start_time)
  # Print the result
  # print(matrix_result)


if __name__ == "__main__":
    main()