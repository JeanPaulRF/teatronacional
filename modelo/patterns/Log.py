from modelo.patterns.Memento import Memento
from modelo.patterns.Snapshopin import Snapshopin
from pathlib import Path
# from teatro.settings import BASE_DIR

class Log:
    registro = []
    file = None
    BASE_DIR = Path(__file__).resolve().parent.parent
    def __init__(self):
        self.registro = []
        self.openFile()

    def openFile(self) -> None:
        self.file = open(self.BASE_DIR / 'static/logs.txt', "r")
    
    def closeFile(self) -> None:
        self.file.close()

    def add(self, new) -> None:
        self.registro + [new]

    def search(self, token) -> list:
        res = []
        for i in self.registro:
            if (i.codigo == token):
                res += [i]
            return  res

    def tranforn(self, data):
        print(data)
        dato = data.split("-/*\n")
        dato.pop(-1)
        a = {
            "Codigo" : dato[-1].split(":")[1],
            "FechaInicio" : dato[3].split(":")[1],
            "FechaFin" : dato[4].split(":")[1],
            "TResultado" : dato[0].split(":")[1],
            "TEstado" : dato[1].split(":")[1],
            "Encargado" : dato[5].split(":")[1],
            "Area" : dato[6].split(":")[1],
            "Comentario" : dato[2].split(":")[1],
            "Completada" : dato[-1].split(":")[1],
        }
        self.add(Snapshopin(a))

    def readFile(self):
        mensaje = self.file.read()
        # self.add(mensaje)
        # print(BASE_DIR)
        self.tranforn(mensaje)