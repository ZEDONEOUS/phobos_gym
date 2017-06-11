#!usr/bin/python

# Ejercicio abstracto
class Ejercicio(object):
    # Metodo fabrica
    def fabricaEjercicios(tipo):
        if tipo == "Sentadillas":
            return Sentadillas()
        if tipo == "Barras":
            return Barras()
        if tipo == "Flexiones":
            return Flexiones()
        assert 0, "Creacion incorrecta de ejercicio: " + tipo
    fabrica = staticmethod(fabricaEjercicios)

# Ejercicio concreto
class Sentadillas(Ejercicio):
    def accion(self):
        print "creacion de Sentadillas"

# Ejercicio concreto
class Barras(Ejercicio):
    def accion(self):
        print "creacion de Barras"

# Ejercicio concreto
class Flexiones(Ejercicio):
    def accion(self):
        print "creacion de Flexiones"

# Creador abstracto
class FabricaEjercicios(object):
    def fabricaEjercicios(): pass

# Creador de ejercicios concreto
class CreadorEjercicios(FabricaEjercicios):
    def fabricaEjercicios(arg):
        ejercicio = Ejercicio.fabrica("Sentadillas")
        ejercicio.accion()

        ejercicio = Ejercicio.fabrica("Barras")
        ejercicio.accion()
