def encode(text):
    sdvig = ""
    for char in text:
        sdvig += chr(ord(char)+ 1) # сдвигаем символ на 1

    encoded = sdvig[::-1] # переворачиваем строку
    return encoded

text = (input("Введите текст для кодирования: "))
encoded_text = encode(text)
print("Закодированный текст:", encoded_text)