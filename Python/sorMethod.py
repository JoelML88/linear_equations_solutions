import numpy as np

def sor(A, b, x0=None, omega=1.25, tol=1e-10, max_iter=1000):
  # Obtener el tamaño del sistema
  n = len(b)

  # Inicializar el vector de soluciones x
  x = np.zeros(n) if x0 is None else x0

  # Bucle de iteraciones
  for k in range(max_iter):
      # Copiar la solución anterior para comparar la convergencia
      x_prev = np.copy(x)

      # Iterar sobre cada ecuación en el sistema
      for i in range(n):
          # Calcular la suma de los términos que no involucran la variable actual
          sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x_prev[i + 1:])

          # Calcular la nueva aproximación para la variable actual con el término de relajación
          x[i] = omega * ((b[i] - sigma) / A[i, i]) + (1 - omega) * x_prev[i]

      # Verificar convergencia comparando la norma del cambio en x con la tolerancia
      if np.linalg.norm(x - x_prev, ord=np.inf) < tol:
          print(f"Iteraciones: {k+1}")
          return x

  # Mensaje si el método no converge en el número máximo de iteraciones
  print("El método SOR no convergió en el número máximo de iteraciones.")
  return x
