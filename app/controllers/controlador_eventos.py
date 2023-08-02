class ControladorEventos:
    def __init__(self, app, modelo_app):
        self.app = app
        self.modelo_app = modelo_app

    def obtener_eventos(self):
        return self.modelo_app

    def seleccionar_evento(self):
        """
        Obtiene el índice del evento seleccionado y llama a la vista de
        información para mostrar la información del evento.
        """
        indice = self.app.vista_app.obtener_evento_seleccionado()
        if indice is not None:
            evento = self.modelo_app[indice]
            self.app.vista_info.mostrar_info_app(evento)
            self.app.cambiar_frame(self.app.vista_info)

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
