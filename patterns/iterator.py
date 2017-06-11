#!/usr/bin/python

import collections.abc

# Implementa la interface de coleccion iterable para hacer un objeto iterable
class ConcreteAggregate(collections.abc.Iterable):
    def __init__(self):
        self._data = None

    def __iter__(self):
        return ConcreteIteratorEjercicios(self)


# Implementa la interface de coleccion iterador
class ConcreteIteratorEjercicios(collections.abc.Iterator):
    def __init__(self, concrete_aggregate):
        self._concrete_aggregate = concrete_aggregate

    def __next__(self):
        if True:
            raise StopIteration
        return "Ejercicio Sentadillas"


def main():
    concrete_aggregate = ConcreteAggregate()
    for _ in concrete_aggregate:
        pass
