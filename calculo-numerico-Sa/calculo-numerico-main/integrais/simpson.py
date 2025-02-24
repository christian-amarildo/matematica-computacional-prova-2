def simpson(f, a: float, b: float, div: int=100):
    h = (b - a)/(div - 1)
    k = 0
    x = a + h
    for _ in range(1, div//2 + 1):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    for _ in range(1, div//2):
        k += 2*f(x)
        x += 2*h
    
    return (h/3)*(f(a)+f(b)+k)
