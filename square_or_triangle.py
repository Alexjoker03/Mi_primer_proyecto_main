# Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
# * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
def triangulo(lado):
    for i in range(lado + 1):
        print(asterisco * i)

def cuadrado(lado):
    for i in range(lado):
        print(asterisco * (lado * 2))



asterisco = "*"

option = int(input("Selecciona una opción >>> 1) Dibuja un triángulo >>> 2) Dibuja un cuadrado  " ))

if option == 1:
    lado = int(input("¿De que tamaño quieres que sea el uno de los lados de tu figura? >>>>>  "))
    triangulo(lado)

elif option == 2:
    lado = int(input("¿De que tamaño quieres que sea el uno de los lados de tu figura? >>>>>  "))
    #Para pintar un cuadrado
    cuadrado(lado)

else:
    print("Tu respuesta no es valida")






