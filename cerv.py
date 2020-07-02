import os
diccionario = dict()
os.system("cls")

cont = 1

while cont <= 5:
   cont += 1
   cerveza = input("Nombre de la Cerveza: ").title()
   cantidad = int(input("Cantidad: "))
   diccionario[cerveza] = cantidad
   os.system("cls")

cont = 1

diccionario_sort = sorted(diccionario.items())
os.system("cls")
for i in diccionario_sort:
   print("{:12} = {:2}".format(i[0],i[1]))
