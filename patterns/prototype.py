#!/usr/bin/python

import copy

# Definicion de objeto prototipo
# que puede ser clonado
class PrototipoEquipos:

    _type  = None
    _value = None

    def clone(self):
        pass

    def getType(self):
        return self._type

    def getValue(self):
        return self._value

# Definicion del objeto basado en el prototipo
class EquipoBicicleta(PrototipoEquipos):
    def __init__(self, number):
        self._type = "Equipo Bicicleta"
        self._value = number

    def clone(self):
        return copy.copy(self)

# Definicion del objeto basado en el prototipo
class EquipoMancuernas(PrototipoEquipos):
    def __init__(self, number):
        self._type = "Equipo Mancuernas"
        self._value = number

    def clone(self):
        return copy.copy(self)

# Administra los objetos creados a base de los prototipos
class FabricaEquipos:

    __type1Value1 = None
    __type1Value2 = None
    __type2Value1 = None
    __type2Value2 = None

    @staticmethod
    def initialize():
        FabricaEquipos.__type1Value1 = EquipoBicicleta(1)
        FabricaEquipos.__type1Value2 = EquipoBicicleta(2)
        FabricaEquipos.__type2Value1 = EquipoMancuernas(1)
        FabricaEquipos.__type2Value2 = EquipoMancuernas(2)

    @staticmethod
    def getEquipoBicicletaValue1():
        return FabricaEquipos.__type1Value1.clone()

    @staticmethod
    def getEquipoBicicletaValue2():
        return FabricaEquipos.__type1Value2.clone()

    @staticmethod
    def getEquipoMancuernasValue1():
        return FabricaEquipos.__type2Value1.clone()

    @staticmethod
    def getEquipoMancuernasValue2():
        return FabricaEquipos.__type2Value2.clone()


def main():
    FabricaEquipos.initialize()

    instance = FabricaEquipos.getEquipoBicicletaValue1()
    print "%s: %s" % (instance.getType(), instance.getValue())

    instance = FabricaEquipos.getEquipoBicicletaValue2()
    print "%s: %s" % (instance.getType(), instance.getValue())

    instance = FabricaEquipos.getEquipoMancuernasValue1()
    print "%s: %s" % (instance.getType(), instance.getValue())

    instance = FabricaEquipos.getEquipoMancuernasValue2()
    print "%s: %s" % (instance.getType(), instance.getValue())
