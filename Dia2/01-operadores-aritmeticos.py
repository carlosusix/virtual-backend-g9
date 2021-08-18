numero1 = 10
numero2 = 80

persona1 = "Eduardo"
persona2 = "Ricardo"

#SUMA 
# nOTA: SI LAS DOS O MAS VAROABLES SON NUMERICAS ENTONCES SE REALIZARA LA SUMA, SI POR EL CONTRARIO LAS VARIABLES SON STRING (CARACTERES) SE CONCATENARAN (SE JUNTARAN)
print(numero1 + numero2)
numero1_string = str(numero1)
print(numero1_string + persona1)

#RESTA
print(numero1 - numero2)
# No se puede usar la resta en variables que no sean numéricas
# print(persona1 - persona2)

#MULTIPLICACION
print(numero1 * numero2)
# el * 2 indica la cantidad de repeticiones que hara la palabra
print(persona1 * 2)

# la multiplicacionde 10 y 80 es 800
print("La multiplicacion de {} y {} es: {}".format(numero1, numero2, numero1*numero2))

print(f"La multiplicacion de {numero1} y {numero2} es: {numero1 * numero2}")

# DIVISIÓN
# Toda divisón aun así sea entera siempre sera flotante (tiene una parte entera y una parte decimal)
print(numero2 / numero1)

#MODULO
# el modulo es el resultado de la división
print(numero2 % numero1)
print(numero1 % numero2)

# COCIENTE
print(numero2 // numero1)
