"""
# filename:fastExponentialAlgorithm.py
# author:heizhou
# No.:150420226
# date:17/10/12
# purpose:This file is to achieve fast exponential algorithm
"""
import math

def fastCaculate(a, b, c):
    """fast exponential algorithm ==>> a^b mod c"""
    # turn b to bin,53==>>110101
    b_bin = bin(b)[2:]
    b_list = []
    for i in xrange(len(b_bin)):
        if b_bin[i] == '1':
            b_list.append(len(b_bin)-i-1)
    b_list.reverse()
    # repeated square operation
    result = 1
    for i in xrange(len(b_list)):
        if b_list[i] != 0:
            basal = a
            for i in range(b_list[i]):
                basal = pow(basal, 2) % c
            result = (result * basal) % c
        else:
            result = (result * (a % c))
    return result




