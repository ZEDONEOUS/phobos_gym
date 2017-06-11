#!/usr/bin/python

# Clase decoradora
class Enrutamiento(object):
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, cls):
        print "Enrutamiento para el sistema roguz_gym"
        return self.func(instance)


    def __set__(self, obj, value):
        print(
            'Setting up {value} '
            'for {obj}'.format(value=value, obj=obj)
        )
        [setattr(obj, k, v) for k, v in value.items()]


# Clases definidas que obtienen la funcionalidad de la clase decoradora
class Rutinas(object):

    @Enrutamiento
    def get_object(self):
        return 'Control de peticiones get y post para rutinas'

class Ejercicios(object):

    @Enrutamiento
    def get_object(self):
        return 'Control de peticiones get y post para Ejercicios'
