import tkinter as tk

#Crea la ventana principal.
w = tk.Tk()
w.title("Escribir")
w.geometry("600x400")

def obt_texto():
    #Obtiene el campo de entrada.
    nomb = cuadro.get()
    saludo.config(text=f"¡Saludos, {nomb}!")
    
#Crea un texto para preguntar.
pregunta = tk.Label(w, text="Pon tu nombre: ")
#Posiciona.
pregunta.pack()
#Crea un campo de entrada.
cuadro = tk.Entry(w, width=20)
cuadro.pack(pady=5) #Añade espacio en vetical.

#Botón que muestra lo puesto en el campo de entrada.
bot = tk.Button(w, text="Mostrar saludo", command=obt_texto)
bot.pack(pady=5)

#Texto vacío para sustituir.
saludo = tk.Label(w, text="")
saludo.pack(pady=5)

#Ejecuta el bucle principal.
w.mainloop()