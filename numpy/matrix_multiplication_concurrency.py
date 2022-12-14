import concurrent.futures
import numpy as np
import sys
import time

def main():
  # Get dimmentions
  rows=int(sys.argv[1]) if len(sys.argv)>2 else 10 
  columns=int(sys.argv[2]) if len(sys.argv)>2 else 10 

  # Generate the matrix
  matrix_1 = np.random.randint(low=0, high=11, size=(rows, columns))
  matrix_2 = np.random.randint(low=0, high=11, size=(columns, rows))

  # Create a new matrix to store the result of the multiplication
  matrix_result = np.zeros((rows, rows))

  def multiply_element(i, j):
    for k in range(len(matrix_1)):
      matrix_result[i][j] += matrix_1[i][k] * matrix_2[k][j]

  def multiply_elements(i):
    for j in range(len(matrix_2)):
      matrix_result[i][j]=np.dot(matrix_1[i], matrix_2[:,j])

  start_time=time.time()

  with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
    # Submit a task for each element of matrixA to be multiplied
    for i in range(len(matrix_1)):
      try:
        executor.submit(multiply_elements,i)
      except:
        print('Error!')

    #executor.shutdown(wait=True)

  end_time=time.time()
  print(end_time- start_time)
  # print(matrix_1)
  # print(matrix_2)
  # Print the result matrix
  #print(matrix_result)

if __name__ == "__main__":
    main()
