"""Created by Jack Paull
A re-written python3.7 implementation of GCD and Extended
GCD used in Affine cipher previously written in C"""


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


if __name__ == '__main__':
    """Only gcd() needs to be used to prove Q1
    """
    print(gcd(7, 26))
    print(gcd(26, 7 % 26))

