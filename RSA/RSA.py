import numtheory
import sys


def main():
    """Performs the general RSA code"""
    key_a = int(input("Please enter the first key: \n"))
    key_b = int(input("Please enter the second key: \n"))

    # Initially we'll choose our own primes
    if key_a < 1000 or key_a > 10000 or key_b < 1000 or key_b > 10000:
        print("Invalid keys, please choose prime numbers between 1000-10 000")
        return 1
    if not (numtheory.prime_check(key_a) or numtheory.prime_check(key_b)):
        print("Invalid keys, please choose prime numbers between 1000-10 000")
        return 1

    encrypt(key_a, key_b)
    decrypt(key_a, key_b)


def encrypt(key_a, key_b):
    """Performs the RSA encrypt on a plain text"""
    # Open files
    try:
        in_file = open("test.txt", 'r', encoding="utf-8")
        out_file = open("testout.txt", 'w', encoding="utf-8")
    except IOError:
        print("IO Error encountered")
        sys.exit(1)

    while True:



def decrypt(key_a, key_b):
    """Converts cipher text back into plain text"""
    # Open files
    try:
        in_file = open("testout.txt", 'r', encoding="utf-8")
        out_file = open("testnout.txt", 'w', encoding="utf-8")
    except IOError:
        print("IO Error encountered")
        sys.exit(1)


if __name__ == '__main__':
    """Run RSA"""
    main()

