#!/usr/bin/python

import abc

# Clase que conoce a sus observadores y los notifica en cambios
class TipoCuerpo:
    def __init__(self):
        self.observadores = set()
        self.estado_sujeto = None

    def attach(self, observer):
        observer._subject = self
        self.observadores.add(observer)

    def detach(self, observer):
        observer._subject = None
        self.observadores.discard(observer)

    def _notify(self):
        for observer in self.observadores:
            observer.update(self.estado_sujeto)

    @property
    def subject_state(self):
        return self.estado_sujeto

    @subject_state.setter
    def subject_state(self, arg):
        self.estado_sujeto = arg
        self._notify()


# Define una clase abstracta para los observadores
class DashboardObserver(metaclass=abc.ABCMeta):

    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass


# Clase contreta que observa los cambios en el sujeto
class DashUsuario(DashboardObserver):
    def update(self, arg):
        self._observer_state = arg
        print "estado de tipo cuerpo actualizado para Usuario"

# Clase concreta que observa los cambios en el sujeto
class DashAdministrador(DashboardObserver):
    def update(self, arg):
        self._observer_state = arg
        print "estado de tipo cuerpo actualizado para admin"


def main():
    subject = Subject()
    concrete_observer = ConcreteObserver()
    subject.attach(concrete_observer)
    subject.subject_state = 123
