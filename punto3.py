public_key = (517, 31)
textCipher =232
options = ["A", "B", "C", "D"]
cripto_option={}


for option in options:
    m = ord(option)
    cripto_option[option] = pow(m, public_key[1], public_key[0])

if cripto_option["A"] == 65 or cripto_option["B"] == 66 or cripto_option["C"] == 67 or cripto_option["D"] == 68:
    print("La deduccion del atancante es verdadera.")
else:
   print("La deduccion del atancante es falsa.")

print("las opciones encriptadas son: ", cripto_option)