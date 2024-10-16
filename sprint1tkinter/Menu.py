import tkinter as tk
from tkinter import messagebox 

#Crea la ventana principal.
w = tk.Tk()
w.title("Menu")
w.geometry("500x500")

#Crea la barra de menú.
menu_principal = tk.Menu(w)
w.config(menu=menu_principal)

#Crea una ventana con un mensaje.
def info():
    messagebox.showinfo("Información", "Este es un menú de ejemplo.")

#Crea un submenú llamado 'Archivo'.
menu_archivo = tk.Menu(menu_principal, tearoff=0) #tearoff elimina unas líneas.
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
#Añade opciones al submenú.
menu_archivo.add_command(label="Abrir")
#Añade una línea de separación.
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=w.quit)

menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=info)

#Ejecuta el bucle principal.
w.mainloop()