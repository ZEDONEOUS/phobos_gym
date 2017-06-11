from rutinas import Rutinas
from ejercicios import Ejercicios
from administrador import Administrador
from usuarios import Usuarios
from termcolor import colored

class FabricaComponentes(object):

    def crear_componente(componente):
        if componente == "Rutinas":
            return Rutinas()
        elif componente == "Ejercicios":
            return Ejercicios()
        elif componente == "Administrador":
            return Administrador()
        elif componente == "Usuario":
            return Usuarios()
        assert 0, "imposible la creacion del componente!" + componente

    crear = staticmethod(crear_componente)
