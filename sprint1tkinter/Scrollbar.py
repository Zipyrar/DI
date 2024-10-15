import tkinter as tk

w = tk.Tk()
w.title("Scrollbar")
w.geometry("500x500")

def mucho_texto():
    for i in range(1, 91):
        texto.insert(tk.END, f"¡{i} muy buenas!\n")

fr = tk.Frame(w)
fr.pack(fill="both", expand=True)

texto = tk.Text(fr, wrap='none')
texto.grid(row=0, column=0, sticky='nsew')

scroll_vert = tk.Scrollbar(fr, orient='vertical', command=texto.yview)
scroll_vert.grid(row=0, column=1, sticky='ns')
texto.config(yscrollcommand=scroll_vert.set)

fr.grid_rowconfigure(0, weight=1)
fr.grid_columnconfigure(0, weight=1)

mucho_texto()

w.mainloop()