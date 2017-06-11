#!usr/bin/python

# Definicion de la fablica abstracta
class RutinaFabricaAbstracta(object):
    def crearIntensidad(arg): pass

    def crearTipoCuerpo(arg): pass

# Definicion de la fabrica de tipo cuerpo
class TipoCuerpoAbstracto:
    def accion(self): pass

class Hectomorfo(TipoCuerpoAbstracto):
    def accion(self):
        print "Hectomorfo"

class Mesomorfo(TipoCuerpoAbstracto):
    def accion(self):
        print "Mesomorfo"

class Endomorfo(TipoCuerpoAbstracto):
    def accion(self):
        print "Endomorfo"

# Definicion de la fabrica de intensidad
class IntensidadAbstracto:
    def accion(self): pass

class Basico(IntensidadAbstracto):
    def accion(self):
        print "Basico"

class Intermedio(IntensidadAbstracto):
    def accion(self):
        print "Intermedio"

class Avanzado(IntensidadAbstracto):
    def accion(self):
        print "Avanzado"

# Fabrica de rutinas concretas
class RutinaAres(RutinaFabricaAbstracta):
    def crearIntensidad(arg):
        return Intermedio()

    def crearTipoCuerpo(arg):
        return Hectomorfo()

# Definicion del cliente
class Cliente(object):
    def __init__(self, fabrica):
        self.fabrica = fabrica
        self.intensidad = fabrica.crearIntensidad()
        self.tipo_cuerpo = fabrica.crearTipoCuerpo()

    def accion(self):
        self.intensidad.accion()
        self.tipo_cuerpo.accion()
