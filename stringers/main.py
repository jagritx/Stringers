from compress.rle import rle_encode, rle_decode

s = 'jkejdjksbcbbbbbeeeeeeeeeoieoifoidfndkdaaaaaaaaaaaaaaaaaaaaaaakkkkkkkkkksnsjshdjjjjjjkjjjjfccccccccccccccciii'
encoded = rle_encode(s)
print(encoded, rle_decode(encoded))


# Golomb done
# huffman (Class) done returns byte array
# rle done
# tunstall done (Class)
# arithmetic done (Counter)
# dictionary based done
# shannonfano
