try:
    numero = 5 / 1
    print(f"el numero es {numero}")
    #numero=1000 / 0
    sumar = 1 + "1"
except ZeroDivisionError:
    print("Hubo un error al hacer la división")
except TypeError:
    print("No se puede sumar strings y números")
except:
    print("Error desconocido")
else:
    print("Todo bien")
finally:
    print("Igual me ejecuto")

#finally => no importa si la operacion salio bien o hubo errores, igual se ejecutara
# 
# else =>para usar el else tenemos que obligatoriamente DECLARAR un except, y este se ejecutará cuando no ingresa a ningún except (cuanndo la operación no tuvo errores)  
print("Soy un ejemplo")

#Ingresar 4 números si un de ellosno es un numero, entonces no tomarlo en cuenta y volver a pedir hasta que tengamos los 4 numeros

numeros = []
while len(numeros) != 4:
    try:
        numero=int(input("Ingrese un número: "))
        numeros.append(numeros)
    except:
        pass

print("Los números son {}".format(numeros))
