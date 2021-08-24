#Condicionales
#If (edad > 18) ....else ....

edad = int(input("Ingrese su edad: "))
#entre 18 y 64 años
if edad>=18 and edad<=64:
    print("Puedes vacunarte")
    print("sigo en el if")
#elseif => sino si | siempre va despues de un if o despues de otro elif  a diferencia del else este lleva una condicion
# a mas de 65 años
elif edad >= 65 :
    print("Necesitas tercera dosis")
#menor de 18 años
else:
    print("Todavia no puedes vacunarte")

print("Yo me ejecuto asi se cumpla o no se cumpla el if")

#OPERADOR TERNARIO
#es una forma de hacer una validación pero en una sola línea de código
#RESULTADO_IF  ....... IF condicion ELSE   RESULTADO_ELSE
texto = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(texto)

#Destructuracion de variables una lista o tupla
#se debe crear la misma cantidad de elementos con los elemntos del arreglo
variable1, variable2, variable3 =["Carlos", "Saul", "Carlos Saul"]
print(variable1)
print(variable2)


a=int(input("Ingrese número: "))
if a==0:
    print(f'El número {a} es cero')
elif a % 2 == 0:
    print(f'El número {a} es par')
else:
   print(f'El número {a} es impar')

# como comentar varias lineas ctrl + k + c

#BUCLES

#FOR => repite desde hasta
meses = ['AGOSTO', 'SETIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
# si nosotros queremos iterar una colección de datos la mejor forma es mediante un FOR
for mes in meses:
    print(mes)
#a diferencia del manejo de scopes (alcance) de la variable en JS, en python, la variable sigue existiendo fuera del for

print(mes)

for numero in range(10):
    print(numero)
    print('=================')

# el range puede recibir hast 3 parámetros
# range(n) => n: el limite de las iteraciones
#range(m,n) => m: el numero inicial
#range(m,n,o)=> o: en cuanto se va a incrementar o decrementar el valor en cada ciclo
for numero in range(5,10):
    print (numero)

print('==========================')

for numero in range(1,10,2):
    print(numero)

print('==========================')

#de la siguiente lista de numeros indicar cuantos son positivos y negativos
numeros = [-4,7,-10,8,25,-7]

#RPTA
# hay 3 negativos y 3 positivos
positivos = 0
num_positivos = []
negativos = 0
num_negativos = []
for numero in numeros:
    if numero > 0:
        num_positivos.append(numero)
        positivos +=1
    else:
        num_negativos.append(numero)
        negativos +=1
        
print(f"hay {negativos} números negativos y son {num_negativos} y hay {positivos} números positivos y son {num_positivos}")

# otra forma
num_positivos = []
num_negativos = []
for numero in numeros:
    if numero > 0:
        num_positivos.append(numero)
    else:
        num_negativos.append(numero)
        
print(f"hay {len(num_negativos)} números negativos y son {num_negativos} y hay {len(num_positivos)} números positivos y son {num_positivos}")

#otra forma
resultado = [[],[]]
for numero in numeros:
    if(numero > 0):
        resultado[0].append(numero)
    else:
        resultado[1].append(numero)
print(
    f"hay {len(resultado[1])} números negativos y son {resultado[1]} y hay {len(resultado[0])} números positivos y son {resultado[0]}"
)

#BREAK
# hace que un el bucle finalice de manera inesperada
for segundo in range(60):
    print(segundo)
    if segundo == 10:
        break

#NOTA: en python el switch - case no existe!
print("============================")
#CONTINUE
#salta la iteracion actual
for numero in range(15):
    if numero == 10 or numero == 11:
        continue
    print(numero)  



#dado los siguientes números:
numeros = [1,2,3,5,9,12,15,17,19,21,25,39, 45]
#indicar cuantos de ellos son multiplos de 3 y de 5, ademas si hay un multiplo de 3 y 5 no contabilizarlos
#multiplos de : 3, multiplos de 5: 1

mul3 = 0
num_mul3 = []
mul5 = 0
num_mul5 = []
for numero in numeros:
    if numero % 15 == 0:
        continue
    if numero % 3 == 0:
        # num_positivos.append(numero)
        mul3 +=1
    elif numero % 5 == 0:
        # num_negativos.append(numero)
        mul5 +=1
        
print(f"hay {mul3} números múltiplos de 3  y hay {mul5} números multiplos de 5")

print("============================")

#WHILE (mientras)
#se ejecutara siempre que la condición sea veradera
#NOTA: en Phyton no existe el do-while
numero = 5
while numero <10:
    numero += 1
    print(numero)

#Ingresar números hasta que  dicho número sea adivinado
numero_adivinar = 10
#5 => 'el número es mayor que ese'
#13 => 'el número es menor que ese'
#10 => 'felicidades adivinaste el número'

#resolución
while True:
    numero = int(input('Ingrese el número: '))
    if numero < numero_adivinar:
        print('El número es mayor que {}'.format(numero))
    elif numero > numero_adivinar:
        print('El número es menor que {}'.format(numero))
    elif numero == numero_adivinar:
        print('Felicidades adivinaste le número')
        break



















