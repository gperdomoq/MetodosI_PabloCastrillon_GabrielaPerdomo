import numpy as np

X = np.array([0,0.5,1])
Y = np.array([1,0.10653,-0.63212])

f1 = (Y[1]-Y[0])/(X[1]-X[0])
f2 = (Y[2]-Y[1])/(X[2]-X[1])

a=(((Y[2]-Y[1])/(X[2]-X[1]))-((Y[1]-Y[0])/(X[1]-X[0])))/(X[2]-X[0])

b=((Y[1]-Y[0])/(X[1]-X[0]))-((X[0]+X[1])*a)

c=Y[0]-((X[0])*(X[1]-X[0]))+((X[0])*(X[1])*a)

print(a,b,c)




x=np.linspace(-0.2,1.2,50)
h=x[1]-x[0]
def DerivadaCentral(f,x,h=1e-6):
    return (f(x+h) - f(x-h))/(2*h)

def GetNewtonMethod(f,df,xn,itmax=100,precision=1e-9):
    
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
    y=(0.3096399999999999*((x)*2))-(1.94176(x))+1
    return y





def GetAllRoots(x, tolerancia=10):
    
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

print (raices)
#solucion punto a

def boltzano(x0,x1,f):

    c = (x0 + x1) / 2
    while f(c)!=0:
        if f(c)>0:
            x0=c
        elif f(c)<0:
            x1=c
        c=(x0+x1)/2
    return(x0,x1)

def funcionb(x):
    y=(np.exp(-x))-x
    return y

puntob=boltzano(0,1,funcionb)
print(puntob)
#solucion punto b

print((puntob[0]+puntob[1])/2)
#solucion punto c

x3mas=(-2*c)/(b+((b**2)-(4*a*c))**0.5)
x3menos=(-2*c)/(b-((b**2)-(4*a*c))**0.5)

print(x3mas,x3menos)
#como el primer valor de x3 no es una raíz de la función, decimos que x3 es igual a x3menos(solucion punto d)

def redondeo(x3menos):
        if n<100:
            epsilon=round(np.abs(funcion(x3menos)),n)
            if epsilon<(1*(10**(-10))):
                return epsilon
            else:
                n+=1
            return epsilon
        else:
            return False
#solución punto e
        

#la raiz es de 0.56714329040978(punto f)
