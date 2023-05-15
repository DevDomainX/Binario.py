#!/usr/bin/env python3 
#Create: by Hans Saldias
from colorama import init, Fore, Style
init()
print(Fore.GREEN+"""
Scrip sencillo para combertir numeros enteros a binario

solo ingrese el numero o numeros y le arrojara el resultado a binario

Create by: Hans Saldias\n\n 
""")

while True:
    try:
      print("Ingrese numero  a combertir binario...\n")
      numero= int(input("Ingrese numero: "))

      prueba= bin(numero)


      print(f"\nEl numero de su ingreso a binario es {prueba}")

    except:
      print("Error => Ingrese un numero (123)\n")
    print("\nPara salir presione 'Ctrl + z'\n")