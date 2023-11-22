"""
---------Joel Méndez León-----------------
---------Karen Ailed Tellez Gomez---------

Resolución de sistemas de ecuaciones de la forma Ax=b

"""

"""
https://numpy.org/doc/stable/user/whatisnumpy.html


JACOBI:
http://blog.espol.edu.ec/analisisnumerico/jacobi-metodo/

Gauss-Seidel
http://blog.espol.edu.ec/analisisnumerico/gauss-seidel-ejemplo01/

SOR:
https://es.wikipedia.org/wiki/Sobrerrelajación_sucesiva

LU:
http://blog.espol.edu.ec/analisisnumerico/metodo-con-matrices-triangulares-alu/

"""

import numpy as np
import time

from jacobiMethod import *
from gaussSeidelMethod import gauss_seidel
from sorMethod import sor



#Ingresamos una matriz diagonal Dominante

A = np.array([[4, -1, 0, -1, 0, 0, 0, 0, 0],
              [-1, 4, -1, 0, -1, 0, 0, 0, 0],
              [0, -1, 4, 0, 0, -1, 0, 0, 0],
              [-1, 0, 0, 4, -1, 0, -1, 0, 0],
              [0, -1, 0, -1, 4, -1, 0, -1, 0],
              [0, 0, -1, 0, -1, 4, 0, 0, -1],
              [0, 0, 0, -1, 0, 0, 4, -1, 0],
              [0, 0, 0, 0, -1, 0, -1, 4, -1],
              [0, 0, 0, 0, 0, -1, 0, -1, 4],
              ])

#ingresamos b
b = np.array([150, 100, 150, 50, 0, 50, 50, 0, 50])

x0 = np.zeros(len(b))

tolerancia = 0.000000001
max_iteraciones = 1000



print("\n*******************************************")
inicio = time.time()

solution = jacobi(A, b,x0, tolerancia, max_iteraciones)
fin = time.time()
print("Tiempo de ejecución JACOBI: ",fin-inicio)

print("Solución aproximada jacobi:\n", np.vstack(solution))



print("\n*******************************************")
# Ejemplo de uso Gauss-Seidel
x0 = np.zeros(len(b))

inicio = time.time()
solution = gauss_seidel(A, b, x0, tolerancia, max_iteraciones)
fin = time.time()
print("Tiempo de ejecución GAUSS: ",fin-inicio)

print("Solución aproximada gauss_seidel:\n", np.vstack(solution))





print("\n*******************************************")
#Ejemplo SOR
omega=1.2
x0 = np.zeros(len(b))
inicio = time.time()
solution = sor(A, b, x0, omega, tolerancia, max_iteraciones)
fin = time.time()
print("Tiempo de ejecución SOR: ",fin-inicio)

print("Solución aproximada SOR:\n", np.vstack(solution))



"""
print("\n*******************************************")
inicio = time.time()
solution = jacobi2(A, b, x0=initial_guess)
fin = time.time()
print("Solución aproximada jacobi:", solution)




"""




"""

A = np.array([[5, 2, -3],
              [2, 10, -8],
              [3, 8, 13]])

#ingresamos b
b = np.array([1, 4, 7])


A = np.array([[1.5, 2, 1.5],
              [1, 3, -1],
              [1, 2, 3]])

#ingresamos b
b = np.array([0, -2, 2])

1 2 3 |2
1 3 -1|-2
3 4 3 |0

"""