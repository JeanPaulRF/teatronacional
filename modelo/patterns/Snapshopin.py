from modelo.patterns.Observer import Observer

class Snapshopin(Observer):
    def __init__(self, datos):
        self.setDatos(datos)
    
    def setDatos(self, datos):
        self.codigo = datos["Id"]
        self.fechaInicio = datos["FechaInicio"]
        self.fechaFin = datos["FechaFin"]
        self.tResultado = datos["TResultado"]
        self.tEstado = datos["TEstado"]
        self.encargado = datos["Encargado"]
        self.area = datos["Area"]
        self.comentario = datos["Comentario"]
        self.completada = datos["Completada"]

    def getDatos(self):
        return {
            "Id" : self.codigo,
            "FechaInicio" : self.fechaInicio,
            "FechaFin" : self.fechaFin,
            "TResultado" : self.tResultado,
            "TEstado" : self.tEstado,
            "Encargado" : self.encargado,
            "Area" : self.area,
            "Comentario" : self.comentario,
            "Completada" : self.completada,
        }