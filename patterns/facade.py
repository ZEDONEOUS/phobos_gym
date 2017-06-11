#!/usr/bin/python


# Interface de acciones sobre partes complejas
class Usuario:
    def crear_rutina(self): pass
    def asignar_tipo_cuerpo(self, position): pass
    def asignar_ejercicios(self): pass

# Definicion de partes complejas
class Administrador:
    def cargar(self): pass

# Fachada
class Computer:
    def __init__(self):
        self.usuario = Usuario()
        self.administrador = Administrador()

    def start_computer(self):
        self.usuario.crear_rutina()
        self.administrador.cargar()
        self.administrador.asignar_tipo_cuerpo(10)
        self.administrador.asignar_ejercicios()
