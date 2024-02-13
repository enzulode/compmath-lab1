import numpy as np
import os
import errors as err

def from_file(filename: str):
  """
    This function performs SLAE parsing from the specific file.
  """
  if not(os.path.isfile(filename)):
    raise err.FileError("file not found")

  try:
    A = np.loadtxt(filename, unpack=True, dtype=float) # load data as matrix
    A = np.transpose(A) # transpose the matrix

    b = A[len(A)-1]
    A = np.delete(A, (len(A)-1), axis=0)

    if len(A) <= 0: # check matrix size is correct
      raise err.MatrixError("invalid matrix size")
    
    return A, b
  except Exception:
    raise err.MatrixError(f"invalid matrix format in the '{filename}' file") # notify user about difficulties

def from_keyboard():
  """
    This function performs SLAE parsing from the CLI.
  """
  n = int(input("Matrix size: ")) # get the matrix size

  if n <= 0: # check matrix size is correct
    raise err.MatrixError("invalid matrix size")

  A = []
  print("Fill in the matrix:")
  for i in range(n): # read the matrix row by row
    print(f"Put {i+1}-th row: ", end = '')
    row = [float(i) for i in input().split(' ', n - 1)]
    A.append(row)

  print("Enter free members column:\n", end = '')
  b = [float(i) for i in input().split(' ', n - 1)]

  return np.array(A, float), np.array(b, float)

def print_matrix(matrix: list) -> None:
  """
    This function performs formatted output of the provided matrix.
  """
  if (matrix_size := len(matrix)) == 1:
    print("----------------------------")
    print(matrix[0][0])
    print("----------------------------")
    return


  print("----------------------------")
  for i in matrix:
    for j in i:
      print(f"{j:7}", end="")
    print()
  print("----------------------------")
  return
