import numpy as np
from sympy import symbols, integrate

x, y = symbols('x y')
f = 2/3 * (x + 2*y)

integral = integrate(integrate(f, (x, 0, 1)), (y, 0, 1))
print('El valor de la integral ',integral, '.Además, no tiene valores negativos en los intervalos dados, por lo que sí es una función de probabilidad válida.')

distribucion_g=integrate(f,(y,0,1))
#print (distribucion_g)

print('La distribucion g(x) es 2(y+1)/3')

distribucion_h=integrate(f,(x,0,1))
#print (distribucion_h)

print('La distribucion h(y) es (4x+1)/3')
f1=x*f
Ex=integrate(x*distribucion_g,(x,0,1))
Ey=integrate(y*distribucion_h,(y,0,1))
#print(Ex,Ey)
print('Los valores esperados de x y "y" son ',(Ex,Ey),' respectivamente')
Exy=integrate(integrate(x*y*f,(x,0,1)),(y,0,1))
covarianza=Exy-((Ex)*(Ey))
print('La covarianza es de ',covarianza)