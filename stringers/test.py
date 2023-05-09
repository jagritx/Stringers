from encrypt.tripledes import generate_key_3des, triple_des_decrypt, triple_des_encrypt
key = generate_key_3des()
# Encrypt a message using the key
plaintext = "This is a secret message"
ciphertext = triple_des_encrypt(key, plaintext)
print("Ciphertext:", ciphertext)
# Decrypt the ciphertext using the key
decrypted_plaintext = triple_des_decrypt(key, ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)
