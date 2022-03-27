import matplotlib.pyplot as plt
import math as m
import numpy as np
def RLC(A, t):
    Vc, x = A
    V = 1.0
    R=10
    L=20
    C=0.05
    v =20 * m.sin(20 * t)

    np.odeint(i1 = v/R)
    np.odeint(i2 = C * Vc)
    np.odeint(Vc = L + V)

    plt.plot(i1, linewidth=2, linestyle='solid',  color='black', label='I1')
    plt.plot(i2,  linewidth=2,  linestyle='dashed', color='black', label='I2')
    plt.plot(v, linewidth=2, linestyle='dotted', color='black', label='v')
    plt.xlabel('a')
    plt.ylabel('T')
    plt.legend()
    plt.grid(axis='both')
    plt.tick_params(axis='both', direction='in', grid_linewidth=1, grid_linestyle='dashed', grid_alpha=0.5)
    plt.show()