from camelcase import CamelCase

instancia = CamelCase("alumnos")

texto = "hola alumnos buenas noches ya se viene el break"

resultado = instancia.hump(texto)

print(resultado)

print(texto[1])
for letra in texto:
    print(letra, end="*")



