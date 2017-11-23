# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:05:55 2017

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
Alph=1.
epsilon=0.001

def func(u,t):
    y,ydot=u
    return [ydot,(-y-4*ydot**2*y)/(1+4*y**2)]

def fex(t):
    return epsilon*np.cos(t)
y0=[epsilon,0.]

sol=odeint(func,y0,t)


plt.figure()
plt.plot(t,sol[:,0],label=r'${\bf y}(t)$')
#plt.plot(t,sol[:,1],'--',label=r'${\bf \dot{y}}(t)$')
plt.plot(t,fex(t),label=r'${\bf y}_e(t)$')
plt.xlabel(r'$t$',fontsize=18)
plt.ylabel(r'$y(t)$')#,\dot{y}(t)$',fontsize=18)
plt.legend(loc=0)
plt.xlim([0.,t.max()])
plt.title(r'$\varepsilon$ = {}'.format(epsilon))
