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
from  gaussSeidelMethod import gauss_seidel
from sorMethod import sor



#Ingresamos una matriz diagonal Dominante

A = np.array([[5, 2, -3],
              [2, 10, -8],
              [3, 8, 13]])

#ingresamos b
b = np.array([1, 4, 7])

initial_guess = np.zeros(len(b))


"""

A = np.array([[1.5, 2, 1.5],
              [1, 3, -1],
              [1, 2, 3]])

#ingresamos b
b = np.array([0, -2, 2])

1 2 3 |2
1 3 -1|-2
3 4 3 |0


print("\n*******************************************")
initial_guess = np.zeros(len(b))
solution = jacobi(A, b,initial_guess, 0.000001, 1000)
print("Solución aproximada jacobi:", solution)

"""

print("\n*******************************************")
# Ejemplo de uso Gauss-Seidel
inicio = time.time()

solution = gauss_seidel(A, b, x0=initial_guess)
print("Solución aproximada gauss_seidel:", solution)
fin = time.time()
print("Tiempo con Recursivo2: ",fin-inicio)


"""
print("\n*******************************************")
inicio = time.time()
solution = jacobi2(A, b, x0=initial_guess)
fin = time.time()
print("Solución aproximada jacobi:", solution)



print("\n*******************************************")
#Ejemplo SOR
inicio = time.time()
solution = sor(A, b, x0=initial_guess)
fin = time.time()
print("Solución aproximada SOR:", solution)


"""
