import json

class Eventos:
    def __init__(self, nombre, imagen, genero, artista, descripcion, hora_inicio, hora_fin, id_ubicacion):
        self.nombre = nombre
        self.imagen = imagen
        self.genero = genero
        self.artista = artista
        self.descripcion = descripcion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.id_ubicacion = id_ubicacion

    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_eventos(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Eventos.de_json(json.dumps(dato)) for dato in datos]