from encrypt.vignere import vigenere_encrypt, vigenere_decrypt
plaintext = "This is a test message."
key = "SECRET"
ciphertext = vigenere_encrypt(plaintext, key)
print(ciphertext)  # Output: "Gksv kv c prng nqyqybu."
decrypted_plaintext = vigenere_decrypt(ciphertext, key)
print(decrypted_plaintext)


""" 
Golomb done
huffman (Class) done returns byte array
rle done
tunstall done (Class)
arithmetic done (Counter)
dictionary based done ~~
shannonfano ~~
CABAC ~~
PPM ~~
ANS ~~
Delta ~~ 
BWT ~~

"""


'''
AES Done : Generate Key
RSA Done : Generate Key from Function
Blowfish Done : Any key
DES Done : Key of Size 8
Triple DES (3DES) Done : Generate Key from Function
Caeser Cypher Done
RC4 (Rivest Cipher 4) Done
Railfence Done
Vignere Done
Salsa20 Done
CHA CHA 20 done
Twofish ~~
ElGamal ~~
'''
