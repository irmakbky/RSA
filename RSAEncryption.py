"""
RSA Encryption Algorithm
This code demonstrates how the RSA algorithm encrypts a given message by relying on mathematically proven relations
like Fermat's Little Theorem, Euler's Generalization of the little theorem, Euler's Phi Function, etc.

The encryption process is as follows:
    * choose two prime numbers p and q
    * let n = p * q
    * let phi(n) be the number of integers up to n that are relatively prime to n (I prove in the paper that this in
        our case is (p - 1) * (q - 1)
    * choose e such that gcd(e, n) = 1 and 1 <= e <= phi(n)
    * choose d such that e * d = 1 (mod phi(n))
    * encrypt message using (m ^ e) % n

p , q : primes
n : product of primes
e : encryption key
d : decryption key
m : original message
em: encrypted message

"""

import random
from math import *

"""
    Finding the Greatest Common Divisor
    should return 1 if two numbers are relatively prime
"""
def gcd(i, num):
    while num != 0:
        r = i % num
        i = num
        num = r

    return i


"""
    Returns True if num is prime, False if not
    For the purposes of the assignment, we're checking if all numbers before num are relatively prime with num,
        and only then returning True
"""
def isPrime(num):
    for i in range(1, num):
        if gcd(i, num) != 1:
            return False

    return True


"""
    Creates a list of lists with two elements representing the possible values for e and d such that they satisfy
        e * d = 1 (mod phi(n))
    Then chooses one pair of values at random
"""
def findEandD(phin, n):
    values_lst = []

    for e in range(2, phin):
        if gcd(e, n) == 1:
            for k in range(1, 100):
                d = ((k * phin) + 1) / e
                if d < n and (floor(d) == ceil(d)):
                    values_lst.append([e, int(d)])

    return random.choice(values_lst)


"""
    Encrypting a given character using the relation em = (m ^ e) % n
    To deal with large integers, we do the modulo operation as we raise it to a power to keep the integers small
"""
def encryptChar(char, e, n):
    #  write char as ascii int
    asc_char = ord(char)

    # step by step calculation
    enc_char = (asc_char * asc_char) % n
    for i in range(2, e):
        enc_char = (enc_char * asc_char) % n

    return chr(enc_char)


"""
    Encryption function
    Passes characters one at a time to the encryptChar function
"""
def encrypt(message, e, n):
    enc_str = ""

    # encrypt all characters
    for char in message:
        enc_char = encryptChar(char, e, n)
        enc_str += enc_char

    return enc_str


# ask the user for p and q and check if they are prime
p = int(input("Enter the first prime: "))
q = int(input("Enter the second prime: "))

if (not isPrime(p)) or (not isPrime(q)):
    print("Wrong input")
# else, keep going

# calculate n and phi n
n = p * q
phin = (p - 1) * (q - 1)  # as proved in the paper, phi(n) = (p-1)*(q-1) where n = p * q

# ask the user for the message
m = input("Enter your message: ")

# choose e and d
ed_lst = findEandD(phin, n)
e = ed_lst[0]
d = ed_lst[1]

# Encryption
em = encrypt(m, e, n)

# output
print("Encrypted message: " + em)
print("n: " + str(n))
print("d: " + str(d))
