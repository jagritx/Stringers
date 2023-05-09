def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext


def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext
