"""
# filename:generateBigPrime.py
# author:heizhou
# No.:150420226
# date:17/10/12
# purpose:This file is to generate big prime,using miller-rabin algorithm
"""
import random
import math

trial_times = 5  # times of miller-rabin trial
prime_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def generatePrime():
    """generate two big prime"""
    while(1):
        option = random.randrange(1000000, 10000000)
        #  compare with prime under 100 to quicklu find out composite number
        judge = 0
        for i in range(len(prime_under_100)):
            if option%prime_under_100[i] == 0:
                break
            judge = i
        if judge < len(prime_under_100)-1:
            continue
        # miller-rabin test
        if isPrime(option) != 1:
            continue
        else:
            return option



def isPrime(option):
    """judge if option is a big prime,using miller-rabin algorithm"""
    for i in range(trial_times):
        a = random.randrange(2, option-1)
        if pow(a, option-1, option) != 1:
            return 0
    return 1


def xnModP(option, u, p):
    """Fermat judge"""
    result = 1
    u_bin = bin(u)[2:]
    for i in range(0, len(u_bin)):
        result = result**2 % p
        if u_bin[i] == '1':
            result = result*option % p
    return result






