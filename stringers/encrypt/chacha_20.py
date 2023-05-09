from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


def CHACHA20_GENERATE_KEY():
    # Generate a 256-bit (32-byte) random key
    key = os.urandom(32)

    # Return the key as a bytes object
    return key


def CHACHA20_ENCODE(key, plaintext):
    # Generate a random 96-bit (12-byte) nonce
    nonce = os.urandom(12)

    # Create a CHACHA20 cipher with the given key and nonce
    cipher = Cipher(algorithms.ChaCha20(key, nonce),
                    mode=None, backend=default_backend())

    # Create an encryptor object with the cipher and use it to encrypt the plaintext
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Return the ciphertext and nonce as bytes objects
    return ciphertext, nonce


def CHACHA20_DECODE(key, nonce, ciphertext):
    # Create a CHACHA20 cipher with the given key and nonce
    cipher = Cipher(algorithms.ChaCha20(key, nonce),
                    mode=None, backend=default_backend())

    # Create a decryptor object with the cipher and use it to decrypt the ciphertext
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Return the plaintext as a bytes object
    return plaintext
