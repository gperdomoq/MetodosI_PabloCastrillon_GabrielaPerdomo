import numpy as np
from tqdm import tqdm



Dx = lambda f,x,y,h=1e-5: (f(x+h,y) - f(x-h,y))/(2*h)
Dy = lambda f,x,y,h=1e-5: (f(x,y+h) - f(x,y-h))/(2*h)

x0, y0 = 2,2

Gradient = lambda f,x,y: np.array([Dx(f,x,y),Dy(f,x,y)])


def Minimizer(f, N, gamma = 1):

    r = np.zeros((N,2))
    r[0] = np.random.uniform(-5.,5.,size=2)

    Grad = np.zeros((N,2))
    Grad[0] = Gradient(f,r[0,0],r[0,1])
    for i in tqdm(range(1,N)):
        r[i] = r[i-1] - gamma*Gradient(f,r[i-1,0],r[i-1,1])
        Grad[i] = Gradient(f,r[i-1,0],r[i-1,1])


    return r,Grad[i]

N=200
#print(Minimizer(funcion,N))
#Para la funcion 1:
def funcion1(x,y):
  f=np.log(x**2 +y**2) + np.sin(x*y) - np.log(2) -np.log(np.pi)
  return f
respuesta1=(Minimizer(funcion1,N))
lista_respuesta1=[]
for i in respuesta1:
  if (funcion1(i[0],i[1])==0).all:
    lista_respuesta1.append(i)
print(lista_respuesta1)


#Para la funcion 2:
def funcion2(x,y):
  f=np.exp(x-y) + np.cos(x*y)
  return f


respuesta2=(Minimizer(funcion2,N))
lista_respuesta2=[]
for i in respuesta2:
  if (funcion2(i[0],i[1])==0).all:
    lista_respuesta2.append(i)
print(lista_respuesta2)