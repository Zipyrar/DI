import tkinter as tk
from tkinter import messagebox

#Crea la ventana principal.
w = tk.Tk()
w.title("Registro")
w.geometry("600x600")

def lista_usuarios():
    #Consigue los datos para pasarlos a una Listbox.
    nombre = cuadro_nomb.get()
    edad =  esc_edad.get()
    sexo = genero.get()
    
    #Comprueba que no falten datos por poner.
    if nombre != "" and sexo != "None":
        lista.insert(tk.END, f"Nombre: {nombre}  Edad: {edad}  Sexo: {sexo}")
    else:
        messagebox.showwarning("Advertencia", "Faltan datos por poner.")
        
    limpia_usuario()

#Borra los datos
def limpia_usuario():
    cuadro_nomb.delete(0, tk.END)
    esc_edad.set(0)
    genero.set("None")
    
#Borra un usuario seleccionado de la lista.
def limpia_usuario_lista():
    selecc = lista.curselection()
    
    #Comprueba que se haya seleccionado a un usuario.
    if selecc:
        lista.delete(selecc)
    else:
        messagebox.showwarning("Advertencia", "No ha seleccionado un usuario para eliminar.")
        

nomb = tk.Label(w, text="Introduzca su nombre:")
nomb.pack(pady=5)
#Crea un campo de entrada.
cuadro_nomb = tk.Entry(w, width=20)
cuadro_nomb.pack(pady=15) 

intro_edad = tk.Label(w, text="Seleccione su edad:")
intro_edad.pack(pady=5)
#Crea un Scale para poner la edad.
esc_edad = tk.Scale(w, from_=0, to=100, orient='horizontal')
esc_edad.pack(pady=5)

#Crea una variable para el género.
genero = tk.StringVar()
genero.set("None")
texto_genero = tk.Label(w, text="Seleccione su género:")
texto_genero.pack(pady=10)

#Crea un Frame para posicionar los Checkbuttons uno al lado del otro.
fr_g = tk.Frame(w)
fr_g.pack(pady=5)

g1 = tk.Radiobutton(fr_g, text="Masculino", variable=genero, value="Masculino")
g1.pack(side="left")
g2 = tk.Radiobutton(fr_g, text="Femenino", variable=genero, value="Femenino")
g2.pack(side="left")
g3 = tk.Radiobutton(fr_g, text="Otro", variable=genero, value="Otro")
g3.pack(side="left")

fr_bot = tk.Frame(w)
fr_bot.pack(pady=5)

#Botón que añade un usuario a la lista.
bot_agre = tk.Button(fr_bot, text="Añadir a la lista", command=lista_usuarios)
bot_agre.pack(side='left', padx=10)

#Botón que elimina un usuario de la lista.
bot_elim = tk.Button(fr_bot, text="Eliminar usuario", command=limpia_usuario_lista)
bot_elim.pack(side='left', padx=10)

#Cierra la ventana gracias al '.quit()'.
bot_elim = tk.Button(fr_bot, text="Salir", command=w.quit)
bot_elim.pack(side='left', padx=10)

fr_lista = tk.Frame(w)
fr_lista.pack(pady=5, fill='both', expand=True)

#Crea una Lisbox en la que solo se puede seleccionar un usuario.
lista = tk.Listbox(fr_lista, selectmode=tk.SINGLE, width=50)
lista.pack(side='left', fill='both', expand=True)  

#Crea un Scrollbar vertical.
scroll_vert = tk.Scrollbar(fr_lista, orient='vertical', command=lista.yview)
scroll_vert.pack(side='right', fill='y') #Alinea a la derecha de la Listbox.

lista.config(yscrollcommand=scroll_vert.set)

selecc = lista.curselection()

#Crea una barra de menú.
menu_principal = tk.Menu(w)
w.config(menu=menu_principal)

def info_guarda():
    messagebox.showinfo("Guardar", "Lista guardada con éxito.")
    
def info_carga():
    messagebox.showinfo("Cargar", "Lista cargada con éxito.")

#Crea un submenú llamado 'Archivo'.
menu_archivo = tk.Menu(menu_principal, tearoff=0) #tearoff elimina unas líneas.
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
#Añade opciones al submenú.
menu_archivo.add_command(label="Guardar lista", command=info_guarda)
menu_archivo.add_separator()
menu_archivo.add_command(label="Cargar lista", command=info_carga)

#Ejecuta el bucle principal.
w.mainloop()