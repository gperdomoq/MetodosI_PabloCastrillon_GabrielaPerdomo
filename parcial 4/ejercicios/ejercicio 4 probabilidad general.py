import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, factorial

     
def calcular_probabilidad(n):
  casos_favorables=factorial(365)
  casos_posibles=(factorial(365 - n)) * (365 ** n)
  return casos_favorables/casos_posibles
puntos=[]
n=np.linspace(1, 80,80)
for i in n:
  a=calcular_probabilidad(i)
  puntos.append(a)
plt.scatter(n,puntos)
plt.xlabel('Personas')
plt.ylabel('Probabilidad')
print('Los ejes corresponden a la probabilidad de tener fechas diferentes de cumpleaños en función del número de personas.')