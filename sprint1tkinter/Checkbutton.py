import tkinter as tk

#Crea la ventana principal.
w = tk.Tk()
w.title("Opciones a seleccionar")
w.geometry("600x400")

#Comprueba si se ha seleccionado la casilla.
def selecc_leer():
    selecc = check_lee.get()
    estado = "Seleccionado" if selecc else "No seleccionado"
    etiq_leer.config(text=f"Leer: {estado}")

def selecc_deporte():
    selecc = check_depor.get()
    estado = "Seleccionado" if selecc else "No seleccionado"
    etiq_deporte.config(text=f"Deportes: {estado}")
    
def selecc_musica():
    selecc = check_musica.get()
    estado = "Seleccionado" if selecc else "No seleccionado"
    etiq_musica.config(text=f"Música: {estado}")

#Crea variables para los Checkbuttons.
check_lee = tk.IntVar()
check_depor = tk.IntVar()
check_musica = tk.IntVar()

texto = tk.Label(w, text="Tus aficiones:")
texto.pack()

#Crea el Checkbutton.
leer = tk.Checkbutton(w, text="Leer", variable=check_lee, command=selecc_leer)
#Posiciona.
leer.pack(pady=10)
#Muestra su estado.
etiq_leer = tk.Label(w, text="Leer: No seleccionado")
etiq_leer.pack(pady=5)
deporte = tk.Checkbutton(w, text="Deportes", variable=check_depor, command=selecc_deporte)
deporte.pack(pady=10)
etiq_deporte = tk.Label(w, text="Deportes: No seleccionado")
etiq_deporte.pack(pady=5)
musica = tk.Checkbutton(w, text="Música", variable=check_musica, command=selecc_musica)
musica.pack(pady=10)
etiq_musica = tk.Label(w, text="Música: No seleccionado")
etiq_musica.pack(pady=5)

#Ejecuta el bucle principal.
w.mainloop()