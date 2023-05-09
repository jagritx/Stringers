from Crypto.Cipher import DES


def DES_ENCODE(key, plaintext):
    # Pad the plaintext to a multiple of 8 bytes
    padded_plaintext = plaintext + \
        ((8 - len(plaintext) % 8) * chr(8 - len(plaintext) % 8)).encode()

    # Create a new DES cipher with the given key and use CBC mode
    cipher = DES.new(key, DES.MODE_CBC)

    # Encrypt the padded plaintext using the DES cipher
    ciphertext = cipher.iv + cipher.encrypt(padded_plaintext)

    # Return the ciphertext as a hex-encoded string
    return ciphertext.hex()


def DES_DECODE(key, ciphertext):
    # Convert the hex-encoded ciphertext to bytes
    ciphertext_bytes = bytes.fromhex(ciphertext)

    # Extract the initialization vector from the ciphertext
    iv = ciphertext_bytes[:8]

    # Extract the ciphertext without the initialization vector
    ciphertext_without_iv = ciphertext_bytes[8:]

    # Create a new DES cipher with the given key, use CBC mode, and set the initialization vector
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)

    # Decrypt the ciphertext using the DES cipher
    plaintext = cipher.decrypt(ciphertext_without_iv)

    # Unpad the plaintext
    plaintext = plaintext[:-plaintext[-1]]

    # Return the decrypted plaintext as a string
    return plaintext.decode()
