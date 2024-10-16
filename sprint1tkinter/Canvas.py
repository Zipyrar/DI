import tkinter as tk

#Crea la ventana principal.
w = tk.Tk()
w.title("Canvas")
w.geometry("500x500")

def dibujo():
    #Pasa los datos a números enteros.
    cX1, cY1, cX2, cY2 = map(int, cuadro_ctam.get().split(","))
    
    rX1, rY1, rX2, rY2 = map(int, cuadro_rectam.get().split(","))
    
    canvas.delete("all")
    
    #Dibuja las figuras.
    canvas.create_oval(cX1, cY1, cX2, cY2, fill="orange")
    canvas.create_rectangle(rX1, rY1, rY1, rY2, fill="blue")
    

circ_tam = tk.Label(w, text="Introduce el tamaño del círculo (x1, y1, x2, y2):")
circ_tam.pack()
#Crea cuadros de entrada para los datos de las figuras.
cuadro_ctam = tk.Entry(w, width=30)
cuadro_ctam.pack(pady=5)
rect_tam = tk.Label(w, text="Introduce el tamaño del rectángulo (x1, y1, x2, y2):")
rect_tam.pack()
cuadro_rectam = tk.Entry(w, width=30)
cuadro_rectam.pack(pady=5)

bot = tk.Button(w, text="Dibujar figuras", command=dibujo)
bot.pack(pady=10)

#Crea un Canvas.
canvas = tk.Canvas(width=400, height=400, bg="white")
canvas.pack(pady=50)

#Ejecuta el bucle principal.
w.mainloop()