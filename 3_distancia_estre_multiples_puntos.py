import math
import sys

#Función para convertir a metros
conversion_a_metros = {
    'k': 1000,     #kilómetros a metros
    'a': 1609.34,  #millas a metros
    'm': 1         #metros
}

def son_colineales(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1)

#Se pide la unidad de medida
while True:
    unidad_input = input("Ingrese las unidades a utilizar (k=kilómetro / a=milla / m=metro / z=salir): ").lower()
    if unidad_input in conversion_a_metros:
        factor_conversion = conversion_a_metros[unidad_input]
        break
    elif unidad_input == 'z':
        print("Terminando programa.")
        sys.exit()
    else:
        print("Entrada no válida.")

#Se pide el tipo de distancia
while True:
    distancia_calcular = input("Ingrese el tipo de distancia a calcular (t=taxi / e=euclídea / m=máximo / z=salir): ").lower()
    if distancia_calcular in ('t', 'e', 'm'):
        break
    elif distancia_calcular == 'z':
        print("Terminando programa.")
        sys.exit()
    else:
        print("Entrada no válida.")

#Se colocan los puntos en una lista (dependiendo de su coordenada)
lista_x = []
lista_y = []
i = 1

while True:
    print("Ingrese el punto (0, 0) para finalizar el ingreso y calcular la distancia.")
    try:
        x = float(input(f"Ingrese x del punto {i}: "))
        y = float(input(f"Ingrese y del punto {i}: "))

        if x == 0 and y == 0:
            if len(lista_x) < 2:
                print("Debe ingresar al menos dos puntos.")
                continue
            break

        #Para verificar que los puntos no se choquen entre ellos
        if len(lista_x) >= 2:
            if son_colineales(lista_x[-2], lista_y[-2], lista_x[-1], lista_y[-1], x, y):
                print("El punto está en la recta de los dos anteriores. Ingrese otro punto.")
                continue

        lista_x.append(x)
        lista_y.append(y)
        i += 1

    except ValueError:
        print("Valores inválidos. Intente de nuevo.")

#Se calcula la distancia
distancia_total = 0

match distancia_calcular:
    case 't':  #Taxi
        for i in range(1, len(lista_x)):
            dx = abs(lista_x[i] - lista_x[i - 1])
            dy = abs(lista_y[i] - lista_y[i - 1])
            distancia_total += dx + dy

    case 'e':  #Euclídea
        for i in range(1, len(lista_x)):
            dx = lista_x[i] - lista_x[i - 1]
            dy = lista_y[i] - lista_y[i - 1]
            distancia_total += math.sqrt(dx**2 + dy**2)

    case 'm':  #Máximo
        for i in range(1, len(lista_x)):
            dx = abs(lista_x[i] - lista_x[i - 1])
            dy = abs(lista_y[i] - lista_y[i - 1])
            distancia_total += max(dx, dy)

resultado_en_metros = distancia_total * factor_conversion
print(f"\nLa distancia total del camino es: {resultado_en_metros:.2f} metros.")
