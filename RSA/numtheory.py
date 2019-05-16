"""Created by Jack Paull
A re-written python3.7 implementation of GCD and Extended
GCD used in Affine cipher previously written in C"""
from random import randrange

import constant


def gcd(a, b):
    """Checks if two keys are co prime to each other
    If so; returns 1 otherwise returns 2 for invalid
    """
    if a == 0:
        return b
    # Else, mod b by a and check if equal on next call
    return gcd(b % a, a)


def extended_gcd(a, n):
    """Extended Euclidean Algorithm to find the inverse
    of A
    """
    t = 0
    # Leave n as it is needed if t becomes a negative
    r = n
    q = 0
    # Temp Values for transitions/loops
    temp = 0
    next_t = 1
    next_r = a

    # Check if the key is not a co prime
    if gcd(a, n) != 1:
        return -1

    # Loop to find the inverse
    while next_r != 0:
        # Get the quotient each time
        # First time is alphabet / key
        q = r / next_r
        temp = t  # 0
        t = next_t  # 1
        next_t = temp - (q * next_t)
        # Now repeat for r
        temp = r
        r = next_r
        next_r = temp - (q * next_r)

    # Ensure the value doesnt end up as a negative
    if t < 0:
        t = t + n

    # Return the found inverse
    return t


def prime_check(given_num):
    """Calculates if a number is prime to some confidence level"""
    is_prime = True
    ran = randrange(1, 32767)

    for ii in range(constant.PRIME_TESTS):
        a = (ran % given_num) + 1
        exponent = (given_num - 1) >> 1
        r = modular_exponent(a, exponent, given_num)

        # If r isn't 1 or -1 then it's 100% not prime
        if not ((r == 1) or (r == (given_num - 1))):
            return False

    # Otherwise can't prove that it isn't
    return is_prime


def modular_exponent(base, exponent, mod):
    """Calculates the value base^exponent % mod efficiently"""
    result = 1
    base = base % mod

    # Ensure number is below upper limit
    if (base > constant.LIMIT) or (exponent > constant.LIMIT) or (mod > constant.LIMIT):
        return -1

    # Review exponents loop
    while exponent > 0:
        # Check the least significant bit
        if exponent & 1:
            result = (result * base) % mod

        # After check now shift to check next bit
        exponent >>= 1
        base = (base * base) % mod

    return result


def prime_gen():
    """Generates a new random prime between 1000 and 10000"""
    while True:
        prime = (randrange(1, 32767) % (constant.UPPER_LIMIT - constant.LOWER_LIMIT)) + constant.LOWER_LIMIT

        # loop till we find a prime
        if prime_check(prime):
            return prime
