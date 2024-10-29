import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading

class ControladorNotas:
    def __init__(self, modelo, vista):
        #Llama a las clases 'NotasModel' y 'VistaNotas'
        self.modelo = modelo
        self.vista = vista
        
        #Añade a los botones sus respectivas funciones.
        self.vista.agrega.config(command=self.agregar_nota)
        self.vista.elimina.config(command=self.eliminar_nota)
        self.vista.guarda.config(command=self.guardar_notas)
        self.vista.carga.config(command=self.cargar_notas)
        self.vista.descarga.config(command=self.descargar_imagen)
        
        self.vista.v.bind("<Button-1>", self.actualizar_coordenadas)
        
    #Añade cada nota a la Listbox.
    def agregar_nota(self):
        nueva_nota = self.vista.cuadro.get()
        self.modelo.agregar_nota(nueva_nota)
        self.vista.cuadro.delete(0, tk.END)
        self.actualizar_listbox()
        
    #Elimina la nota seleccionada.
    def eliminar_nota(self):
        selecc = self.vista.lista.curselection()
        if selecc:
            indice = selecc[0]
            self.modelo.eliminar_nota(indice)
            self.actualizar_listbox()
            
    def guardar_notas(self):
        self.modelo.guardar_notas()
        messagebox.showinfo("Guardar Notas", "Notas guardadas con éxito.")
        
    def cargar_notas(self):
        self.modelo.cargar_notas()
        self.actualizar_listbox()
        
    def descargar_imagen(self):
        url = 'https://raw.githubusercontent.com/LaboratoriaChile/portafolio-sass/master/img/img_city.jpg'
        hilo = threading.Thread(target=self.iniciar_imagen, args=(url,))
        hilo.start()
        
    def iniciar_imagen(self, url):
        try:
            res = requests.get(url)
            res.raise_for_status()  #Lanza una excepción si la descarga falla.
            imagen = Image.open(BytesIO(res.content))
            imagen = imagen.resize((200, 200))
            imagen_tk = ImageTk.PhotoImage(imagen)
            
            #Actualizar la interfaz en el hilo principal.
            self.vista.imagen.config(image=imagen_tk)
            self.vista.imagen.image = imagen_tk  #Mantiene una referencia.
        except requests.exceptions.RequestException as e:
            #Manda un mensaje de error en caso de fallar.
            messagebox.showerror(f"Error al descargar la imagen: {e}")
            
    #Obtiene las coordenadas del clic izquierdo y las muestra.
    def actualizar_coordenadas(self, evento):
        self.modelo.actualizar_coordenadas(evento.x, evento.y)
        self.vista.coordenadas.config(text=f"Coordenadas: [{evento.x}] [{evento.y}]")
        
    #Actualiza la Lisbox para añadir las modificaciones.
    def actualizar_listbox(self):
        self.vista.lista.delete(0, tk.END)
        
        notas = self.modelo.obtener_notas()
        
        for nota in notas:
            self.vista.lista.insert(tk.END, nota)