from views.vista_principal import VistaPrincipal
from models.evento import Eventos
from models.ubicacion import Ubicacion
from PIL import Image, ImageTk

class ControladorPrincipal:
    def __init__(self, root):
        self.vista = VistaPrincipal(root, self.seleccionar_evento, seleccionar_ubicacion)
        self.eventos = Eventos.cargar_eventos("app/data/eventos.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("app/data/ubicaciones.json")
        self.imagenes = []

        self.cargar_eventos()
        self.cargar_imagenes()
        self.cargar_marcadores()

    def cargar_eventos(self):
        for local in self.eventos:
            self.vista.agregar_evento(Eventos)
        
    def cargar_imagenes(self):
        for evento in self.eventos:
            imagen = ImageTk.PhotoImage(Image.open(f"app/views/images/{evento.imagen}").resize((200, 200)))
            self.imagenes.append(imagen)

    def cargar_marcadores(self):
        for ubicacion, evento in zip(self.ubicaciones, self.evento):
            imagen = self.imagenes[ubicacion.id - 1]
            marcador = self.vista.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud, ubicacion.localidad, evento.nombre, imagen)
            marcador.hide_image(True)
            self.marcadores.append(marcador)

    def seleccionar_evento(self, event):
        # Obtiene el índice del elemento seleccionado
        indice_seleccionado = self.vista.lista_evento.curselection()
        # Obtiene el evento seleccionado
        evento_seleccionado = self.evento[indice_seleccionado[0]]
        
        ubicacion_seleccionada = Ubicacion(0, 0, 0, "")
        
        # Busca la ubicación correspondiente al local seleccionado
        for ubicacion in self.ubicaciones:
            if ubicacion.id == evento_seleccionado.id_ubicacion:
                ubicacion_seleccionada = ubicacion
                break
        
        # Centra el mapa en la ubicación seleccionada
        self.vista.mapa.set_position(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud, ubicacion_seleccionada.localidad)

        print(f"Latitud: {ubicacion_seleccionada.latitud}, Longitud: {ubicacion_seleccionada.longitud}, localidad: {ubicacion_seleccionada.localidad}")

def seleccionar_ubicacion(marcador):
    if marcador.image_hidden is True:
        marcador.hide_image(False)
    else:
        marcador.hide_image(True)
    print("Ubicación seleccionada: ", marcador.text)
