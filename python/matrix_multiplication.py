import sys
import random
import time

def generate_matrix(rows, columns):
  new_matrix=[]
  for n in range(rows):
    new_row=[]
    for m in range(columns):
      new_row.append(random.randint(0,10))
    new_matrix.append(new_row)
  
  return new_matrix

def get_columns(matrix):
  columns=[]
  for i in range(len(matrix[0])):
    columns.append([row[i] for row in matrix])
  return columns



def dot_point(row,column):
  result=0
  for i in range(len(row)):
    result+=row[i]*column[i]
  return result

def matrix_multiplication(matrix_1,matrix_2):
  #generate 0 matrix_result
  matrix_result=[([0]*len(matrix_2[0])) for i in range(len(matrix_1))]
  for r, row in enumerate(matrix_1):
    for c,col in enumerate(get_columns(matrix_2)):
      matrix_result[r][c]=dot_point(row,col)
  return matrix_result



def main():
  rows=int(sys.argv[1]) if len(sys.argv)>2 else 10 
  columns=int(sys.argv[2]) if len(sys.argv)>2 else 10 
  #Generate matrix 1
  matrix_1=generate_matrix(rows,columns)
  #Generate matrix 2
  #change the columns to rows then the matrices can always can multiply
  matrix_2=generate_matrix(columns,rows)
  #multiply matrix
  #print(matrix_1)
  #print(matrix_2)
  start_time=time.time()
  matrix_result=matrix_multiplication(matrix_1,matrix_2)
  end_time=time.time()
  print(end_time-start_time)
  #print(matrix_result)





if __name__ == "__main__":
    main()