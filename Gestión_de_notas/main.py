import tkinter as tk
from notasModel import NotasModel
from vistaNotas import VistaNotas
from controladorNotas import ControladorNotas

def main():
    #Crea la ventana principal.
    v = tk.Tk()
    #Llama a los demás archivos.
    modelo = NotasModel([])
    vista = VistaNotas(v)
    controlador = ControladorNotas(modelo, vista)
    #Ejecuta el bucle principal.
    v.mainloop()

if __name__ == "__main__":
    main()