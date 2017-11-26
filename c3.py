from __future__ import print_function

import math
import numpy as np
import sys
import matplotlib.pyplot as plt



def f(E, k_b, T):
    return 1.0/(np.exp(E/(k_b*T) + 1.0))


z=0.5
V=0.01


e=1.0#1.6022e-19
h_bar=1.0#6.582e-16
T_lr=1.0#1.0e-5
V_k=-1.0#e-5
delta=1.0#2.4e-4
k_b=1.0#8.61733e-5
T=1.0#4.0/11604.525
h_bar_WD=300.0/11604.525
N_l0=1.0/(V_k*np.log(delta/(h_bar_WD*2.0)))
N_r0=1.0/(V_k*np.log(delta/(h_bar_WD*2.0)))
    
    

E_k= z/(1-z)

D=[]

E_k=np.linspace(-4.0, 4.0, 500)
#print(E_k)
for e_k in E_k:
  if e_k<0:
    if e_k**2 > delta**2:
          d=np.absolute(e_k-e*V)*np.absolute(e_k)\
                     /(np.sqrt((e_k-e*V)**2 - delta**2)*np.sqrt(e_k**2 - delta**2))
          D.append(d)
    else:
       d=0
       D.append(d)
  else:
     if e_k**2 > delta**2:
       d=(e_k+e*V)*e_k/(np.sqrt((e_k+e*V)**2 - delta**2)*np.sqrt(e_k**2 - delta**2))
       D.append(d)
     else:
       d=0
       D.append(d)
  
#print(D)


"""if e_k**2 > delta**2:
            I_qp_i=N_l0*N_r0*2.0*np.pi*T_lr**2/h_bar*(E_k+e*V)*E_k/(np.sqrt((E_k+e*V)**2 - delta**2)*np.sqrt(E_k**2 - delta**2)\
                                  *(1- z**2))*(f(E_k + e*V, k_b, T) - f(E_k, k_b, T)) 
            #print(I_qp_i)
else:
            I_qp_i=0"""

plt.plot(E_k, D)


plt.savefig("density of sate1.png", dpi=150)
