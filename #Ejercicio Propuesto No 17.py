#Ejercicio Propuesto No 17
#En este programa utilizo la libreria math, sin embargo es posible conseguir un resultado aproximado utilizando 3.1416
import math
Radio = int(input())
area = math.pi * (Radio**2)
longitud = 2*math.pi*Radio
#En el problema no se especifica si deben ser redondeados los resultados, por ende no lo haré
print("Área del círculo:", area, "Longitud del círculo:", longitud)