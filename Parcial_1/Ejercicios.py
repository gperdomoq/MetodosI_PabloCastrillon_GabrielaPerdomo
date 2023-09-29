import numpy as np


x=np.linspace(-2.2,1.0,50)
h=x[1]-x[0]
def DerivadaCentral(f,x,h=1e-6):
    return (f(x+h) - f(x-h))/(2*h)

def GetNewtonMethod(f,df,xn,itmax=100,precision=1e-8):
    
    error = 1.
    it = 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
            # Criterio de parada
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        
   # print('Raiz',xn,it)
    
    if it == itmax:
        return False
    else:
        return xn
    

def funcion(x):
    y=(3*((x)*5))+(5(x)**4)-((x)**3)
    return y




def GetAllRoots(x, tolerancia=6):
    
    raices = np.array([])
    
    for i in x:
        
        raiz=GetNewtonMethod(funcion, DerivadaCentral,i)
        
        if raiz != False:
            
            croot = np.round(raiz, tolerancia)
            
            if croot not in raices:
                raices = np.append(raices,croot)
                
    raices.sort()
    
    return raices
raices=GetAllRoots(x)

print(raices)
