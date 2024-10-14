import tkinter as tk

w = tk.Tk()
w.title("Lista")
w.geometry("600x400")

def muestra():
    selecc = lista.curselection()
    elemento = [lista.get(i) for i in selecc]
    res.config(text=f"Seleccionaste {"".join(elemento)}")

frutas = ["Manzana", "Naranja", "Plátano", "Granada", "Fresa", "Mango"]

lista = tk.Listbox(w, selectmode=tk.SINGLE)
for fruta in frutas:
    lista.insert(tk.END, fruta)
lista.pack(pady=15)

bot = tk.Button(w, text="Mostrar fruta", command=muestra)
bot.pack(pady=5)

res = tk.Label(w, text="No seleccionaste ninguna fruta.")
res.pack(pady=10)

w.mainloop()