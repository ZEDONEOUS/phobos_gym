#!/usr/bin/python

# Definicion del director de la rutina
class DirRutinas:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    # Algoritmo para crear una rutina
    def getRutina(self):
        rutina = Rutina()

        intensidad = self.__builder.getIntensidad()
        rutina.setIntensidad(intensidad)

        ejercicio = self.__builder.getEjercicio()
        rutina.setEjercicio(ejercicio)

# Definicion de las partes de la rutina
class Ejercicio:
    accion = None

class Intensidad:
    nivel = None

# Definicion de la estructura de la rutina
class Rutina:

    def __init__(self):
        self.intensidad = None
        self.ejercicios = None

    def setIntensidad(self, intensidad):
        self.ejercicios = intensidad

    def setEjercicio(self, ejercicio):
        self.intensidad = ejercicio

    def specification(self):
        print "Ejercicios: ", self.ejercicios.accion
        print "Intensidad de la rutina: ", self.intensidad.nivel

# Clase abstracta constructora
class Builder:
    def getEjercicio(self): pass
    def getIntensidad(self): pass

# Definicion concreta de una rutina
class BuilderRutinaAres(Builder):

    def getEjercicio(self):
        ejercicio = Ejercicio()
        ejercicio.accion = "Sentadillas"
        return ejercicio

    def getIntensidad(self):
        intensidad = Intensidad()
        intensidad.nivel = "Avanzado"
        return intensidad

def main():
    ares = BuilderRutinaAres()

    director = DirRutinas()

    # Build Nissan
    print "Nissan"
    director.setBuilder(ares)
    rutina = director.getRutina()
    rutina.specification()
