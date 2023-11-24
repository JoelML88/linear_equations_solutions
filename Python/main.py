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
from saveFile import save_file
from datetime import datetime


"""
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


"""

# Matriz de Hilbert de tamaño 50x50
A = np.array([[1 / (i + j + 1) for j in range(50)] for i in range(50)])

# Vector de unos de tamaño 50
b = np.ones(50)


x0 = np.zeros(len(b))

tolerancia = 0.000000001
max_iteraciones = 10000


print("\n*******************************************")
inicio = time.time()
solution,iteraciones = jacobi(A, b,x0, tolerancia, max_iteraciones)
fin = time.time()

#Escribimos log
data_to_add = datetime.now().strftime('%Y-%m-%d %H:%M:%S')+",Jacobi,"+str(tolerancia)+","+str(max_iteraciones) +","+str(fin-inicio)+","+str(iteraciones)+","+str(solution).replace("\n", "")+"\n"
archiveName = "Jacobi_"+ datetime.now().strftime('%d.%m.%Y')+".csv"
save_file(archiveName, data_to_add)



print("Tiempo de ejecución JACOBI: Ini",inicio,"fin:",fin,"Resta: ",fin-inicio)

print("Solución aproximada jacobi:\n", np.vstack(solution))



print("\n*******************************************")
# Ejemplo de uso Gauss-Seidel
x0 = np.zeros(len(b))

inicio = time.time()
solution,iteraciones = gauss_seidel(A, b, x0, tolerancia, max_iteraciones)
fin = time.time()

#Escribimos log
data_to_add = datetime.now().strftime('%Y-%m-%d %H:%M:%S')+",gauss_seidel,"+str(tolerancia)+","+str(max_iteraciones) +","+str(fin-inicio)+","+str(iteraciones)+","+str(solution).replace("\n", "")+"\n"
archiveName = "gauss_seidel_"+ datetime.now().strftime('%d.%m.%Y')+".csv"
save_file(archiveName, data_to_add)


print("Tiempo de ejecución GAUSS: Ini",inicio,"fin:",fin,"Resta: ",fin-inicio)
print("Solución aproximada gauss_seidel:\n", np.vstack(solution))





print("\n*******************************************")
#Ejemplo SOR
omega=1.2
x0 = np.zeros(len(b))
inicio = time.time()
solution,iteraciones = sor(A, b, x0, omega, tolerancia, max_iteraciones)
fin = time.time()

#Escribimos log
data_to_add = datetime.now().strftime('%Y-%m-%d %H:%M:%S')+",SOR,"+str(tolerancia)+","+str(max_iteraciones) +","+str(fin-inicio)+","+str(iteraciones)+","+str(solution).replace("\n", "")+"\n"
archiveName = "SOR_"+ datetime.now().strftime('%d.%m.%Y')+".csv"
save_file(archiveName, data_to_add)

print("Tiempo de ejecución SOR: Ini",inicio,"fin:",fin,"Resta: ",fin-inicio)
print("Solución aproximada SOR:\n", np.vstack(solution))

