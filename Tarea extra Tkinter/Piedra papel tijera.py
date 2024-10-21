import tkinter as tk
import random

#Crea la ventana principal.
w = tk.Tk()
w.title("Piedra, papel o tijera")
w.geometry("600x600")  

#Crea la barra de menú.
menu_prin = tk.Menu(w)
w.config(menu=menu_prin)

#Inicia los puntos para los jugadores y la máquina.
pj = 0  # Puntos jugador 1.
pj2 = 0  # Puntos jugador 2.
pm = 0  # Puntos de la máquina.

#Texto inicial que cambia según la situación del juego.
texto = tk.Label(w, text="Seleccione el modo de juego en el menú.", font=("Arial", 20))
texto.pack(pady=40)

#Lista de posibles elecciones de la máquina.
elecc = ["Piedra", "Papel", "Tijeras"]

#Botones para seleccionar piedra, papel o tijeras.
b_piedra = tk.Button(w, text="Piedra")
b_papel = tk.Button(w, text="Papel")
b_tijeras = tk.Button(w, text="Tijeras")

#Elección inicial del jugador 1 (vacía al inicio).
elecc_j1 = None

#Etiquetas para mostrar el resultado de la jugada y mensajes de victoria.
res = tk.Label(w, text="", font=("Arial", 15))
res.pack(pady=10)

#Mensaje de felicitaciones cuando uno de los jugadores gana.
mens = tk.Label(w, text="", font=("Arial", 15))
mens.place(x=300, y=400, anchor="center")

#Etiqueta para mostrar los puntos de los participantes.
puntos = tk.Label(w, text="")

#Función para iniciar el modo de juego contra la máquina.
def vs_maquina():
    texto.config(text="Seleccione su opción: ")  #Cambia el texto de indicación.

    #Configura los botones para que envíen la jugada del jugador.
    b_piedra.config(command=lambda: jugada_maquina("Piedra"))
    b_piedra.pack(padx=10, pady=10)
    b_papel.config(command=lambda: jugada_maquina("Papel"))
    b_papel.pack(padx=10, pady=10)
    b_tijeras.config(command=lambda: jugada_maquina("Tijeras"))
    b_tijeras.pack(padx=10, pady=10)
    
    #Reinicia los puntos en pantalla.
    puntos.config(text="Puntos jugador: 0    Puntos IA: 0")
    puntos.pack(pady=10)

    #Limpia mensajes anteriores.
    mens.config(text="")
    res.config(text="")

#Función que procesa la jugada contra la máquina.
def jugada_maquina(elecc_jugador):
    global pj, pm

    #La máquina elige una opción al azar.
    elecc_maquina = random.choice(elecc)
    
    #Verifica si hay empate.
    if elecc_jugador == elecc_maquina:
        res.config(text=f"Empate. Ambos eligieron {elecc_maquina}.")
    #Verifica si el jugador gana.
    elif (elecc_jugador == "Piedra" and elecc_maquina == "Tijeras") or \
         (elecc_jugador == "Papel" and elecc_maquina == "Piedra") or \
         (elecc_jugador == "Tijeras" and elecc_maquina == "Papel"):
        res.config(text=f"Sacaste {elecc_jugador}. La IA sacó {elecc_maquina}." +
                   "\nPunto para jugador.")
        pj += 1
    #Si no hay empate ni gana el jugador, la máquina gana.
    else:
        res.config(text=f"Sacaste {elecc_jugador}. La IA sacó {elecc_maquina}." +
                   "\nPunto para la IA.")
        pm += 1

    #Actualiza el marcador de puntos.
    puntos.config(text=f"Puntos jugador: {pj}    Puntos IA: {pm}")

    #Verifica si alguien ha ganado.
    if pj == 3:
        mens.config(text="¡Jugador ha ganado!")
        reset_puntos_IA()
    elif pm == 3:
        mens.config(text="La máquina ha ganado.")
        reset_puntos_IA()
    #Vacía el mansaje de victoria anterior al volver a empezar.
    elif pj < 3 or pm < 3:
        mens.config(text="")

#Reinicia los puntos al terminar una partida contra la máquina.
def reset_puntos_IA():
    global pj, pm
    pj = 0
    pm = 0
    puntos.config(text="Puntos jugador: 0    Puntos IA: 0")

