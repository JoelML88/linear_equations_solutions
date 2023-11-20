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

from jacobiMethod import *
from  gaussSeidelMethod import gauss_seidel
from sorMethod import sor
from luMethod import *



#Ingresamos una matriz diagonal Dominante

A = np.array([[5, 2, -3],
              [2, 10, -8],
              [3, 8, 13]])

#ingresamos b
b = np.array([1, 4, 7])


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
initial_guess = np.zeros(len(b))
solution = gauss_seidel(A, b, x0=initial_guess)
print("Solución aproximada gauss_seidel:", solution)



"""
print("\n*******************************************")
initial_guess = np.zeros(len(b))
solution = jacobi2(A, b, x0=initial_guess)
print("Solución aproximada jacobi:", solution)



print("\n*******************************************")
#Ejemplo SOR
initial_guess = np.zeros(len(b))
solution = sor(A, b, x0=initial_guess)
print("Solución aproximada SOR:", solution)



print("\n*******************************************")
# Realizar la descomposición LU
L, U = lu_decomposition(A)
# Resolver el sistema de ecuaciones lineales mediante la descomposición LU
solution = solve_lu(L, U, b)
print("Solución aproximada LU:", solution)

"""
