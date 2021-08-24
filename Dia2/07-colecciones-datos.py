# list => listas
# ordenadas y modificables
colores =['morado','azul','rosado','amarillo']
mezclada = ['otoño', 14, False, 15.2, [1,2,3]]

# imprimir la primera posicion
# en Python si la posicion no existe, lanzara iun error, a diferencia de JS, que indicara undefined (no definido)
print (colores[0])
# al usar valores negativos en las posiciones de la lista, se 'invertirá' y podremos recorrer dicha lista
print (colores[-1])
print(colores[1:3])  #trae azul y rosado, trae de la posicion uno hast menor a la posicion menor que 3

print(colores[1:])

#toda la lista hasta la posicion menor que 2
print(colores[:2])

# sirve para copiar EL CONTENIDO de la lista mas no su ubicación de memoria
colores_2 = colores[:]
print(id(colores_2))
print(id(colores))

print(colores[1:-3])

# metodo para agregar un elemento a una lista
colores.append('naranja')
print(colores)

# 1.metodo para eliminar un valor
# solamente si existe lo eliinara, sino lanzara un error
colores.remove('azul')
print(colores)

# 2. si quieres eliminarlo y ADEMÁS guardar el valor eliminado en una variable
color_eliminado = colores.pop(0)
print(colores)
print(color_eliminado)

#3. el metodo para eliminar el valor
#este metodo tambien sirve para eliminar variables
# nombre="Carlos"
# del nombre
# print(nombre)

del colores[0]
print(colores)

# medira la longitud de la lista
# la longitud sera la cantidad de elementos de un arreglo 
print(len(colores))

# TUPLAS
# la tupla a diferencia de la lista es una coleccin de datos ordenada PERO que una vez creada no se puede editar
notas=(10, 15, 20,9,17,10,10,10,10)
print(notas[0])
print(len(notas))


print(notas.count(10))

# DICCIONARIOS
persona = {
    'nombre': 'Carlos',
    'apellido': 'Castro',
    'edad':28,
    'donacion_organos':True,
    'hobbies':[
        {
            'nombres':'Volar drones',
            'conocimiento':'avanzado'
        },
        {
            'nombre':'Montar bici',
            'conocimeinto':'intermedio'
        }
    ]
}

persona['edad']=35
persona['nacionalidad']= 'peruano'
print(persona['apellido'])
print(persona['nombre'])
print(persona)

# imprimir el primer hobby de la persona
# Volar drones
print(persona['hobbies'][0])

#forma de extraer solalemnte las llaves
print(persona.keys())

#forma de extraer solamente los valores
print(persona.values())

persona.clear()
print(persona)

#CONJUNTOS
#COLECCION DE DATOS desordenada, QUE UNA VEZ QUE LA CREAMOS NO PODREMOS ACCEDER A SUS POSICIONES YA QUE ESTARA ORDENADA ALEATORIAMENTE
#se puede editar mas no se puede ingresar a sus elementos por posiciones
alumnos = {'Kevin', 'Katherine', 'Ricardo', 'Aylin', 'Carlos', 'Eduardo'}
print(alumnos)
alumnos.add('Diego')
print(alumnos)
alumnos.remove('Eduardo')
print(alumnos)

#generalemnte se usa para guardar valores sin la necesidad de llaves
cursos = {'matematicas', 'cta', 'biologia', 'comunicacion'}
print('matematicas' in cursos)
