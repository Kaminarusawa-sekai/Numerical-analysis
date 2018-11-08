
from sympy import *
import types
def fFunc(x,fi=-100,bi=100): 
    if bi>=x>=fi:
        y=pow(x,2)-4*x+3
        return y
    else:
        raise ValueError

def derivative(a):
    #求导模块
    pass


def bis(fi=-100,bi=100):
    mid=(fi+bi)/2
    print(mid)
    #print(fFunc(mid)*fFunc(fi))
    if fFunc(fi)*fFunc(mid)<-0.0001:
        bis(fi,mid)
    elif -0.0001<fFunc(fi)*fFunc(mid)<0.0001:
        return mid
    else:
        bis(mid,bi)



def newton(a):
    x=symbols('x')
    y=pow(x,2)-4*x+3
    diffFunc=diff(y,x)
    def New(c):   
        c=c-fFunc(c)/diffFunc.subs('x',c)
        if -0.0001>fFunc(c) or fFunc(c)>0.0001:
            print("17:%s" %(c))
            c=New(c)
        print("19:%s" %c)
        return c
    b=New(a)
    return b

def newtonJustice():
    #newton迭代法的收敛性判断
    pass

#newton(2.5)

def simplifiedNewton(a):
    x=symbols('x')
    y=pow(x,2)-4*x+3
    diffFunc=diff(y,x)
    sN=diffFunc.subs('x',a)
    def simplifiedNew(c):   
        c=c-fFunc(c)/sN
        #print(c)
        if -0.1>fFunc(c) or fFunc(c)>0.1:
            c=simplifiedNew(c)
            print(c)
        return c
    b=simplifiedNew(a)
    return b



b=simplifiedNewton(2.5)
print(b)

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