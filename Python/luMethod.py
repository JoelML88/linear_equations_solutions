
import numpy as np

from scipy.linalg import lu



#***************************************************************
def lu_decomposition(A):
  """
  Realiza la descomposición LU de una matriz cuadrada A.

  Parámetros:
  - A: Matriz cuadrada de entrada.

  Devuelve:
  - L: Matriz triangular inferior de la descomposición LU.
  - U: Matriz triangular superior de la descomposición LU.
  """
  n = len(A)

  # Inicializar matrices L y U
  L = np.zeros((n, n))
  U = np.zeros((n, n))

  # Descomposición LU
  for i in range(n):
      # L tiene unos en la diagonal principal
      L[i, i] = 1.0

      # Calcular elementos de la fila i de U
      for j in range(i, n):
          U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])

      # Calcular elementos de la columna i de L
      for k in range(i + 1, n):
          L[k, i] = (A[k, i] - np.dot(L[k, :i], U[:i, i])) / U[i, i]

  return L, U

def solve_lu(L, U, b):

  """
  Resuelve un sistema de ecuaciones lineales Ax = b mediante la descomposición LU.

  Parámetros:
  - L: Matriz triangular inferior de la descomposición LU.
  - U: Matriz triangular superior de la descomposición LU.
  - b: Vector de términos constantes.

  Devuelve:
  - x: Solución del sistema.
  """
  # Resolver Ly = b mediante sustitución hacia adelante
  y = np.linalg.solve(L, b)

  # Resolver Ux = y mediante sustitución hacia atrás
  x = np.linalg.solve(U, y)

  return x

#***************************************************************