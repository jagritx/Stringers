from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def AES_ENCODE(key, plaintext):
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(AES.block_size)

    # Create a new AES cipher with the given key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encrypt the plaintext using the AES cipher in CBC mode with PKCS7 padding
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))

    # Combine the IV and ciphertext into a single byte string
    encoded = iv + ciphertext

    # Return the encoded byte string
    return encoded


def AES_DECODE(key, encoded):
    # Extract the IV and ciphertext from the encoded byte string
    iv = encoded[:AES.block_size]
    ciphertext = encoded[AES.block_size:]

    # Create a new AES cipher with the given key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext using the AES cipher in CBC mode with PKCS7 padding
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    # Return the decrypted plaintext as a string
    return plaintext.decode()
