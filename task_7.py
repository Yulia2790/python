
def fact(n):
    new = (el * fact(n-1) for el in fact(n))
    for el in new:
        yield el


