import math
import sys

#Función para convertir a metros
conversion_a_metros = {
    'k': 1000,     # kilómetros a metros
    'a': 1609.34,  # millas a metros
    'm': 1         # metros ya está en metros
}

while True:
    unidad_input = input("Ingrese las unidades a utilizar (k=kilómetro / a=milla / m=metro): ").lower()
    if unidad_input in conversion_a_metros:
        factor_conversion = conversion_a_metros[unidad_input]
        break
    elif unidad_input == 'z':
        print("terminando programa")
        exit()
    else:
        print("Entrada no válida")
    

while True:
    distancia_calcular = input("Ingrese el tipo de distancia a calcular (t=taxi / e=euclídea / m=máximo): ").lower()
    if distancia_calcular in ('t', 'e', 'm'):
        break
    elif distancia_calcular == 'z':
        print("terminando programa")
        exit()
    else:
        print("Entrada no válida")


i = 1

lista_x = []
lista_y = []

try:
    while True:
        print("ingrese el punto (0;0) para realisar el calculo")
        
        x_inp = float(input(f"ingrese el valor x del punto {i}: "))
        y_inp = float(input(f"ingrese el valor y del punto {i}: "))

        if x_inp == 0 and y_inp == 0:
            break

        lista_x.append(x_inp)
        lista_y.append(y_inp)

        i += 1
except:
    print("valores invalidos")

distancia = 0
match distancia_calcular:
    case 't':
        for i in range(1,len(lista_x)):
            distancia=abs(lista_x[i-1]-lista_y[i-1])+abs(lista_x[i]-lista_y[i])
    case 'e':
        print("")

resultado_en_metros = distancia * factor_conversion
print(f"Su resultado es de {resultado_en_metros:.2f} metros.")




    



    
    


