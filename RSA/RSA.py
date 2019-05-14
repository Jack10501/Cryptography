"""Created by Jack Paull
RSA encryption and decryption in Python3.7"""
import numtheory
import sys
from random import randrange

# Global Vars
n = 0
e = 0
d = 0


def main():
    """Performs the general RSA code"""
    # Generate randomised prime keys
    key_a = numtheory.prime_gen()
    key_b = numtheory.prime_gen()
    print("Keys Generated: " + key_a + ", " + key_b)

    # Generate e, d, n and then pass into encrypt/decrypt
    calc_e_n(key_a, key_b)
    print("Values generated; N:" + str(n) + ", E: " + str(e) +
          ", D: " + str(d))
    # Perform encryption and then decryption
    encrypt()
    decrypt()


def encrypt():
    """Performs the RSA encrypt on a plain text"""
    # Open files
    try:
        in_file = open("test.txt", 'r', encoding="utf-8")
        out_file = open("testout.txt", 'w', encoding="utf-8")
    except IOError:
        print("IO Error encountered")
        sys.exit(1)

    # Encrypt files
    print("Encrypting: " + in_file.name + " to: " + out_file.name)
    while True:
        pt = 0
        for ii in range(2):
            c = in_file.read(1)
            if not c:
                in_file.close()
                out_file.close()
                print("Encryption of: " + in_file.name + " Complete")
                break
            # Perform encryption
            pt += ord(c) << ((1 - ii) << 3)

        # If nothing, ignore
        if pt != 0:
            ct = numtheory.modular_exponent(pt, e, n)
            for ii in range(4):
                c = ct >> ((3 - ii) << 3)
                out_file.write(c)


def decrypt():
    """Converts cipher text back into plain text"""
    # Open files
    try:
        in_file = open("testout.txt", 'r', encoding="utf-8")
        out_file = open("testnout.txt", 'w', encoding="utf-8")
    except IOError:
        print("IO Error encountered")
        sys.exit(1)

    # Decrypt files
    print("Decrypting: " + in_file.name + " to: " + out_file.name)
    while True:
        ct = 0
        for ii in range(4):
            c = in_file.read(1)
            if not c:
                in_file.close()
                out_file.close()
                print("Decryption of: " + in_file.name + " Complete")
                break
            # Perform decryption
            ct += ord(c) << ((3 - ii) << 3)

        # If nothing, ignore
        if ct != 0:
            pt = numtheory.modular_exponent(ct, d, n)
            for ii in range(2):
                c = pt >> ((1 - ii) << 3)
                if c != 0:
                    out_file.write(c)


def calc_e_n(key_a, key_b):
    """Generates the value for E to encrypt and value for D to decrypt and the modules n"""
    global n
    global e
    global d

    n = key_a * key_b

    tot_n = (key_a - 1) * (key_b - 1)

    while True:
        e = randrange(1, 32767) % tot_n
        if numtheory.gcd(e, tot_n) == 1:
            break

    d = numtheory.extended_gcd(e, tot_n)


if __name__ == '__main__':
    """Run RSA"""
    main()

