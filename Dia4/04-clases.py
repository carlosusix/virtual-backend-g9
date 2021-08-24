class Mueble:
    precio = 00.00
    color = "Blanco"
    especificaciones = []
    tipo = ""

    def indicar_tipo(self):
        return "El tipo es: {}".format(self.tipo)


# el self nunca se pasa, si es que hay otro parametro si se pasa
mueble1 = Mueble()  #aqui estoy instanciando es decir copiando la clase
mueble1.tipo = "Sofa-cama"
print(mueble1.indicar_tipo())

mueble2 = Mueble()
mueble2.tipo = "Silleta"
print(mueble2.indicar_tipo())
