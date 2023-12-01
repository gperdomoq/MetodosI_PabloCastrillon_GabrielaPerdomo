import random
import numpy as np
import matplotlib.pyplot as plt

N = int(10**5)

def tirar_moneda():
   
    resultado = []
    for _ in range(4):  
        lanzamiento = random.choice(['C', 'S'])  
        resultado.append(lanzamiento)
    return resultado


conteo_mas1=0
conteo_menos1=0  
for _ in range(N):
    resultado = tirar_moneda()
    if resultado.count('C') == 2:
      conteo_mas1+=1
    
    elif resultado.count('C') == 2:
      conteo_menos1-=1
conteo_final=abs(conteo_menos1)+conteo_mas1


probabilidad=conteo_final/N
print('La probabilidad es de ',probabilidad)