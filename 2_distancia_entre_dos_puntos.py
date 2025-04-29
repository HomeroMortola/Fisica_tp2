
while True:
    unidadez_utilisar = input("Ingrese las unidades a utilisar(k=kilometro/a=milla/m=metro) :").lower

    #comprobamos si la estrada es valida y asignamos la unidad a utilisar
    match unidadez_utilisar:
        case 'k':
            unidadez_utilisar = "kilometros"
            break
        case 'a':
            unidadez_utilisar = "milla"
            break
        case 'm':
            unidadez_utilisar = "metros"
            break
        case _:
            print("Entrada no valida")
    
while True:
    distancia_calcular = input("Ingrese la distancia a calcular () :").lower
    #comprobamos si la estrada es valida y asignamos la unidad a utilisar
    if distancia_calcular == 't' or distancia_calcular == 'e' or distancia_calcular == 'm':
        break
    else:
        print("Entrada no valida")

try:
    x1 = input("Ingrese la cordenada x del primer punto :")
    y1 = input("Ingrese la cordenada y del primer punto :")
    x2 = input("Ingrese la cordenada x del segundo punto :")
    y2 = input("Ingrese la cordenada y del segundo punto :")

    match distancia_calcular:
        case 'k'


except:
    print("Valore no validos")

