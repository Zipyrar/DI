#Importa el tkinter.
import tkinter as tk

#Crea la ventana principal.
w = tk.Tk()
w.title("Textos")
w.geometry("400x400")

def cambiante():
    #Configura la etiqueta para cambiarle el texto.
    tag3.config(text="Texto cambiado.")
    
#Crea una etiqueta de texto.
tag1 = tk.Label(w, text="¡Bienvenido!")
#Posiciona el elemento.
tag1.pack()
tag2 = tk.Label(w, text="Alonso")
tag2.pack()
tag3 = tk.Label(w, text="Buenas tardes.")
tag3.pack()
#Crea un botón que usa una función.
sw = tk.Button(w, text="Un botón", command=cambiante)
sw.pack()

#Ejecuta el bucle principal.
w.mainloop()