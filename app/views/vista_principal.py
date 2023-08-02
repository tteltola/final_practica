import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk

class VistaPrincipal:
    def __init__(self, root, controlador=None):
        self.root = root
        self.controlador = controlador
        self.frame_mapa = tk.Frame(self.root, width=600, height=600)
        self.frame_mapa.pack(side='right')

        self.frame_eventos = tk.Frame(self.root, width=300, height=600)
        self.frame_eventos.pack(side='left', fill='both', expand=True)

        # Placeholder para el mapa
        self.mapa = TkinterMapView(self.frame_mapa, width=600, height=600, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.pack(side='right')

        # Listbox para los evento
        self.lista_eventos = tk.Listbox(self.frame_eventos)
        self.lista_eventos.bind('<<ListboxSelect>>', self.controlador.seleccionar_evento)
        self.lista_eventos.pack(fill='both', expand=True)

    def agregar_evento(self, evento):
        self.evento = evento
        self.lista_eventos.insert(tk.END, evento)
        
    def agregar_marcador_mapa(self, latitud, longitud, localidad, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, localidad, text=texto, image=imagen, command=self.controlador.seleccionar_ubicacion)
    