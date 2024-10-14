import tkinter as tk

w = tk.Tk()
w.title("Botones")
w.geometry("400x400")

def muestra():
    texto = tk.Label(w, text="¡Buenas!")
    texto.pack()
    
def destruye():
    w.destroy()



bot1 = tk.Button(w, text="Un botón", command=muestra)
bot1.pack()
bot2 = tk.Button(w, text="Cierra ventana", command=destruye)
bot2.pack()

w.mainloop()