textCipher = "ALCONNOBEOGLLVVZGOCOVNSOVZDOODELXFMVLXÑZ"
alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def analisisFrecuencia(text):
    frecuency = {}
    for letter in text:
        if letter in frecuency:
            frecuency[letter] += 1
        else:
            frecuency[letter] = 1
    
    moreLetter = max(frecuency, key=frecuency.get)
    return moreLetter

print("Las letras que mas se repiten son: ", analisisFrecuencia(textCipher))


def desplazamiento(moreLetter):
    desplazamiento = alphabet.index(moreLetter) - alphabet.index("E")
    return desplazamiento

print("El desplazamiento es: ", desplazamiento(analisisFrecuencia(textCipher)))


def descifrar(text, desplazamiento):
    textDescipher = ""
    for letter in text:
        if letter in alphabet:
            textDescipher += alphabet[(alphabet.index(letter) - desplazamiento) % len(alphabet)]
        else:
            textDescipher += letter
    return textDescipher


print("El mensaje descifrado es: ", descifrar(textCipher, desplazamiento(analisisFrecuencia(textCipher))))