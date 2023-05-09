def rail_fence_encode(plain_text, num_rails):
    # Initialize the fence with empty strings
    fence = ['' for i in range(num_rails)]

    # Populate the fence by iterating over the plaintext
    rail = 0
    direction = 1
    for char in plain_text:
        fence[rail] += char
        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction = -direction

    # Return the encoded message
    return ''.join(fence)


def rail_fence_decode(cipher_text, num_rails):
    # Create an empty matrix with the correct dimensions
    matrix = [['' for i in range(len(cipher_text))] for j in range(num_rails)]

    # Populate the matrix with the ciphertext
    rail = 0
    direction = 1
    for i in range(len(cipher_text)):
        matrix[rail][i] = '*'
        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction = -direction

    index = 0
    for i in range(num_rails):
        for j in range(len(cipher_text)):
            if matrix[i][j] == '*' and index < len(cipher_text):
                matrix[i][j] = cipher_text[index]
                index += 1

    # Read the plaintext from the matrix
    plain_text = ''
    rail = 0
    direction = 1
    for i in range(len(cipher_text)):
        plain_text += matrix[rail][i]
        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction = -direction

    # Return the decoded message
    return plain_text
