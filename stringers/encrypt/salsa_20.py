from salsa20 import XSalsa20_xor
import os


def Salsa20_Encrypt(key, plaintext):
    # Generate a 24-byte (192-bit) nonce
    nonce = os.urandom(24)

    # Encrypt the plaintext using the XSalsa20 cipher
    ciphertext = XSalsa20_xor(plaintext, nonce, key)

    # Return the nonce and ciphertext as a tuple
    return nonce + ciphertext


def Salsa20_Decrypt(key, nonce_and_ciphertext):
    # Split the nonce and ciphertext
    nonce = nonce_and_ciphertext[:24]
    ciphertext = nonce_and_ciphertext[24:]

    # Decrypt the ciphertext using the XSalsa20 cipher
    plaintext = XSalsa20_xor(ciphertext, nonce, key)

    # Return the plaintext as a bytes object
    return plaintext
