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
    num = ""
    for i in encoded_text:
        if i.isalpha():
            decoded_text += i*int(num)
            num = ""
        else:
            num += i

    return decoded_text
