from __future__ import print_function

import scipy.integrate as integrate
import scipy.special as special

import math
import numpy as np
import sys
import matplotlib.pyplot as plt


def f(E, k_b, T):
    if E/(k_b*T) > 1.0e3:
       return 0.0
    elif E/(k_b*T) < -1.0e3:
       return 1.0
    else:
       return 1.0/(np.exp(E/(k_b*T))+ 1.0)



def I_qp(z,V):
    """ I_qp we wish to integrate """
    e=1.0#1.6022e-19
    h_bar=1.0#6.582e-16
    T_lr=1.0e-5
    V_k=-1.0e-5
    delta=0.1#2.4e-4
    k_b=8.61733e-5
    T=4.0/11604.525
    h_bar_WD=300.0/11604.525
    N_l0=1.0/(V_k*np.log(delta/(h_bar_WD*2.0)))
    N_r0=1.0/(V_k*np.log(delta/(h_bar_WD*2.0)))
    

    E_k= z/(1-z**2)
    
    if (E_k-e*V)**2 > delta**2 and E_k**2 > delta**2:
            I_qp_i=np.absolute(E_k-e*V)*np.absolute(E_k)*(1+z**2)\
                     /(np.sqrt((E_k-e*V)**2 - delta**2)*np.sqrt(E_k**2 - delta**2)*(1- z**2)**2)*\
                       (f(E_k - e*V, k_b, T) - f(E_k, k_b, T))
            #print (f(E_k - e*V, k_b, T) - f(E_k, k_b, T))
            #print(I_qp_i)
    else:
            I_qp_i=0
            #print(I_qp_i)
    return I_qp_i


#def I_1():


#def I_2():



#def I_J():


#def I_toatal():


"""def trap(a, b, I_qp, N, V):
    #do a trapezoid integration by breaking up the domain [a,b] into N
    #slabs 
    xedge = np.linspace(a, b, N+1)

    integral = 0.0

    for n in range(N):
        integral += 0.5*(xedge[n+1] - xedge[n])*(I_qp(xedge[n], V) + I_qp(xedge[n+1], V))

    return integral



def simp(a, b, I_qp, N, V):
    #  do a Simpson's integration by breaking up the domain [a,b] into N
    #slabs.  Note: N must be even, because we do a pair at a time 

    xedge = np.linspace(a, b, N+1)

    integral = 0.0

    if not N%2 == 0:
        sys.exit("ERROR: N must be even")

    delta = (xedge[1] - xedge[0])
    #print(delta)
    for n in range(0, N, 2):
        integral += (1.0/3.0)*delta*(I_qp(xedge[n],V) +
                                     4.0*I_qp(xedge[n+1],V) +
                                     I_qp(xedge[n+2],V))
    #print(integral)
    return integral"""




if __name__ == "__main__":

    """ loop over a number of resolutions and output the error """
    a=-1.0
    b=1.0
    
    e=1.0#1.6022e-19
    T_lr=1.0
    V_k=-1.0
    delta=2.4e-4
    k_b=8.61733e-5
    T=4.0/11604.525
    h_bar_WD=300.0/11604.525
    N_l0=1.0/(V_k*np.log(delta/(h_bar_WD*2.0)))
    N_r0=1.0/(V_k*np.log(delta/(h_bar_WD*2.0)))


    I=np.zeros((100), dtype=np.float64)
    V=np.linspace(0.0, 0.4, 100)
    #print (V)
    i=0
    #print(i)
    for V_i in V:
        N=20000
        #print(N)
        
        I[i], err = integrate.quad(lambda z:I_qp(z, V_i), a,b)      #simp(a, b, I_qp, N, V_i)
        i +=1
        
    #print (I)

    plt.plot(V, I)


    plt.savefig("I_V.png", dpi=300)
