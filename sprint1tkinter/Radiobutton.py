import tkinter as tk

w = tk.Tk()
w.title("Opciones a seleccionar")
w.geometry("600x400")

colores = {
    "rojo":"red",
    "verde":"green",
    "azul":"blue"
}

def muestra():
    selecc = val_radio.get()
    res.config(text=f"Seleccionaste el color {selecc}.")
    w.config(bg=colores[selecc])
    

val_radio = tk.StringVar()
val_radio.set("rojo")

texto = tk.Label(w, text="Seleccione color:")
texto.pack(pady=10)

c1 = tk.Radiobutton(w, text="Rojo", variable=val_radio, value="rojo", command=muestra)
c1.pack(pady=5)
c2 = tk.Radiobutton(w, text="Verde", variable=val_radio, value="verde", command=muestra)
c2.pack(pady=5)
c3 = tk.Radiobutton(w, text="Azul", variable=val_radio, value="azul", command=muestra)
c3.pack(pady=5)

res = tk.Label(w, text="Seleccionaste el color rojo.")
res.pack(pady=10)

w.mainloop()