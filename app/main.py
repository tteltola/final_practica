import tkinter as tk
from models.evento import Eventos
from models.ubicacion import Ubicacion
from models.usuario import Usuario
from views.vista_inicio import VistaInicio
from views.vista_eventos import VistaEventos
from views.vista_info import VistaInfo
from views.vista_principal import VistaPrincipal
from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_eventos import ControladorEventos
from controllers.controlador_info import ControladorInfo
from controllers.controlador_principal import ControladorPrincipal


class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("MusicTour")
        self.geometry("330x600")
        self.resizable(False, False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        eventos = Eventos.cargar_eventos("data/evento.json")
        Ubicacion = Ubicacion.cargar_ubicaciones("data/ubicacion.json")
        Usuario = Usuario.cargar_usuarios("data/usuario.json")
        controlador_inicio = ControladorInicio(self)
        controlador_eventos = ControladorEventos(self, eventos)
        controlador_info = ControladorInfo(self)
        controlador_principal = ControladorPrincipal

        self.views_inicio = VistaInicio(self, controlador_inicio)
        self.views = VistaPrincipal(self, controlador_principal)
        self.views_eventos = VistaEventos(self, controlador_eventos)
        self.views_info = VistaInfo(self, controlador_info)

        self.ajustar_frame(self.views_inicio)
        self.ajustar_frame(self.views_eventos)
        self.ajustar_frame(self.views_info)
        self.ajustar_frame(self.views_principal)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
