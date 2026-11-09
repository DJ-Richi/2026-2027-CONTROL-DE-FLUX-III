# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 22/10/2024
# Versió: 1
#
# Descripció: Demana a l'usuari un nombre enter i imprimeix tots els nombres parells des de 0 fins a aquest nombre.
# Especificacions Programa que generi un nombre enter i imprimeix tots els nombres parells.

try:
    num = int(input("Introdueix un nombre enter: "))

    print(f"\nNombres parells de 0 fins a {num}:\n")
    for i in range(0, num + 1):
        if i % 2 == 0:
            print(i)

except ValueError:
    print("Aquest no es un valor enter positiu")