from __future__ import print_function

import math
import numpy as np
import sys



def f(E, k_b, T):
    return 1.0/(np.exp(E/(k_b*T) + 1.0) 



def I_qp(z, N_l0, N_r0, e, T_lr, V, delta, k_b, T):
    """ I_qp we wish to integrate """
        E_k= z/(1-z)
    return N_l0*N_r0*2.0*np.pi*T_lr**2/h_bar*(f(E_k + e*V, k_b, T) - f(E_k, k_b, T))\
                    *(E_k+e*V)*E_k/(np.sqrt((E_k+e*V)**2 - delta**2)*np.sqrt(E_k**2 - delta**2)*(1- z**2))


def I_1():


def I_2():


def I_J():


def I_toatal():


def simp(a, b, I, N):
    """  do a Simpson's integration by breaking up the domain [a,b] into N
    slabs.  Note: N must be even, because we do a pair at a time """

    xedge = np.linspace(a, b, N+1)

    integral = 0.0

    if not N%2 == 0:
        sys.exit("ERROR: N must be even")

    delta = (xedge[1] - xedge[0])

    for n in range(0, N, 2):
        integral += (1.0/3.0)*delta*(I(xedge[n]) +
                                     4.0*I(xedge[n+1]) +
                                     I(xedge[n+2]))

    return integral



def main():
    """ loop over a number of resolutions and output the error """
    z=
    N_l0=
    N_r0=
    e=
    T_lr=
    V=
    delta=
    k_b=
    T=
   
    a = 0.0
    b = 1.0

    for N in [2, 4, 8, 16, 32, 64, 128]:
        t = simp(a, b, fun, N)
        e = t - I_exact(a, b)
        print(N, t, e)


if __name__ == "__main__":
    main()

