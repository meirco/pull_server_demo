def mult(a, b):
    if b == 0:
        return 0
    return a + mult(a, b-1)


def pow(d,e):
    if e == 0:
        return 1
    if e == 1:
        return d
    return mult(d, pow(d, e-1))


if __name__ == '__main__':
    c = pow(2,3)
    print(c)
    print('it was good thing ')
