#!/usr/bin/python

import abc

# Define una clase abstracta y establece los metodos primitivos
# para la plantilla
class AbstractFormsHandler(metaclass=abc.ABCMeta):
    def template_method(self):
        self.crear()
        self.validar()

    @abc.abstractmethod
    def crear(self):
        pass

    @abc.abstractmethod
    def validar(self):
        pass

# Implementa las operaciones primitivas
class RegistroUsuariosForm(AbstractFormsHandler):
    def crear(self):
        print "creacion del formulario de registro de usuarios"

    def validar(self):
        print "validacion de campos del formulario"

# Implementa las operaciones primitivas
class RegistroRutinasForm(AbstractFormsHandler):
    def crear(self):
        print "creacion del formulario de registro de rutinas"

    def validar(self):
        print "validacion de los campos del formulario de registr de rutinas"

# Implementa las operaciones primitivas
class LoginForm(AbstractFormsHandler):
    def crear(self):
        print "creacion del formulario de Login"

    def validar(self):
        print "validacion de los campos del formulario de Login"

def main():
    concrete_class = ConcreteClass()
    concrete_class.template_method()
