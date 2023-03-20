import heapq
from collections import Counter


def tunstall_encode(s, num_bits):
    # Get frequency counts of characters in string
    freqs = Counter(s)

    # Create a priority queue of trees, with each tree containing a single character
    trees = [([char], freqs[char]) for char in freqs]
    heapq.heapify(trees)

    # Build the Tunstall codebook by iteratively expanding the most frequent tree
    while len(trees) < 2 ** num_bits:
        tree, weight = heapq.heappop(trees)
        for char in freqs:
            new_tree = tree + [char]
            new_weight = weight * freqs[char]
            heapq.heappush(trees, (new_tree, new_weight))

    # Map each character to its Tunstall code
    codebook = {}
    for i, (tree, weight) in enumerate(trees):
        code = bin(i)[2:].zfill(num_bits)
        codebook[tree[0]] = code

    # Encode the string using the Tunstall codebook
    encoded = ''.join(codebook[char] for char in s)

    return encoded, codebook


def tunstall_decode(encoded, codebook):
    # Invert the codebook to map codes to characters
    inverse_codebook = {code: char for char, code in codebook.items()}

    # Decode the encoded string using the inverse codebook
    decoded = ''
    code = ''
    for bit in encoded:
        code += bit
        if code in inverse_codebook:
            decoded += inverse_codebook[code]
            code = ''

    return decoded
