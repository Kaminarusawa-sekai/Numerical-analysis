# _*_ coding:utf-8 _*_
def Solve(func):
    def wrapper(*args,**kw):
        print(Bisection(func,func.fi,func.bi))
        return func(*args,**kw)
    return wrapper


def Bisection(func,fi,bi):
    mid=(fi+bi)/2
    if (func(fi)*func(mid))+0.0001<0:
        Bisection(func,fi,mid)
    elif -0.0001<func(fi)*func(mid)<0.0001:
        return mid
    else:
        Bisection(func,mid,bi)


@Solve
def fFunc(a,fi=-100,bi=100):
    f=fi
    b=bi
    if bi>a>fi:
        y=pow(a,2)+a*7+4
        print('y')
        return y
    else:
        raise ValueError

fFunc(1)


def bis(fi=-100,bi=100):
    mid=(fi+bi)/2
    if (fFunc(fi)*fFunc(mid))+0.0001<0:
        bis(fi,mid)
    elif -0.0001<fFunc(fi)*fFunc(mid)<0.0001:
        return mid
    else:
        bis(mid,bi)

print(bis)