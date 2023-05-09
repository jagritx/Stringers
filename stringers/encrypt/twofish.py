from Crypto.Cipher import Twofish


def TWOFISH_GENERATE_KEY():
    # Generate a new Twofish key with a key length of 256 bits
    key = Twofish.new(key=b'This is a secret key.', mode=Twofish.MODE_ECB)

    # Return the key as a byte string
    return key


def TWOFISH_ENCODE(key, plaintext):
    # Create a new Twofish cipher with the given key and use ECB mode
    cipher = Twofish.new(key=key, mode=Twofish.MODE_ECB)

    # Encrypt the plaintext using the Twofish cipher
    ciphertext = cipher.encrypt(plaintext.encode())

    # Return the ciphertext as a byte string
    return ciphertext


def TWOFISH_DECODE(key, ciphertext):
    # Create a new Twofish cipher with the given key and use ECB mode
    cipher = Twofish.new(key=key, mode=Twofish.MODE_ECB)

    # Decrypt the ciphertext using the Twofish cipher
    plaintext = cipher.decrypt(ciphertext)

    # Return the decrypted plaintext as a string
    return plaintext.decode()
