import tkinter as tk

#Crea la ventana principal.
w = tk.Tk()
w.title("Scale")
w.geometry("500x500")

def act_valor(val):
    valor.config(text=f"Valor: {val}")

#Crea un Scale horinzontal.
escala = tk.Scale(w, from_=0, to=100, orient='horizontal', command=act_valor)
escala.pack(pady=20)

#Muestra el valor seleccionado a tiempo real.
valor = tk.Label(w, text="Valor: 0")
valor.pack(pady=10)

#Ejecuta el bucle principal.
w.mainloop()