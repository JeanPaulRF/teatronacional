from modelo.patterns.Memento import Memento

class Historial():
    def __init__(self):
        self._historial = []
    
    def add(self, memento):
        print("Agregando memento")
        self._historial.append(memento)
    
    def get(self, index):
        return self._historial[index]

    def isEmpy(self):
        return len(self._historial) == 0