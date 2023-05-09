from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def RSA_GENERATE_KEYS():
    # Generate a new RSA key pair with a key length of 2048 bits
    key = RSA.generate(2048)

    # Return the public and private keys as strings
    return key.publickey().export_key().decode(), key.export_key().decode()


def RSA_ENCODE(public_key_str, plaintext):
    # Import the public key from the given string
    public_key = RSA.import_key(public_key_str)

    # Create a new RSA cipher with the public key and use PKCS#1 OAEP padding
    cipher = PKCS1_OAEP.new(public_key)

    # Encrypt the plaintext using the RSA cipher
    ciphertext = cipher.encrypt(plaintext.encode())

    # Return the ciphertext as a base64-encoded string
    return ciphertext.hex()


def RSA_DECODE(private_key_str, ciphertext):
    # Import the private key from the given string
    private_key = RSA.import_key(private_key_str)

    # Create a new RSA cipher with the private key and use PKCS#1 OAEP padding
    cipher = PKCS1_OAEP.new(private_key)

    # Decrypt the ciphertext using the RSA cipher
    plaintext = cipher.decrypt(bytes.fromhex(ciphertext))

    # Return the decrypted plaintext as a string
    return plaintext.decode()
