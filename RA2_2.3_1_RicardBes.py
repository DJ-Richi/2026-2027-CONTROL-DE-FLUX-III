# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 09/11/2026
# Versió: 1
#
# Descripció: Demana a l'usuari un programa que generi una seqüència de nombres des de 0 fins a un nombre introduït per l'usuari. 
# Especificacions Programa que generi una seqüència de nombres des de 0 fins a un nombre per part de l'usuari. 


try:
    numero = int(input("Introdueix un nombre: "))

    for i in range(numero + 1):
        print(i)

except Exception:
    print("Error: has d'introduir un nombre enter.")