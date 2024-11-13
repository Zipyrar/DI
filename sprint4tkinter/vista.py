import tkinter as tk
from tkinter import simpledialog
from tkinter import Toplevel

class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback, model):
        self.window = Toplevel()  # Usamos Toplevel o root según el contexto
        self.labels = {}
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback
        self.model = model

        self.window.title("Juego de Memoria")
        
        # Etiqueta de tiempo (solo una vez)
        self.time_label = tk.Label(self.window, text="0", font=("Helvetica", 24))
        self.time_label.grid(row=0, column=0, columnspan=2)  # Ajustar la posición según sea necesario
        
        # Crear el tablero
        self.create_board()

    def create_board(self):
        # Aquí usamos la misma ventana que se creó en __init__
        for row in range(self.model.board_size):
            for col in range(self.model.board_size):
                label = tk.Label(self.window, image=self.model.hidden_image, width=self.model.size, height=self.model.size, borderwidth=2, relief="raised")
                label.grid(row=row+1, column=col)  # Ajustamos la posición para que no se superponga con el time_label
                label.bind("<Button-1>", lambda e, r=row, c=col: self.on_card_click_callback((r, c)))
                self.labels[(row, col)] = label

        # Mostrar los movimientos
        self.moves_label = tk.Label(self.window, text="Movimientos: 0")
        self.moves_label.grid(row=self.model.board_size + 1, column=0, columnspan=self.model.board_size // 2)

    def update_board(self, pos, image_id):
        if pos in self.labels:
            self.labels[pos].config(image=image_id)
        
    def reset_cards(self, pos1, pos2):
        if pos1 in self.labels:
            self.labels[pos1].config(image=self.model.hidden_image)  #Usar una imagen predefinida para mantener el tamaño
        if pos2 in self.labels:
            self.labels[pos2].config(image=self.model.hidden_image)
            
    def update_move_count(self, moves):
        self.moves_label.config(text=f"Movimientos: {moves}")
        
    def update_time(self, time):
        if self.time_label.winfo_exists():  #Verificar si el widget sigue existiendo.
            self.time_label.config(text=f"Tiempo: {time}")
        
    def destroy(self):
        """Destruye la ventana y limpia los recursos."""
        if self.window:
            self.window.destroy()
        self.labels.clear()

class MainMenu:
    def __init__(self, root, show_difficulty_selection_callback, show_stats_callback, quit_callback):
        self.window = root
        self.window.title("Juego de memoria")

        self.show_difficulty_selection_callback = show_difficulty_selection_callback
        self.show_stats_callback = show_stats_callback
        self.quit_callback = quit_callback

        self.play = tk.Button(root, text="Jugar partida", command=self.show_difficulty_selection_callback)
        self.play.pack(pady=20)
        self.stats = tk.Button(root, text="Estadísticas", command=self.show_stats_callback)
        self.stats.pack(pady=20)
        self.quit = tk.Button(root, text="Salir", command=self.quit_callback)
        self.quit.pack(pady=20)

    def ask_player_name(self):
        # Pedir el nombre del jugador con simpledialog
        player_name = simpledialog.askstring("Nombre del Jugador", "Ingresa tu nombre:")

        if not player_name:
            player_name = "Jugador"  # Valor predeterminado si no se ingresa un nombre.

        return player_name
    
    def show_stats(self, stats):
        stats_root = Toplevel()
        stats_root.title("Estadísticas")
        for level, entries in stats.items():
            tk.Label(stats_root, text=f"{level}").pack()
            for entry in entries:
                tk.Label(stats_root, text=f"{entry['Nombre']} - Movimientos: {entry['Movimientos']}").pack()
