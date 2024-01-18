"""Crea un programa que calcule el daño de un ataque durante
 * una batalla Pokémon.
 * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
 *   (buscar su efectividad)
 * - El programa recibe los siguientes parámetros:
 *  - Tipo del Pokémon atacante.
 *  - Tipo del Pokémon defensor.
 *  - Ataque: Entre 1 y 100.
 *  - Defensa: Entre 1 y 100."""



print("ÉSTA ES UNA BATALLA POKEMÓN")
print("TIPOS DE POKEMÓN: ")
print("1 >>> AGUA \n2 FUEGO \n3 PLANTA \n4 ELECTRICO")




effectivness = ("super_effective", "neutral", "not_that_effective")
pokemon_type = ("AGUA", "FUEGO", "PLANTA", "ELECTRICO") 
type_att_pokemon = int(input("Ingrese el número correspondiente (1-4) al tipo de pokemón que ATACA >>> "))
type_def_pokemon = int(input("Ingrese el número correspondiente (1-4) al tipo de pokemón que DEFIENDE >>> "))
att_pokemon = int(input("¿Cuál es el ataque del pokemón ofensor? >>> ")) 
if att_pokemon > 100 or att_pokemon < 1:
    print("El ataque debe de tener un valor entre 1 y 100")
def_pokemon = int(input("¿Cuál es la defensa del pokemón defensor? >>> ")) 


print(effectivness[0],",", pokemon_type[3])



