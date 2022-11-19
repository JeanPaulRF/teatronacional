from modelo.patterns.Observer import Observer
from modelo.patterns.Snapshopin import Snapshopin
from pathlib import Path
# from teatro.settings import BASE_DIR

class Log:
    registro = []
    fileR = None
    fileW = None
    BASE_DIR = Path(__file__).resolve().parent.parent
    def __init__(self):
        self.registro = []

    def add(self, new) -> None:
        self.registro + [new]

    def write(self, data) -> None:
        self.fileW = open(self.BASE_DIR / 'static/logs.txt', "a")
        print(data.getDatos())
        res = "Id:" + str(data.codigo) + "-/*\n"
        res += "TResultado:" + data.tResultado + "-/*\n"
        res += "Comentario:" + data.comentario + "-/*\n"
        res += "FechaInicio:" + data.fechaInicio+ "-/*\n"
        res += "FechaFin:" + data.fechaFin + "-/*\n"
        res += "Encargado:" + data.encargado + "-/*\n"
        res += "Area:" + data.area + "-/*\n"
        res += "TEstado:" + data.tEstado + "-/*\n"
        res += "Completada:" + str(data.completada) + "-/*\n"
        res += "----#----\n"
        self.fileW.write(res)
        self.fileW.close()

    def search(self, token) -> list:
        res = []
        for i in self.registro:
            if (i.codigo == token):
                res += [i]
            return  res

    def tranforn(self, data):
        # print(data)
        lista = data.split("----#----\n")
        print(lista)
        print("\n\n")
        for i in lista:
            if (i != ""):
                dato = data.split("-/*\n")
                dato.pop(-1)
                print(dato)
                a = {
                    "Id" : dato[-1].split(":")[1],
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
        self.fileR = open(self.BASE_DIR / 'static/logs.txt', "r")
        mensaje = self.fileR.read()
        print(mensaje)
        if (mensaje != ""):
            self.tranforn(mensaje)
        self.fileR.close()