import tkinter as tk

class VistaNotas:
    def __init__(self, v):
        #Llama a la ventana principal.
        self.v = v

        self.titulo = tk.Label(v, text="Gestión de notas")
        self.titulo.pack()
    
        self.lista = tk.Listbox(v, selectmode=tk.SINGLE)
        self.lista.pack()
    
        self.cuadro = tk.Entry(v, width=20)
        self.cuadro.pack()

        self.agrega = tk.Button(v, text="Agregar nota")
        self.agrega.pack()
        self.elimina = tk.Button(v, text="Eliminar nota")
        self.elimina.pack()
        self.guarda = tk.Button(v, text="Guardar notas")
        self.guarda.pack()
        self.carga = tk.Button(v, text="Cargar notas")
        self.carga.pack()
        self.descarga = tk.Button(v, text="Descargar imagen")
        self.descarga.pack()
        
        self.coordenadas = tk.Label(v, text="")
        self.coordenadas.pack()
    
        self.imagen = tk.Label(v, text="")
        self.imagen.pack()