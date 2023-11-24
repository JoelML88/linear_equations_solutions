import numpy as np

    


def jacobi(A, b, x0=None, tol=0.1, max_iter=1000):
    """
    Método de Jacobi para resolver el sistema de ecuaciones lineales Ax=b.

    Parámetros:
    - A: Matriz del sistema de ecuaciones.
    - b: Vector de términos constantes.
    - x0: Aproximación inicial.
    - tol: Tolerancia para el criterio de parada.
    - max_iter: Número máximo de iteraciones.

    Devuelve:
    - x: Solución aproximada del sistema de ecuaciones.
    """
    
    # n es el tamaño del sistema
    n = len(b)

    # Inicialización del vector de solución x
    x = np.zeros(n) if x0 is None else x0
    x_prev = np.copy(x)  # Vector auxiliar para almacenar la solución previa

    # Bucle de iteraciones
    for k in range(max_iter):
        # Iterar sobre cada ecuación en el sistema
        for i in range(n):
            # Calcular la suma de los términos que no involucran la variable actual
            sigma = np.dot(A[i, :i], x_prev[:i]) + np.dot(A[i, i + 1:], x_prev[i + 1:])

            # Calcular la nueva aproximación para la variable actual
            x[i] = (b[i] - sigma) / A[i, i]

        # Verificar convergencia comparando la norma del cambio en x con la tolerancia
        if np.linalg.norm(x - x_prev, ord=np.inf) < tol:
            print(f"Iteraciones: {k+1}")
            return x,k+1

        # Actualizar el vector de solución previa
        x_prev[:] = x

    # Mensaje si el método no converge en el número máximo de iteraciones
    print("El método de Jacobi no convergió en el número máximo de iteraciones.")
    return x,k+1