class FileError(Exception):
  """
    Represents file-related errors.
  """
  def __init__(self, message) -> None:
    super().__init__("File error occured: " + message)

class MatrixError(Exception):
  """
    Represents matrix-related errors.
  """
  def __init__(self, message) -> None:
    super().__init__("Matrix error occured: " + message)
