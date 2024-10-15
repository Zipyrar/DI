import tkinter as tk
from tkinter import messagebox

w = tk.Tk()
w.title("Menu")
w.geometry("500x500")

menu_principal = tk.Menu(w)
w.config(menu=menu_principal)

def info():
    messagebox.showinfo("Información", "Este es un menu de ejemplo.")

menu_archivo = tk.Menu(menu_principal, tearoff=0) #tearoff elimina unas líneas.
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=w.quit)

menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=info)

w.mainloop()