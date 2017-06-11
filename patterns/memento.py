#!/usr/bin/python

import pickle

# Clase a la cual se le generara el memento
class Rutina(object):
    def __init__(self, arg):
        super(Rutina, self).__init__()
        self.arg = arg

# Controla la generacion del estado del memento y la obtencion de este
class RutinaMemento(object):
    def __init__(self):
        self.rutina = Rutina()
        self.originator = Originator()

    def set_state(self):
        originator.create_memento(self.rutina)

    def get_state(self):
        originator.set_memento(self.rutina

# Crea un momento conteniendo una captura del estado actual del objeto
class Originator(object):
    def __init__(self):
        self._state = None

    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previous_state)

    def create_memento(self):
        return pickle.dumps(vars(self))


def main():
    originator = Originator()
    memento = originator.create_memento()
    originator._state = True
    originator.set_memento(memento)
