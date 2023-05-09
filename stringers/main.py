from encrypt.rsa import RSA_GENERATE_KEYS, RSA_ENCODE, RSA_DECODE
public_key_str, private_key_str = RSA_GENERATE_KEYS()
plaintext = "Hello, world!"
ciphertext = RSA_ENCODE(public_key_str, plaintext)
print("Encrypted message:", ciphertext)
decrypted_text = RSA_DECODE(private_key_str, ciphertext)
print("Decrypted message:", decrypted_text)


""" 
Golomb done
huffman (Class) done returns byte array
rle done
tunstall done (Class)
arithmetic done (Counter)
dictionary based done
Advanced
shannonfano done
CABAC done
PPM done
ANS done
Delta done
BWT done

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
Easy
Twofish done
ElGamal done
'''
