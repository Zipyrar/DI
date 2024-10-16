import tkinter as tk

#Crea la ventana principal.
w = tk.Tk()
w.title("Frame")
w.geometry("500x500")

#Crea un Frame.
fr_sup = tk.Frame(w, bg="lightblue")
fr_sup.pack(padx=50, pady=20, fill="both")

#Añade al Frame.
et1_sup = tk.Label(fr_sup, text="Buenas tardes.", bg="lightblue")
et1_sup.pack(pady=5)
et2_sup = tk.Label(fr_sup, text="Me estoy muriendo de cansancio.", bg="lightblue")
et2_sup.pack(pady=5)
estado = tk.Label(fr_sup, text="Teclea tu estado:", bg="lightblue")
estado.pack(pady=10)
cuadro = tk.Entry(fr_sup, width=20)
cuadro.pack(pady=5)

def estado():
    tu_estado = cuadro.get()
    dialogo.config(text=f"Estoy {tu_estado}", bg="lightgrey")
    
def borra():
    borra = cuadro.get()
    dialogo.config(text="", bg="lightgrey")
    
#Crea otro Frame.
fr_inf = tk.Frame(w, bg="lightgrey")
fr_inf.pack(padx=50, pady=20, fill="both")

bot1 = tk.Button(fr_inf, text="Muestra estado", bg="lightgrey", command=estado)
bot1.pack(pady=5)
dialogo = tk.Label(fr_inf, text="", bg="lightgrey")
dialogo.pack(pady=5)
bot2 = tk.Button(fr_inf, text="Borrar estado", bg="lightgrey", command=borra)
bot2.pack(pady=5)

#Ejecuta el bucle principal.
w.mainloop()