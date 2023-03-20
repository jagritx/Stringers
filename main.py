from src.compress.shannonfano import sf_encode, sf_decode

s = 'hello world'
print("encoded", sf_encode(s))
print('Decoded string:', dict_decode(dict_encode(s)))

# Golomb done
# huffman (Class) done returns byte array
# rle done
# tunstall done (Class)
# arithmetic done (Counter)
# dictionary based done
# shannonfano
