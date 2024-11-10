import tkinter as tk
from tkinter import simpledialog
from tkinter import  Toplevel

class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback):
        self.window = None
        self.labels = {}
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback
        
    def create_board(self, model):
        self.window = Toplevel()
        self.window.title("Juego de memoria")
        
        for row in range(model.board_size):
            for col in range(model.board_size):
                label = tk.Label(self.window, text="?", width=10, height=5, borderwidth=2, relief="raised")
                label.grid(row=row, column=col)
                label.bind("<Button-1>", lambda e, r=row, c=col: self.on_card_click_callback((r, c)))
                self.labels[(row, col)] = label
                
        self.move_label = tk.Label(self.window, text="Movimientos: 0")
        self.move_label.grid(row=model.board_size, column=0, columnspan=model.board_size // 2)

        self.time_label = tk.Label(self.window, text="Tiempo: 0")
        self.time_label.grid(row=model.board_size, column=model.board_size // 2, columnspan=model.board_size // 2)
        
    def update_board(self, pos, image_id):
        if pos in self.labels:
            self.labels[pos].config(image=image_id)
        
    def reset_cards(self, pos1, pos2):
        if pos1 in self.labels:
            self.labels[pos1].config(image="", text="?")
        if pos2 in self.labels:
            self.labels[pos2].config(image="", text="?")
        
    def update_move_count(self, moves):
        self.move_label.config(f"Movimientos: {moves}")
        
    def update_time(self, time):
        self.time_label.config(f"Tiempo: {time}")
        
    def destroy(self):
        if self.window:
            self.window.destroy()
        self.labels.clear()

class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        self.window = root
        self.window.title("Juego de memoria")
        
        self.start_game_callback = start_game_callback 
        self.show_stats_callback = show_stats_callback
        self.quit_callback = quit_callback
        
        self.play = tk.Button(root, text="Jugar partida", command=self.start_game_callback)
        self.play.pack(pady=20)
        self.stats = tk.Button(root, text="Estadísticas", command=self.show_stats_callback)
        self.stats.pack(pady=20)
        self.quit = tk.Button(root, text="Salir", command=self.quit_callback)
        self.quit.pack(pady=20)
        
    def ask_player_name(self):
        #Pedir el nombre del jugador con simpledialog.
        player_name = simpledialog.askstring("Nombre del Jugador", "Ingresa tu nombre:")
        
        if not player_name:
            player_name = "Jugador"  #Valor predeterminado si no se ingresa un nombre.

        #Llamar al callback (GameController) con los parámetros obtenidos.
        self.start_game_callback(player_name)
    
    def show_stats(self, stats):
        stats_root = Toplevel()
        stats_root.title("Estadísticas")
        for level, entries in stats.items():
            tk.Label(stats_root, text=f"{level}").pack()
            for entry in entries:
                tk.Label(stats_root, text=f"{entry['Nombre']} - Movimientos: {entry['Movimientos']}").pack()