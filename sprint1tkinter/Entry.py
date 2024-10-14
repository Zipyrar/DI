import tkinter as tk

w = tk.Tk()
w.title("Escribir")
w.geometry("600x400")

def obt_texto():
    nomb = cuadro.get()
    saludo.config(text=f"¡Saludos, {nomb}!")
    

pregunta = tk.Label(w, text="Pon tu nombre: ")
pregunta.pack()
cuadro = tk.Entry(w, width=20)
cuadro.pack(pady=5)

bot = tk.Button(w, text="Mostrar saludo", command=obt_texto)
bot.pack(pady=5)

saludo = tk.Label(w, text="")
saludo.pack(pady=5)

w.mainloop()