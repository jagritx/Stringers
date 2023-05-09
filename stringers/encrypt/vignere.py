def vigenere_encrypt(plaintext, key):
    """
    Encrypts plaintext using Vigenère cipher with the given key.

    Args:
        plaintext (str): The plaintext to encrypt.
        key (str): The encryption key.

    Returns:
        str: The encrypted ciphertext.
    """
    ciphertext = ""
    key_idx = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_idx].upper()) - ord('A')
            cipher_char = chr(
                ((ord(char.upper()) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += cipher_char
            key_idx = (key_idx + 1) % len(key)
        else:
            ciphertext += char

    return ciphertext


def vigenere_decrypt(ciphertext, key):
    """
    Decrypts ciphertext using Vigenère cipher with the given key.

    Args:
        ciphertext (str): The ciphertext to decrypt.
        key (str): The decryption key.

    Returns:
        str: The decrypted plaintext.
    """
    plaintext = ""
    key_idx = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_idx].upper()) - ord('A')
            plain_char = chr(
                ((ord(char.upper()) - ord('A') - shift) % 26) + ord('A'))
            plaintext += plain_char
            key_idx = (key_idx + 1) % len(key)
        else:
            plaintext += char

    return plaintext
