from flask import Flask
from conexion_bd import base_de_datos

app = Flask(__name__)
#                                        mysql://username:password@localhost/db_name                 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:carloscastro08@localhost/reposteria.flask'
#si se establece True SqlAlchemy rastreara las modificaciones de los objetos (modelos) y lanzara señales de cambio, su valor predeterminado en None, igual habilita el tracking pero emite una advertencia que en futuras versiones se removera el valor x default None y si o si tendremos que indicar un valor inicial
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#Inicia la conexioncon la bd para darle las credenciales definidas en el app.config
base_de_datos.init_app(app)

#creara las tablas aun no mapeadas y si todo esta bien no devolvera nada 
base_de_datos.create_all(app=app)

@app.route("/")
def initial_controller():
    return {
        "message":"Bienvenido a mi API de reposteria"
    }

if __name__ == '__main__':
   app.run(debug=True) 
