from Memento import Memento

class Snapshop:
    registro = []

    def __init__(self) -> None:
        pass

    def add(self, new) -> None:
        self.registro + [new]

    def search(self, token) -> list:
        