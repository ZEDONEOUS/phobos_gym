from interface import Interface, implements

# interface definicion de especialistas
class Especialista(Interface):
    def operacion(self): pass

# Definicion de implementacion de interface de especialistas
class Fisioterapeuta(implements(Especialista)):
    def operacion(self):
        print "Recomendacion de fisioterapeuta"

# Extencion que se desea implementar
class Nutricionista(Interface):
    def operacion(self): pass

# Adaptador para uso de extencion junto con lo que ya se tiene
class AdapterEspecialidad(implements(Nutricionista)):
    def __init__(self, actual):
        self.actual = actual

    def operacion(self):
        print "Recomendacion nutricionistica"
        self.actual.operacion()
