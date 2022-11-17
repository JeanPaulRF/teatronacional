from modelo.patterns.Memento import Memento

class Snapshop:
    registro = []

    def __init__(self):
        self.registro = []

    def add(self, new) -> None:
        self.registro + [new]

    def search(self, token) -> list:
        res = []
        for i in self.registro:
            if (i.codigo == token):
                res += [i]
            return  res