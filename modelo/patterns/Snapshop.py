from Memento import Memento

class Snapshop(Memento):
    def __init__(self):
        self.codigo = ""
    
    def setDatos(self, datos):
        self.codigo = datos.codigo
        self.registros = datos.registros
        self.fechaInicio = datos.fechaInicio
        self.fechaFin = datos.fechaFin
        self.tResultado = datos.tResultado
        self.tEstado = datos.tEstado
        self.encargado = datos.encargado
        self.area = datos.area
        self.comentario = datos.comentario
        self.completada = datos.completada

    def getDatos(self):
        return {
            "codigo" : self.codigo,
            "registros" : self.registros,
            "fechaInicio" : self.fechaInicio,
            "fechaFin" : self.fechaFin,
            "tResultado" : self.tResultado,
            "tEstado" : self.tEstado,
            "encargado" : self.encargado,
            "area" : self.area,
            "comentario" : self.comentario,
            "completada" : self.completada,
        }