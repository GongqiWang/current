
import math
import numpy as np
import sys
import matplotlib.pyplot as plt


def f(E, k_b, T):
    return 1.0/(np.exp(E/(k_b*T)) + 1.0)

if __name__ == "__main__":

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

  E_k=np.linspace(-100.0, 100.0, 500)
  
  F=[]
    #print(E_k)
  for e_k in E_k:

        fermi=f(e_k, k_b, T)

        F.append(fermi)



  plt.plot(E_k, F)


  plt.savefig("fermi.png", dpi=150)

