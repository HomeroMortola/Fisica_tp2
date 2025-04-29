import math
import sys
while True:
    unidades_utilizar = input("Ingrese las unidades a utilisar(k=kilometro/a=milla/m=metro) :").lower()

    #comprobamos si la estrada es valida y asignamos la unidad a utilisar
    match unidades_utilizar:
        case 'k':
            unidades_utilizar = "kilometros"
            break
        case 'a':
            unidades_utilizar = "milla"
            break
        case 'm':
            unidades_utilizar = "metros"
            break
        case 'z':
            print("terminando programa")
            exit()
        case _:
            print("Entrada no valida")
    
while True:
    distancia_calcular = input("Ingrese la distancia a calcular () :").lower()
    #comprobamos si la estrada es valida y asignamos la unidad a utilisar
    if distancia_calcular == 't' or distancia_calcular == 'e' or distancia_calcular == 'm':
        break
    elif distancia_calcular == 'z':
        print("terminando programa")
        exit()
    else:
        print("Entrada no valida")
    
    


