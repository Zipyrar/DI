import tkinter as tk

w = tk.Tk()
w.title("Textos")
w.geometry("400x400")

def cambiante():
    tag3.config(text="Texto cambiado.")

tag1 = tk.Label(w, text="¡Bienvenido!")
tag1.pack()
tag2 = tk.Label(w, text="Alonso")
tag2.pack()
tag3 = tk.Label(w, text="Buenas tardes.")
tag3.pack()
sw = tk.Button(w, text="Un botón", command=cambiante)
sw.pack()

w.mainloop()