#/usr/bin/python

# Clase invocadora del comando
class Invocador(object):
    def ejecutar_comando(self):
        ingreso = IngresoPlataforma(Receptor())
        ingreso.ejecutar()

# Interface que define la usabilidad de un comando
class Comando(object):
    def ejecutar(self): pass

# Clase concreta que dispara el comando
class IngresoPlataforma(Comando):
    def __init__(self, estado):
        self.receptor = estado

    def ejecutar(self):
        self.receptor.accion()

# Comando ejecutado luego de ser invocado
class Receptor(object):
    def accion(self):
        print "Ingresa a la plataforma Rouz Gym"
