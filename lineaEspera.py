from math import log
from numpy import random
import numpy as np
from random import random
from statistics import mean,stdev

def linea(l_l,l_s,T):
    tl=0
    inf=1000000000
    ts=inf
    t=0
    l=0
    k=0
    while t<T:
        t=min(tl,ts)
        if t==tl:
            l=l+1
            k=(k+1)-1
            tl=t-(1/l_l)*log(random())
            if l==1:
                k=0
                ts=t-(1/l_s)*log(random()) 
        else:
            l=l-1
            k=l-2
            if l==0:
                ts=inf
            else:
                ts=t-(1/l_s)*log(random())
    return k
T=100
l_l=1.5
l_s=1.6
N=100000
esp=0
for i in range(N):
    esp=esp+linea(l_l,l_s,T)
print(esp/N)