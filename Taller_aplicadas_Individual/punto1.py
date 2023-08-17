# Autor: David Leonardo Lopez Forero

text = "ATAQUEN"

def cesar(text):
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    alphabet = alphabet.lower()
    alphabet = list(alphabet)
    text = text.lower()
    text = list(text)
    new_text = ""
    for i in range(len(text)):
        new_text += alphabet[(alphabet.index(text[i]) + 3) % 27].upper()
    return new_text

print("el texto a cifrar es: " + text)
print("el texto cifrado es: " + cesar(text))
    