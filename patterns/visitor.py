#!/usr/bin/python

import abc

# Define una interface con las operaciones por usuario
class Visitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_product_a(self): pass

    @abc.abstractmethod
    def create_product_b(self): pass

# Implementa las operaciones para crear cada login
class LoginControlador(Visitor):
    def create_product_a(self):
        return ClienteLogin()

    def create_product_b(self):
        return ConcreteProductB1()

# Define una interface para un tipo de usuario por logueo
class LoginDefInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self): pass

# Implementa el usuario creado por la fabrica
class ClienteLogin(LoginDefInterface):
    def accept(self):
        print "login representativo de clientes"

# Implementa el usuario creado por la fabrica
class AdministradorLogin(LoginDefInterface):
    def accept(self):
        print "login representativo de administradores"



def main():
    for visitor in (LoginControlador()):
        product_a = visitor.create_product_a()
        product_b = visitor.create_product_b()
        product_a.accept()
        product_b.interface_b()
