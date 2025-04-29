import math
import sys
while True:
    unidadez_utilisar = str(input("Ingrese las unidades a utilisar(k=kilometro/a=milla/m=metro) :").lower())

    #comprobamos si la estrada es valida y asignamos la unidad a utilisar
    match unidadez_utilisar:
        case "k":
            unidadez_utilisar = "kilometros"
            break
        case 'a':
            unidadez_utilisar = "milla"
            break
        case 'm':
            unidadez_utilisar = "metros"
            break
        case 'z':
            exit()
            break
        case _:
            print("Entrada no valida")
    
while True:
    distancia_calcular = input("Ingrese la distancia a calcular () :").lower()
    #comprobamos si la estrada es valida y asignamos la unidad a utilisar
    if distancia_calcular == 't' or distancia_calcular == 'e' or distancia_calcular == 'm':
        break
    else:
        print("Entrada no valida")
    


