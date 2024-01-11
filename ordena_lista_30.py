# Crea una función que ordene y retorne una matriz de números.
 
# - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
#   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
#   o de mayor a menor.
# * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
#   automáticamente. 

def fun_listado(lista, orden):
    if orden == "ASC":
        for i in range(largo_lista):
            numero = int(input("Introduce un número >>>  "))
            lista.append(numero)

        for i in range(largo_lista):

             for j in range(0, largo_lista - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    
    if orden == "DESC":
        for i in range(largo_lista):
            numero = int(input("Introduce un número >>>  "))
            lista.append(numero)

        for i in range(largo_lista):

             for j in range(0, largo_lista - i - 1):
                if lista[j] < lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]  

    if orden != "DESC" or "ASC":
        lista = [1, 3, 5, 7]  

    return(lista)            



lista = []
largo_lista = int(input("¿De cuántos números va a ser tu lista? >>>  "))
ord = input("Escribe ASC si quieres que se muestre tu lista de forma ascendente o DESC si... ya sabes >>> ")
orden = ord.upper()

resultado = fun_listado(lista, orden)
<<<<<<< HEAD
print(f"Tu lista es: {resultado} esta dude, lo logramos")
print("Eres genial")
=======
print(f"Tu lista es: {resultado} esta dude, y ya no molestes")

>>>>>>> regresa_fuera_funcion

      
      





    





