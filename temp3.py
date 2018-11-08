class MathFunc(object):
    def __init__(self, args):
        self._funcs = []
        for key, value in args.items():
            if type(value) == type(0) or type(value) == type(0.0) and type(key) == type(0):
                temp = lambda x, key=key, value=value: value * pow(x, key)
                self._funcs.append(temp)

    def value(self, x):
        result = 0
        for func in self._funcs:
            result += func(x)

        return result

class FuncRoot(object):
    @classmethod
    def bisection(cls, math_func, fi, bi, ep=1e-5):
        mid=(fi + bi) / 2
        print(mid)
        if math_func.value(fi) * math_func.value(mid) < -ep:
            cls.bisection(math_func, fi, mid)
        elif -ep < math_func.value(fi) * math_func.value(mid) < ep:
            return mid
        else:
            cls.bisection(math_func, mid, bi)
            

args = {
    0: 3,
    1: -4,
    2: 1
}
y = MathFunc(args)
print(FuncRoot.bisection(y,-100,100))
