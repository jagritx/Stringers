from Crypto.Cipher import Blowfish
from Crypto import Random
import base64


def BLOWFISH_ENCODE(key, plaintext):
    # Generate a random 8-byte initialization vector
    iv = Random.new().read(Blowfish.block_size)

    # Create a new Blowfish cipher with the given key and IV
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)

    # Pad the plaintext to be a multiple of 8 bytes
    plaintext = plaintext.encode()
    plaintext += b"\0" * (8 - len(plaintext) % 8)

    # Encrypt the plaintext using the Blowfish cipher
    ciphertext = cipher.encrypt(plaintext)

    # Combine the IV and ciphertext into a single message
    message = iv + ciphertext

    # Return the message as a base64-encoded string
    return base64.b64encode(message).decode()


def BLOWFISH_DECODE(key, ciphertext):
    # Decode the ciphertext from base64
    ciphertext = base64.b64decode(ciphertext)

    # Extract the IV from the message
    iv = ciphertext[:Blowfish.block_size]

    # Create a new Blowfish cipher with the given key and IV
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)

    # Decrypt the ciphertext using the Blowfish cipher
    plaintext = cipher.decrypt(ciphertext[Blowfish.block_size:])

    # Remove any padding from the plaintext
    plaintext = plaintext.rstrip(b"\0")

    # Return the decrypted plaintext as a string
    return plaintext.decode()
