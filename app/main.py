import tkinter as tk
from controller.controlador_principal import ControladorPrincipal

root = tk.Tk()
root.title("evento en la Zona")
controlador = ControladorPrincipal(root)
root.mainloop()
