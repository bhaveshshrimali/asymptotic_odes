# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:56:14 2017

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

t=np.linspace(0.,10,1000)
epsilon=0.1
Alp=1.

def func(u,t,epslon,alph):
    y,ydot=u
    return [ydot,1./epslon*(-epslon*alph*ydot-y-epslon*y**3)]

def fex(t):
    return np.sqrt(epsilon)*np.exp(-Alp*t/2.)*np.sin(t/np.sqrt(epsilon))

y0=[0.,1.]

sol=odeint(func,y0,t,args=(epsilon,Alp))
plt.figure()
plt.plot(t,sol[:,0],label=r'${\bf y}(t)$')
#plt.plot(t,sol[:,1],'--',label=r'${\bf \dot{y}}(t)$')
plt.plot(t,fex(t),label=r'${\bf y}_e(t)$')
plt.xlabel(r'$t$',fontsize=18)
plt.ylabel(r'$y(t)$')#,\dot{y}(t)$',fontsize=18)
plt.legend(loc=0)
plt.xlim([0.,t.max()])
plt.title(r'$\varepsilon$ = {}'.format(epsilon))
