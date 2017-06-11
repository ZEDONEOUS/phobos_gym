#!/usr/bin/python

# Controlador de logueos con cadena de responsabilidades
class LoginHandler(object):
    def __init__(self, sucesor = None):
        self.sucesor = sucesor

    def ingreso_plataforma(self): pass

# Definicion de clase para controlar la peticion de logueo
class LoginAdmin(LoginHandler):
    def ingreso_plataforma(self):
        if True:
            print "ingreso plataforma administrador"
        elif self.sucesor is not None:
            self.sucesor.ingreso_plataforma()

# Definicion de clase final de la cadena
class LoginCliente(LoginHandler):
    def ingreso_plataforma(self):
        if False:
            print "ingreso plataforma cliente"
        elif self.sucesor is not None:
            self.sucesor.ingreso_plataforma()
