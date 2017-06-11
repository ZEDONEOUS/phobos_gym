from abc import ABCMeta, abstractmethod
from interface import Interface, implements

# Interface de especificacion de objeto
class IEspecialista(Interface):
    def operacionImp(self): pass

# Objeto concreto
class Nutricionista(implements(IEspecialista)):
    def operacionImp(self):
        print "Nutricional"

# Objeto concreto
class Fisioterapeuta(implements(IEspecialista)):
    def operacionImp(self):
        print "Terapeutico"


# Clase abstracta diferentes implementaciones
class Empleado(object):
    __metaclass__ = ABCMeta
    def __init__(self, accion):
        self.accion = accion

    @abstractmethod
    def operacion(self): pass

# Clase concreta, implementacion de clase abstracta
class Especialista(Empleado):
    def __init__(self, accion):
        super(Especialista, self).__init__(accion)

    def operacion(self):
        print "Riesgo identificado en area: "
        self.accion.operacionImp()
