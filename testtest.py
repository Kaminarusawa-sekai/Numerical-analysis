from sympy import *

def fFunc(x):
    y=pow(x,2)-4*x+3
    return y

def newtonDownhill(a):
    x=symbols('x')
    y=pow(x,2)-4*x+3
    diffFunc=diff(y,x)
    def downhillFactor(a,factor):
        b=a-factor*fFunc(a)/diffFunc.subs('x',a)
        if abs(b)>abs(a):
            factor=factor/2
            downhillFactor(a,factor)
        return factor
    def downhillNew(c):
        factor=downhillFactor(a,1)
        print(factor)
        c=c-factor*fFunc(c)/diffFunc.subs('x',c)
        print(c)
        if -0.0001>fFunc(c) or fFunc(c)>0.0001:
            c=downhillNew(c)
            #print(c)
        return c
    b=downhillNew(a)
    return b



b=newtonDownhill(2.1)
print(b)