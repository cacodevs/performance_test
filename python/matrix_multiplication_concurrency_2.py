from concurrent.futures import ThreadPoolExecutor
import sys
import time
from matrix_multiplication import generate_matrix, get_columns, dot_point


def dot_point_columns(matrix_result, r,row, columns):
  for c,col in enumerate(columns):
    matrix_result[r,c]=dot_point(row, col)
  return True

def matrix_multiplication_concurrency(matrix_1,matrix_2,executor):
  #generate 0 matrix_result
  matrix_result=[([0]*len(matrix_2[0])) for i in range(len(matrix_1))]
  for r, row in enumerate(matrix_1):
    columns=get_columns(matrix_2)
    executor.submit(dot_point_columns,matrix_result, r, row, columns)
  
  return matrix_result
  


def main():
  rows=int(sys.argv[1]) if len(sys.argv)>2 else 10 
  columns=int(sys.argv[2]) if len(sys.argv)>2 else 10 
  #Generate matrix 1
  matrix_1=generate_matrix(rows,columns)
  #Generate matrix 2
  #change the columns to rows then the matrices can always can multiply
  matrix_2=generate_matrix(columns,rows)
  #caclculate matrix result
  # print(matrix_1)
  # print(matrix_2)
  start_time=time.time()
  executor = ThreadPoolExecutor(max_workers=12)
  matrix_result=matrix_multiplication_concurrency(matrix_1, matrix_2, executor)
  executor.shutdown()
  end_time=time.time()
  print(end_time-start_time)
  # print(matrix_result)



if __name__ == "__main__":
    main()