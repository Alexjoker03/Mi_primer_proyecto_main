# Crea una función que ordene y retorne una matriz de números.
 
# - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
#   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
#   o de mayor a menor.
# * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
#   automáticamente. 

def fun_listado(lista, orden):
    print(lista)


lista = []
largo_lista = int(input("¿De cuántos números va a ser tu lista? >>>  "))
for i in range(largo_lista):
    numero = int(input("Introduce un número >>>  "))
    lista.append(numero)

fun_listado(lista, orden)

