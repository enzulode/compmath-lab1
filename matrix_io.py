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
