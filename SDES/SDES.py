"""Created by Jack Paull
SDES encryption algorithm with components that have been adapted from stack exchange"""
import sys

"""Const Parameters"""
P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8 = (6, 3, 7, 4, 8, 5, 10, 9)
P4 = (2, 4, 3, 1)

IP = (2, 6, 3, 1, 4, 8, 5, 7)
IPi = (4, 1, 3, 5, 7, 2, 8, 6)

EP = (4, 1, 2, 3, 2, 3, 4, 1)

S0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
     ]

S1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
     ]


def permutation(original_key, perm):
    """Perform one of the permutations on the given key"""
    new_key = ''
    for ii in perm:
        new_key += original_key[ii-1]
    return new_key


def get_left(bits):
    """Access bits, div the length by two
    to reach the middle, then cut all bits
    after the centre"""
    return bits[:int(len(bits)/2)]


def get_right(bits):
    """As above but now cut all bits before
    the center"""
    return bits[int(len(bits)/2):]


def shift(bits):
    """Performs lshift"""
    rot_left_half = get_left(bits)[1:] + get_left(bits)[0]
    rot_right_half = get_right(bits)[1:] + get_right(bits)[0]
    return rot_left_half + rot_right_half


def key1(key):
    """Returns the first key after P10 and P8"""
    return permutation(shift(permutation(key, P10)), P8)


def key2(key):
    """Returns the second key after P10, P8 and P8"""
    return permutation(shift(shift(shift(permutation(key, P10)))), P8)


def xor(bits, key):
    """Performs a xor within f_k"""
    new = ''
    for bit, key_bit in zip(bits, key):
        new += str(((int(bit) + int(key_bit)) % 2))
    return new


def sbox(bits, sb):
    """Formatting for S Boxes"""
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return '{0:02b}'.format(sb[row][col])


def f_k(bits, key):
    """Retrieve left half"""
    left = get_left(bits)
    """Retrieve right half"""
    right = get_right(bits)
    bits = permutation(right, EP)
    """Perform XOR taking in bits and 8bit k2"""
    bits = xor(bits, key)
    """Split key after XOR and apply 
    appropriate S-boxes"""
    bits = sbox(get_left(bits), S0) + sbox(get_right(bits), S1)
    """Perform P4 permutation"""
    bits = permutation(bits, P4)
    return xor(bits, left)


def switch(bits, temp):
    """Performs the switch between the right and left bits"""
    return get_right(bits) + temp


def encrypt(pt, key):
    """Perform initial IP before fk"""
    bits = permutation(pt, IP)
    """First fk taking in k1"""
    temp = f_k(bits, key1(key))
    bits = switch(bits, temp)
    """Second fk taking in k2"""
    bits = f_k(bits, key2(key))
    """Change the binary number to an int ascii value and then to a 
    char based on that value and return"""
    return chr(int(permutation(bits + temp, IPi), 2))


def decrypt(ct, key):
    """Perform initial IP before fk"""
    bits = permutation(ct, IP)
    """First fk taking in k2"""
    temp = f_k(bits, key2(key))
    bits = switch(bits, temp)
    """second fk taking in k1"""
    bits = f_k(bits, key1(key))
    """Change the binary number to an int ascii value and then to a 
    char based on that value and return"""
    return chr(int(permutation(bits + temp, IPi), 2))


def bin_con(st):
    """Converts a string into a binary string"""
    new_st = ''.join(format(ord(x), 'b') for x in st)
    if len(new_st) != 8:
        new_st = new_st.rjust(8, '0')
    return new_st


def str_con(bi):
    """Converts a binary value to its character"""
    print(''.join(format(ord(bi), 'c')))


def key_con(key):
    """Places the key within bounds by modding it by 256 to ensure 8 bits then
    Converts the given key to a binary number"""
    """rjust() forces the key to be 10 bits and pads with 0's at the start"""
    temp_key = 0
    for ii in key:
        temp_key = temp_key + ord(ii)
    """Ensures it's within 8 bits, this allows us to take in any key"""
    temp_key = temp_key % 256
    """Now format the key in binary"""
    new_key = ''.join(format(temp_key, 'b'))
    """Pad the key"""
    if len(new_key) != 10:
        new_key = new_key.rjust(10, '0')
    return new_key


def main():
    """Checking args are correct"""
    if len(sys.argv) != 5:
        print("Please enter correct values\n"
              "SDES.py <mode> <key> <inFile> <outFile>\n"
              "Modes: -e: Encrypt, -d: decrypt\n"
              "Key: any combination of keyboard characters (NO SPACE)\n"
              "File: Files MUST be created before running for optimal results")
        sys.exit(1)

    """Assign Vars"""
    mode = sys.argv[1]
    key = sys.argv[2]

    """Convert and pad key for 10 bits"""
    key = key_con(key)
    """Attempt to open the files"""
    try:
        in_file = open(sys.argv[3], 'r', encoding="utf-8")
        out_file = open(sys.argv[4], 'w', encoding="utf-8")
    except IOError:
        print("IO Error encountered\n"
              "Please ensure all files are created before running")
        sys.exit(1)

    """Check if the mode is to encrypt or decrypt"""
    if mode == "-e":
        while True:
            pt = in_file.read(1)
            if not pt:
                in_file.close()
                out_file.close()
                print("Encryption of: " + in_file.name + " Complete")
                break
            bin_pt = bin_con(pt)
            out_file.write(encrypt(bin_pt, key))
    elif mode == "-d":
        while True:
            ct = in_file.read(1)
            if not ct:
                in_file.close()
                out_file.close()
                print("Decryption of: " + in_file.name + " Complete")
                break
            bin_ct = bin_con(ct)
            out_file.write(decrypt(bin_ct, key))


if __name__ == '__main__':
    main()
