# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 09/11/2026
# Versió: 1
#
# Descripció: Demana a l'usuari un nombre enter i imprimeix tots els nombres primers des de 2 fins a aquest nombre.​
# Especificacions Programa que generi un nombre enter i imprimeix tots els nombres primers

try:
    num = int(input("Introdueix un nombre enter: "))

    print(f"\nNombres primers de 2 fins a {num}:\n")

    for i in range(2, num + 1):
        primer = True

        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                primer = False
                break

        if primer:
            print(i)

except ValueError:
    print("Aquest no és un valor enter positiu")