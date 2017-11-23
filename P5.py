# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:08:31 2017

@author: M K Shrimali
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
matplotlib.rcParams['xtick.top'] = 'True'
matplotlib.rcParams['ytick.right'] = 'True'
matplotlib.rcParams['grid.linestyle'] = '--'

t=np.linspace(0.,100,1000)
epsilon=0.01

def func(y,t,epslon):
    u,ud=y
    return [ud,-u-epslon*ud*abs(ud)]
u0=[0.,1]

sol=odeint(func,u0,t,args=(epsilon,))

plt.figure()
plt.plot(t,sol[:,0],label=r'${\bf u}(t)$')
plt.xlabel(r'$t$',fontsize=18)
plt.ylabel(r'$u(t)$')#,\dot{y}(t)$',fontsize=18)
plt.legend(loc=0)
plt.xlim([0.,t.max()])
plt.title(r'$\varepsilon$ = {}'.format(epsilon))
plt.figure(figsize=(6,6))
plt.plot(sol[:,0],sol[:,1])