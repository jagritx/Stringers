from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes


def generate_key_3des():
    # Generate a new Triple DES key
    key = get_random_bytes(24)
    return key


def triple_des_encrypt(key, plaintext):
    # Pad the plaintext to a multiple of 8 bytes
    padded_plaintext = plaintext.encode().ljust(8 * ((len(plaintext) + 7) // 8))

    # Create a new Triple DES cipher with the key and use CBC mode
    cipher = DES3.new(key, DES3.MODE_CBC)

    # Encrypt the padded plaintext using the Triple DES cipher
    ciphertext = cipher.iv + cipher.encrypt(padded_plaintext)

    # Return the ciphertext as a base64-encoded string
    return ciphertext.hex()


def triple_des_decrypt(key, ciphertext):
    # Convert the ciphertext from a base64-encoded string to bytes
    ciphertext = bytes.fromhex(ciphertext)

    # Extract the initialization vector from the ciphertext
    iv = ciphertext[:DES3.block_size]

    # Create a new Triple DES cipher with the key and use CBC mode
    cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)

    # Decrypt the ciphertext using the Triple DES cipher and remove padding
    plaintext = cipher.decrypt(
        ciphertext[DES3.block_size:]).rstrip(b"\0").decode()

    # Return the decrypted plaintext as a string
    return plaintext
