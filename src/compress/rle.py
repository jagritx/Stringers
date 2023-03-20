def rle_encode(text):
    encoded_text = ""
    i = 0
    while i < len(text):
        count = 1
        while i < len(text) - 1 and text[i] == text[i+1]:
            count += 1
            i += 1
        encoded_text += str(count) + text[i]
        i += 1
    return encoded_text


def rle_decode(encoded_text):
    decoded_text = ""
    i = 0
    while i < len(encoded_text):
        count = int(encoded_text[i])
        char = encoded_text[i+1]
        decoded_text += char * count
        i += 2
    return decoded_text