#Función para iniciar el modo de juego para dos jugadores.
def vs_j2():
    global elecc_j1
    elecc_j1 = None  #Vacía la elección del jugador 1.

    #Modifica el texto para el turno del jugador 1.
    texto.config(text="Turno del jugador 1: ")

    #Configura los botones para el jugador 1.
    b_piedra.config(command=lambda: guarda_eleccion_j1("Piedra"))
    b_piedra.pack(padx=10, pady=10)
    b_papel.config(command=lambda: guarda_eleccion_j1("Papel"))
    b_papel.pack(padx=10, pady=10)
    b_tijeras.config(command=lambda: guarda_eleccion_j1("Tijeras"))
    b_tijeras.pack(padx=10, pady=10)

    #Reinicia los puntos de ambos jugadores.
    puntos.config(text="Puntos jugador 1: 0    Puntos jugador 2: 0")
    puntos.pack(pady=10)
    
    #Limpia mensajes anteriores.
    mens.config(text="")
    res.config(text="")

#Guarda la elección del jugador 1.
def guarda_eleccion_j1(elecc):
    global elecc_j1
    elecc_j1 = elecc  #Asigna la elección del jugador 1.

    #Ahora permite que el jugador 2 elija.
    texto.config(text="Turno del jugador 2: ")

    #Configura los botones para el jugador 2.
    b_piedra.config(command=lambda: jugada_jugadores("Piedra"))
    b_piedra.pack(padx=10, pady=10)
    b_papel.config(command=lambda: jugada_jugadores("Papel"))
    b_papel.pack(padx=10, pady=10)
    b_tijeras.config(command=lambda: jugada_jugadores("Tijeras"))
    b_tijeras.pack(padx=10, pady=10)

#Función que compara las elecciones de ambos jugadores y actualiza los puntos.
def jugada_jugadores(elecc_j2):
    global elecc_j1, pj, pj2

    #Verifica si hay empate.
    if elecc_j1 == elecc_j2:
        res.config(text=f"Empate. Ambos eligieron {elecc_j2}.")
    #Verifica si el jugador 1 gana.
    elif (elecc_j1 == "Piedra" and elecc_j2 == "Tijeras") or \
         (elecc_j1 == "Papel" and elecc_j2 == "Piedra") or \
         (elecc_j1 == "Tijeras" and elecc_j2 == "Papel"):
        res.config(text=f"Jugador 1 sacó {elecc_j1}. Jugador 2 sacó {elecc_j2}." + 
                   "\nPunto para jugador 1.")
        pj += 1
    #Si no hay empate ni gana el jugador 1, el jugador 2 gana.
    else:
        res.config(text=f"Jugador 1 sacó {elecc_j1}. Jugador 2 sacó {elecc_j2}." +
                   "\nPunto para jugador 2.")
        pj2 += 1

    #Actualiza el marcador de puntos.
    puntos.config(text=f"Puntos jugador 1: {pj}    Puntos jugador 2: {pj2}")

    #Verifica si algún jugador ha ganado.
    if pj == 3:
        mens.config(text="¡Jugador 1 ha ganado!")
        reset_puntos_jugadores()
    elif pj2 == 3:
        mens.config(text="¡Jugador 2 ha ganado!")
        reset_puntos_jugadores()
    #En caso de que aún no gane nadie.
    elif pj < 3 or pj2 < 3:
        #Vacía el mansaje de victoria.
        mens.config(text="")
        #Modifica el texto para el turno del jugador 1.
        texto.config(text="Turno del jugador 1: ")
        
        #Vacía la elección del jugador 1.
        elecc_j1 = None

        #Configura los botones para el jugador 1.
        b_piedra.config(command=lambda: guarda_eleccion_j1("Piedra"))
        b_piedra.pack(padx=10, pady=10)
        b_papel.config(command=lambda: guarda_eleccion_j1("Papel"))
        b_papel.pack(padx=10, pady=10)
        b_tijeras.config(command=lambda: guarda_eleccion_j1("Tijeras"))
        b_tijeras.pack(padx=10, pady=10)
        
        

#Reinicia los puntos de ambos jugadores después de una partida.
def reset_puntos_jugadores():
    global pj, pj2, elecc_j1
    pj = 0
    pj2 = 0
    elecc_j1 = None

    #Reinicia el marcador y los botones para comenzar otra partida.
    puntos.config(text="Puntos jugador: 0    Puntos jugador 2: 0")
    texto.config(text="Turno del jugador 1:")
    res.config(text="")
    
    b_piedra.config(command=lambda: guarda_eleccion_j1("Piedra"))
    b_papel.config(command=lambda: guarda_eleccion_j1("Papel"))
    b_tijeras.config(command=lambda: guarda_eleccion_j1("Tijeras"))

#Crea el submenú y sus opciones.
menu_partidas = tk.Menu(menu_prin, tearoff=0)
menu_prin.add_cascade(label="Partida", menu=menu_partidas)
menu_partidas.add_command(label="Un jugador", command=vs_maquina)
menu_partidas.add_command(label="Dos jugadores", command=vs_j2)
menu_partidas.add_separator()
menu_partidas.add_command(label="Salir", command=w.destroy)

#Ejecuta el bucle principal.
if __name__ == "__main__":
    w.mainloop()