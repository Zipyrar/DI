import tkinter as tk

#Crea la ventana principal.
w = tk.Tk()
w.title("Lista")
w.geometry("600x400")

#Comprueba la selección.
def muestra():
    selecc = lista.curselection()
    elemento = [lista.get(i) for i in selecc]
    res.config(text=f"Seleccionaste {"".join(elemento)}")

#Crea lista de opciones.
frutas = ["Manzana", "Naranja", "Plátano", "Granada", "Fresa", "Mango"]

#Crea una listbox, que solo puede elegir un elemento.
lista = tk.Listbox(w, selectmode=tk.SINGLE)
for fruta in frutas:
    lista.insert(tk.END, fruta) #Inserta en la listbox los elementos.
lista.pack(pady=15) #Posiciona.

bot = tk.Button(w, text="Mostrar fruta", command=muestra)
bot.pack(pady=5)

#Muestra la selección.
res = tk.Label(w, text="No seleccionaste ninguna fruta.")
res.pack(pady=10)

#Ejecuta el bucle principal.
w.mainloop()