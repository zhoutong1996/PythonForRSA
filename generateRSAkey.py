"""
# filename:generateRSAkey.py
# author:heizhou
# No.:150420226
# date:17/10/12
# purpose:This file is to generate a RSA key
"""
from generateBigPrime import generatePrime as GP

def generateKey():
    """generate n,e and n,d"""
    p = GP()
    q = GP()
    while(p == q):
        q = GP()
    n = p*q
    e = 0
    m = (p-1)*(q-1)
    for i in xrange(int(m**(1./4)), m):
        if gcd(m, i) == 1:
            e = i
            break
    d = getInverse(e, m)
    return {'publicKey': [n, e], 'privateKey': [n, d]}


def getInverse(e, m):
    """seeking inverse ==>> e*d mod m = 1"""
    x1 = 1
    x2 = 0
    x3 = m
    y1 = 0
    y2 = 1
    y3 = e
    while y3 != 1:
        q = int(x3 / y3)
        t1 = x1 - q * y1
        t2 = x2 - q * y2
        t3 = x3 - q * y3
        x1 = y1
        x2 = y2
        x3 = y3
        y1 = t1
        y2 = t2
        y3 = t3
    return y2 % m


def gcd(a, b):
    """judge if a and b is coprime
"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)





