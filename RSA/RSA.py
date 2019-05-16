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
    print("Keys Generated: " + str(key_a) + ", " + str(key_b))

    # Generate e, d, n and then pass into encrypt/decrypt
    calc_e_n(key_a, key_b)
    print("Values generated; N:" + str(n) + ", E: " + str(e) +
          ", D: " + str(d))

    # Attempt to open the files
    try:
        in_file = open("in.txt", 'r', encoding="utf-8")
        out_file = open("out.txt", 'w', encoding="utf-8")
    except IOError:
        print("IO Error encountered\n"
              "Please ensure all files are created before running\n"
              "Make sure in file is called in.txt and out is out.txt")
        sys.exit(1)

    # Perform encryption
    print("Encrypting: " + in_file.name + " to: " + out_file.name)
    while True:
        pt = in_file.read(1)
        if not pt:
            in_file.close()
            out_file.close()
            print("Encryption of: " + in_file.name + " Complete")
            break
        out_file.write(chr(encrypt(pt)))

    # Attempt to open the files
    try:
        in_file = open("out.txt", 'r',)
        out_file = open("nout.txt", 'w',)
    except IOError:
        print("IO Error encountered\n"
              "Please ensure all files are created before running\n")
        sys.exit(1)

    # Perform decryption
    print("Decrypting: " + in_file.name + " to: " + out_file.name)
    while True:
        ct = in_file.read(1)
        if not ct:
            in_file.close()
            out_file.close()
            print("Decryption of: " + in_file.name + " Complete")
            break
        out_file.write(chr(decrypt(ct)))


def encrypt(pt):
    """Performs the RSA encrypt on a plain text"""
    # Encrypt files
    ct = numtheory.modular_exponent(ord(pt), e, n)
    print(ct)
    return ct


def decrypt(ct):
    """Converts cipher text back into plain text"""
    # Decrypt files
    pt = numtheory.modular_exponent(ord(ct), d, n)
    return pt


def calc_e_n(key_a, key_b):
    """Generates the value for E to encrypt and value for D to decrypt and the modules n"""
    global n, e, d

    n = key_a * key_b

    tot_n = (key_a - 1) * (key_b - 1)

    while numtheory.gcd(e, tot_n) != 1:
        e = randrange(1, 32767) % tot_n

    d = numtheory.extended_gcd(e, tot_n)


if __name__ == '__main__':
    """Run RSA"""
    main()
