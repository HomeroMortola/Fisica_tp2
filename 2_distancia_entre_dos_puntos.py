import math

#Función para convertir a metros
conversion_a_metros = {
    'k': 1000,     #kilómetros a metros
    'a': 1609.34,  #millas a metros
    'm': 1         #metros
}

#Se pide que el usuario ingrese la unidad
while True:
    unidad_input = input("Ingrese las unidades a utilizar (k=kilómetro / a=milla / m=metro): ").lower()
    if unidad_input in conversion_a_metros:
        factor_conversion = conversion_a_metros[unidad_input]
        break
    else:
        print("Entrada no válida")

#Se pide el tipo de distancia
while True:
    distancia_calcular = input("Ingrese el tipo de distancia a calcular (t=taxi / e=euclídea / m=máximo): ").lower()
    if distancia_calcular in ('t', 'e', 'm'):
        break
    else:
        print("Entrada no válida")

try:
    x1 = float(input("Ingrese la coordenada x del primer punto: "))
    y1 = float(input("Ingrese la coordenada y del primer punto: "))
    x2 = float(input("Ingrese la coordenada x del segundo punto: "))
    y2 = float(input("Ingrese la coordenada y del segundo punto: "))

    #Se calcula la distancia según el tipo elegido
    match distancia_calcular:
        case 't':  # Taxi
            distancia = abs(x1 - x2) + abs(y1 - y2)
        case 'e':  # Euclídea
            distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        case 'm':  # Máximo
            distancia = max(abs(x1 - x2), abs(y1 - y2))

    #Se convierte el resultado a metros con la funcion creada anteriormente
    resultado_en_metros = distancia * factor_conversion
    print(f"Su resultado es de {resultado_en_metros:.2f} metros.")

except ValueError:
    print("Valores no válidos. Asegúrese de ingresar números.")
