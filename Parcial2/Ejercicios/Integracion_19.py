import numpy as np
import matplotlib.pyplot as plt


def ecuacion_banda_prohibida(x,T,Td=300):
    sqr = np.sqrt(pow(x, 2) + pow(dT, 2))
    num = np.tanh(sqr*Td/(2*T))
    return num/sqr

X = np.array([-np.sqrt(1 / 3), np.sqrt(1 / 3)])
W = np.array([1, 1])


def gauss_legendre_integrate(f, X, W, T):
    sum = 0
    for i in range(len(X)):
        sum += W[i] * f(X[i], T)
    return sum

def temp(f, X, W, Td=300):
    T = np.arange(1, 20, 1e-4)
    for T_ in T:
        dT = 300*1,380649*(10**-23)*T_
        I = gauss_legendre_integrate(f, X, W, T_)/2
        if abs(I - 1 / 0.3) < 1e-3:
            print("entered")
            return T_
    return None

def temperaturas(f, X, W, Td=300):
    T = np.arange(1, 20, 1e-4)
    I = []
    for T_ in T:
        I.append(gauss_legendre_integrate(f, X, W, T_)/2)
    return I

I = temperaturas(ecuacion_banda_prohibida, X, W)
print(min(I), max(I))

np.