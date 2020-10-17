"""
RSA Decryption Algorithm
This code demonstrates how the RSA algorithm decrypts a given encrypted message by relying on mathematically proven
relations like Fermat's Little Theorem, Euler's Generalization of the little theorem, Euler's Phi Function, etc.

The decryption process is as follows:
    * receive em, d, and n
    * decrypt message using (em ^ d) % n

em : encrypted message (message received)
d :  decryption key
n : product of two primes
dm : decrypted message (should be the same as the original message)

--One improvement would be if the message could be decrypted without having to know n, just with the decryption key d.

"""

"""
    Decrypting a given character using the relation dm = (em ^ d) % n
    To deal with large integers, we do the modulo operation as we raise it to a power to keep the integers small
"""
def decryptChar(char, d, n):
    # write char as ascii int
    asc_char = ord(char)

    # step by step calculation
    dec_char = (asc_char * asc_char) % n
    for i in range(2, d):
        dec_char = (dec_char * asc_char) % n

    return chr(dec_char)


"""
    Decryption function
    Passes characters one at a time to the decryptChar function
"""
def decrypt(em, d, n):
    dec_str = ""

    # decrypt all characters
    for char in em:
        dec_char = decryptChar(char, d, n)
        dec_str += dec_char

    return dec_str


# Decryption

# ask for necessary values
em = input("Enter the encrypted message: ")
d = int(input("Enter d: "))
n = int(input("Enter n: "))

# decrypt
dm = decrypt(em, d, n)

# output
print("Decrypted message: " + dm)