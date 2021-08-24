from flask import Flask

#__name__ => muestra si el archivo en el cual se esta llamando a la clase Flask es el archivp principal del proyecto, esto se hace para eviatr que la instancia de la clase Flask se pueda crear en otros lados (patron de diseño Singletton)
app = Flask(__name__)

#si estamos en el archivo principal del proyecto nos imprimira __main__ caso contario imprimira la ubicacion del archivo
#print(__name__)

#decorador => un patron de software que se utiliza para modificar el funcionamiento de una clase o de una funcion en particular sin la necesidad de emplear otro metodos como la herencia (cosa que no se puede en una funcion comun y corriente)
@app.route('/')
def inicio():
    print("Me llamaron")
    return {
        "message":"Hello world!"
    }

#Nota: Todo el codigo a implementar siempre debe ir antes del run()
app.run(debug=True) #sirve para levantar un servidor web