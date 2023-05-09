def rc4(key, plaintext):
    # Key scheduling algorithm
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-random generation algorithm
    i = j = 0
    ciphertext = []
    for c in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        ciphertext.append(c ^ k)

    return bytes(ciphertext)


def rc4_encrypt(key, plaintext):
    return rc4(key, plaintext)


def rc4_decrypt(key, ciphertext):
    return rc4(key, ciphertext)
