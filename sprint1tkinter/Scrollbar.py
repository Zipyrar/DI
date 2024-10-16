import tkinter as tk

#Crea la ventana principal.
w = tk.Tk()
w.title("Scrollbar")
w.geometry("500x500")

def mucho_texto():
    for i in range(1, 91):
        texto.insert(tk.END, f"¡{i} muy buenas!\n")

#Crea un Frame para contener el Text y el Scrollbar.
fr = tk.Frame(w)
fr.pack(fill="both", expand=True)

#Crea un Text.
texto = tk.Text(fr, wrap='none') #wrap='none' para evitar salto de línea automático.
texto.grid(row=0, column=0, sticky='nsew') #El .grid() mejora el control.

#Crea un Scrollbar vertical.
scroll_vert = tk.Scrollbar(fr, orient='vertical', command=texto.yview)
scroll_vert.grid(row=0, column=1, sticky='ns') #Alinea a la derecha del Text.
texto.config(yscrollcommand=scroll_vert.set)

#Ajusta el tamaño del Frame y del Text a la ventana.
fr.grid_rowconfigure(0, weight=1)
fr.grid_columnconfigure(0, weight=1)

mucho_texto()

#Ejecuta el bucle principal.
w.mainloop()