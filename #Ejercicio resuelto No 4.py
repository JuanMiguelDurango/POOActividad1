#Ejercicio resuelto No 4
Edad_Juan = int(input()) #Se recibe la edad de Juan como un entero
Edad_Alberto = int(Edad_Juan*(2/3)) #Se asigna la edad de Alberto como 2/3 la de Juan (Se reasigna el parametro int solo para eliminar el .0 del print final)
Edad_Ana = int(Edad_Juan*(4/3)) #Se asigna la edad de Ana como 4/3 la de Juan
Mama_Edad = Edad_Juan+Edad_Alberto+Edad_Ana #Se asigna la edad de Mamá como la suma de las 3 variables anteriores
print("Las edades son: Alberto:",Edad_Alberto,"Juan:",Edad_Juan,"Ana:",Edad_Ana,"Mamá:",Mama_Edad) #Se devuelven las edades mediante print