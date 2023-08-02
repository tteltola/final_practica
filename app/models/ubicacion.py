import json

class Ubicacion:
    def __init__(self, id, direccion, localiadad, latitud, longitud):
        self.id = id
        self.direccion = direccion
        self.localidad = localiadad
        self.latitud = latitud
        self.longitud = longitud
        
    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_ubicaciones(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Ubicacion.de_json(json.dumps(dato)) for dato in datos]
