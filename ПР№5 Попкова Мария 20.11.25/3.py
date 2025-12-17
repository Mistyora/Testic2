def decode(encoded_text):

    back_to_normal = encoded_text[::-1]

    decoded = ""
    for char in back_to_normal:
        decoded += chr(ord(char) - 1)
    return decoded

text = (input("Введите закодированный текст: "))
decoded_text = decode(text)
print("Закодированный текст:", decoded_text)