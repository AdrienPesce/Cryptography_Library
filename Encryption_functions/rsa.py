#!/usr/bin/python3.5

# ################################################################################################################################
# 		 Notes
# ################################################################################################################################

'''

Module ras

Used to encrypte and decrypte message using ras algorithm

In this module, the functions availables are:
    - keys_creation
    - encryption
    - decryption

'''



# ################################################################################################################################
#       Import modules
# ################################################################################################################################

# Standard modules



# ################################################################################################################################
# 		 Functions
# ################################################################################################################################

# ################################################################
# 		 keys_creation
# ################################################################

def keys_creation(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = phi - 1
    while get_gcd(e, phi) != 1:
        e -= 1

    i = phi - 1
    x = 1 + i*phi
    while x % e != 0: 
        i -= 1
        x = 1 + i*phi
    d = int(x/e) 

    publicKey = (e, n)
    privateKey = (d, n)

    return publicKey, privateKey

def get_gcd(a, b):
    if b == 0:
        gcd = a
    else:
        r = a % b
        gcd = get_gcd(b, r)
    
    return gcd


# ################################################################
# 		 encryption
# ################################################################

def encryption(message, publicKey):
    e, n = publicKey
    messageEncrypted = message ** e % n
    return messageEncrypted


# ################################################################
# 		 decryption
# ################################################################

def decryption(message, privateKey):
    d, n = privateKey
    messageDecrypted = message ** d % n
    return messageDecrypted



# ################################################################################################################################
# 		 Main
# ################################################################################################################################

if __name__ == '__main__':
    publicKey, privateKey = keys_creation(37, 97)
    print(publicKey)
    print(privateKey)
    message = 808
    print(message)
    encrypted = encryption(message, publicKey)
    print(encrypted)
    decrypted = decryption(encrypted, privateKey)
    print(decrypted)


