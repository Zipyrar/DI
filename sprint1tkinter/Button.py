import tkinter as tk

#Crea la ventana principal.
w = tk.Tk()
w.title("Botones")
w.geometry("400x400")

#Muestra el texto al pulsar en el botón correspondiente.
def muestra():
    texto = tk.Label(w, text="¡Buenas!")
    texto.pack()
    
#'.destroy()/.quit() cierran la ventana.
def destruye():
    w.destroy()


#Crea un botón. 'command' llama a una función.
bot1 = tk.Button(w, text="Un botón", command=muestra)
#Posiciona.
bot1.pack()
bot2 = tk.Button(w, text="Cierra ventana", command=destruye)
bot2.pack()

#Ejecuta el bucle principal.
w.mainloop()