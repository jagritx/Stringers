import math


def golomb_encode(input_str, m):
    """
    Encode a string using Golomb coding with parameter m.
    """
    # Compute the value of b that minimizes the average code length.
    b = int(math.ceil(math.log2(m)))

    # Initialize the output string.
    output_str = ""

    # Encode each character in the input string.
    for char in input_str:
        # Compute the quotient and remainder of the Golomb code.
        q, r = divmod(ord(char), m)

        # Append the quotient to the output string using unary code.
        output_str += "1" * q + "0"

        # Append the remainder to the output string using binary code.
        output_str += "{0:b}".format(r).zfill(b)

    return output_str


def golomb_decode(input_str, m):
    """
    Decode a string encoded using Golomb coding with parameter m.
    """
    # Compute the value of b that minimizes the average code length.
    b = int(math.ceil(math.log2(m)))

    # Initialize the output string.
    output_str = ""

    # Decode each Golomb code in the input string.
    while len(input_str) > 0:
        # Find the index of the first zero after the first one.
        index = input_str.index("0") + 1

        # Count the number of ones before the first zero.
        q = input_str[:index].count("1")

        # Remove the encoded quotient from the input string.
        input_str = input_str[index:]

        # Extract the encoded remainder from the input string.
        r = int(input_str[:b], 2)

        # Remove the encoded remainder from the input string.
        input_str = input_str[b:]

        # Compute the decoded character and append it to the output string.
        char = chr(q * m + r)
        output_str += char

    return output_str
