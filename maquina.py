from math import log
from numpy import random
import numpy as np
from random import random
from statistics import mean,stdev

def fun():
    def f(alfa):
        return (-1/alfa)*log(random())    

    infi=1000000
    alfa=1/50    
    beta=1/5    
    n=5         
    s=3         
    infi=1000000
    disp=s      
    td=[]       
    for i in range(n):
        td.append(f(alfa))
    tdp=min(td)   
    tsp=infi     
    l=0         
    indicador=0
    cuenta=0
    while indicador==0:
        t=min(tdp,tsp)   
        if tdp==tsp:
            print("Cuidado")
        if t==tdp:
            if disp==0:
                indicador=1
                k=td.index(tdp)    
            else:
                disp=disp-1        
                l=l+1              
                k=td.index(tdp)    
                td[k]=t+f(alfa)
                
                if tdp>90:
                    return 1
                
                if l==1:
                    tsp=t+f(beta)
                
                    if tsp>90:
                        return 1
                    
                tdp=min(td)
        else:
            l=l-1
            disp=disp+1
            if l>0:
                tsp=t+f(beta)
            
            
            else:
                tsp=infi
    return 3


cuenta=0
n=100000
for i in range(n):
    x=fun()
    if x==1:
        cuenta+=1

print(cuenta/n)