# #una función es un bloque de código que se va a ejecutar cuantas veces sea llamada la función

# def saludar():
#     print("Hola, buenas tardes")

# saludar()

# #funciones con parametros 
# #los parametros que usan funcines o las variables creadas dentro de las mismas solamente podrán ser accedidas dentro de ellas
# def saludarPersona(nombre):
#     edad=40
#     print(f"Hola {nombre} como te va")

# saludarPersona("Carlos")


# def sin_nombre():
#     """Función que no hace nada y solamente es de muestra"""
#     print("Yo soy una función sin nombre")

# sin_nombre()

# #las funciones pueden recibir parametros y estos pueden ser opcionales
# def registro(nombre, correo=None):     #None significa vacio
#     print("Registro exitoso")

# registro("Carlos")
# registro("Carlos","carlosusix@gmail.com")

# # Crear una funcion llamada identificacion en la cual se reciba el nombre, apellido y la nacionalidad del cliente, si en el caso no se pasa la nacionalidad entonces sera Peruano, imprimir el resultado en forma de un diccionario
# # def identificacion(nombre, apellido, nacionalidad="Peruano"):
# #     if nacionalidad==None:
# #         print(f"Su nombre y apellido son {nombre} {apellido} y su nacionalidad es peruano")
# #     else:
# #         print(f"Su nombre y apellido son {nombre} {apellido} y su nacionalidad es {nacionalidad}")

# # identificacion("Carlos","Castro")
# # identificacion("Carlos","Castro","Colombiano")

# def identificacion(nombre, apellido, nacionalidad="Peruano"):
#     resultado = {
#         "nombre": nombre,
#         "apellido":apellido,
#         "nacionalidad": nacionalidad
#     }
#     print(resultado)

# identificacion("Carlos","Castro")
# identificacion("Carlos","Castro","Colombiano")

# # todos los parametros que tengan un valor predeterminado SIEMPRE VAN AL FINAL
# def sumatoria(num1, num2=10, num3=15):
#     print(num1+num2+num3)
# sumatoria(10)

# # el parametro que tiene el simbolo * es un parámetro especiañ de python que sirve para almacenar n valores
# #todos los valores que pasemos a ese parametro se almacenaran en una tupla en el mismo prden con el cual hemos pasado los parametros
# def alumnos(*args):
#     print(args)

# alumnos("Eduardo", "Siannet", "Pablo", "Fernando", "Rick", "Jhonathan")

# #se recomienda que *args debe ir al final
# def tareas(nombre, apellido, *args):
#     print("ok")

# tareas("Eduardo", "Martinez", "1", "2", 3)

# en la función alumnos_notas se recibira una cantidad N de alumnos en la cual se debe indicar cuantos aprobaron y cuanto desaprobaron siendo la nota mínima 11
#pass es una palabra reservada que me permite pasar la funcion que aun no he implementado 
# def alumnos_notas():
#     # todo: implementar lógica
#     pass

# def alumnos_notas(nombre, promedio):
#     if promedio >=11:
#         print(f"El alumno {nombre}, esta {promedio}")
def alumnos_notas(*args):
    aprobados = 0
    desaprobados = 0
    for alumno in args:
        if alumno['promedio'] >=11:
            aprobados +=1
        else:
            desaprobados +=1
    print(f"Hay {aprobados} alumnos aprobados y {desaprobados} alumnos desaprobados")

alumnos_notas(
    {"nombre": "Raul", "promedio":17},
    {"nombre": "Roxana", "promedio": 20},
    {"nombre": "Alfonso", "promedio": 10},
    {"nombre": "Pedro", "promedio": 8},
    {"nombre": "Katherine", "promedio": 16}
)

#keyword arguments => es muy similar a los *args solo con la diferrencia de los kwargs usan el nombre del parametro (nombre="Eduardo")
def indeterminada(**kwargs):
    print(kwargs)

indeterminada(nombre="Eduardo", apellido="de rivero", nacionalidad="Peruano")

indeterminada(edad=50, estatura=2.10)

def variada(*args, **kwargs):
    print(args)
    print(kwargs)

variada(10, "eduardo", {"est_civil":"Viudo"},
mascota="Firulais", raza="Buldog")

def sumatoria(num1, num2):
    print()