#!/usr/bin/python

# Clase encargada de la representacion del objeto comun
class Ejercicio(object):
    def __init__(self, nom_ej, desc_ej):
        self.nom_ej = nom_ej
        self.desc_ej = desc_ej

# Clase que se encarga de controlar las instancias de cada objeto
class FabricaRutinas(object):
    def __init__(self):
        self.instancias = dict()

    def get_instancia(self, nom_ej, desc_ej):
        if (nom_ej, desc_ej) not in self.instancias:
            self.instancias[(nom_ej, desc_ej)] = Ejercicio(nom_ej, desc_ej)
        return self.instancias[(nom_ej, desc_ej)]
