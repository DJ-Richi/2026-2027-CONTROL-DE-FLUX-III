# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 09/11/2026
# Versió: 1
#
# Descripció: Escriu un programa que mostri la taula de multiplicar d'un número introduït per l'usuari.
# Especificacions Programa que generi la taula de multiplicar d'un número introduït per l'usuari.

try:
    num = int(input("Introdueix un número per veure la taula de multiplicar: "))

    print(f"\nTaula de multiplicar del {num}:\n")
    for i in range(0, 11):
      print(f"{num} x {i} = {num * i}")

except ValueError:
   print("Aquest valor no es un nobre enter")