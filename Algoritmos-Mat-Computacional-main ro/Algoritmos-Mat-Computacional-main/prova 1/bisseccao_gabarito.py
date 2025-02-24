import math



def bisseccao(f, a, b, e):
    i=0
    ai=a
    bi=b

    while abs(bi-ai) > e:
        pi = (ai+bi)/2
        print("a{}: {};  b{}: {};  p{}: {};".format(i,ai,i,bi,i,pi))
        if f(ai)*f(pi)<0:
            bi = pi
        else:
            ai = pi
        i+=1

    return (ai+bi)/2


bisseccao(lambda x:x**3-9*x+3, -4,-2, 0.000000001)
bisseccao(lambda x:x**3-9*x+3, 0,2, 0.000000001)
bisseccao(lambda x:x**3-9*x+3, 2,4, 0.000000001)
bisseccao(lambda x:math.sqrt(x)-5*math.exp(-x), 1,2, 0.000000001)
# bisseccao(lambda x:x*math.log10(x)-1, 2,3, 0.00000000001)

