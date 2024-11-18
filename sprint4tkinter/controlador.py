import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label
from modelo import GameModel
from vista import MainMenu, GameView
import threading
import time

class GameController:
    def __init__(self, root):
        self.root = root
        self.selected = []
        self.timer_started = False
        self.player_name = ""
        self.current_time = 0
        self.model = None
        self.menu = None
        self.game_view = None
        self.game_window = None 
        
        self.menu = MainMenu(root, self.show_difficulty_selection, self.show_stats, self.quit_application)

    def show_difficulty_selection(self):
        difficulty = simpledialog.askstring("Dificultad", "Selecciona la dificultad (facil, normal, dificil):")
        
        if difficulty in ['facil', 'normal', 'dificil']:
            self.player_name = self.menu.ask_player_name()
            
            if self.player_name:
                threading.Thread(target=self.start_game, args=(difficulty,), daemon=True).start()
            else:
                messagebox.showerror("Error", "Nombre del jugador no introducido.")
        else:
            messagebox.showerror("Error", "Debe seleccionar una dificultad.")

    def start_game(self, difficulty):
        if self.game_window is None:
            self.show_loading_window("Cargando tablero...")
            
            self.timer_started = False
            self.current_time = 0
            self.moves = 0
            self.pairs_found = 0

            if self.player_name and difficulty:
                self.model = GameModel(difficulty, self.player_name)
                self.model.size = 100
                self.model.start_timer()
                self.update_time()
                self.model.start_timer()
                self.check_images_loaded()
            else:
                messagebox.showerror("Error", "El nombre del jugador o la dificultad no son válidos.")
        else:
            print("El tablero ya está en uso.") 
            
    def time_label_exists(self):
        return hasattr(self.game_view, 'time_label') and self.game_view.time_label is not None and isinstance(self.game_view.time_label.master, Toplevel)
            
    def show_loading_window(self, message):
        self.loading_root = Toplevel(self.root)
        self.loading_root.title("Pantalla de carga")
        label = Label(self.loading_root, text=message)
        label.pack(expand=True)
        self.loading_root.grab_set()
        self.root.update_idletasks()
    
    def check_images_loaded(self):
        if self.model.images_are_loaded():
            #Cerrar la ventana de carga.
            self.loading_root.destroy()
            
            #Crear la vista del juego y pasar el modelo.
            self.game_view = GameView(self.root, self.on_card_click, self.update_move_count, self.update_time, self.model)
            
            if self.game_window is None:
                self.game_window = self.game_view.create_board()
        else:
            #Verificar cada 50ms si las imágenes han sido cargadas.
            self.root.after(500, self.check_images_loaded)
            
    def on_card_click(self, pos):
        if not self.timer_started:
            self.timer_started = True
            self.update_time()

        if pos not in self.selected:
            self.selected.append(pos)
            row, col = pos
            image = self.model.images[self.model.board[row][col]]
            self.game_view.update_board(pos, image)

        if len(self.selected) == 2:
            self.root.after(500, self.handle_card_selection)
            
    def handle_card_selection(self):
        if len(self.selected) == 2:
            pos1, pos2 = self.selected
            row1, col1 = pos1
            row2, col2 = pos2
            image1 = self.model.images[self.model.board[row1][col1]]
            image2 = self.model.images[self.model.board[row2][col2]]
            
            if self.model.check_match(pos1, pos2):
                self.game_view.update_board(pos1, image1)
                self.game_view.update_board(pos2, image2)
            else:
                self.root.after(100, lambda: self.game_view.reset_cards(pos1, pos2))
                
            self.selected.clear()
        self.update_move_count(self.model.moves)

        if self.model.is_game_complete():
            self.check_game_complete()

    def update_move_count(self, moves):
        self.game_view.update_move_count(moves)

    def check_game_complete(self):
        if self.model.is_game_complete():
            if not hasattr(self, 'game_complete_shown'):  #Evitar mostrar varias veces.
                self.game_complete_shown = True
                self.model.save_score(self.player_name, self.model.moves, self.current_time)
                messagebox.showinfo("Fin de la partida", "¡Has encontrado todas las parejas!")
                self.return_to_main_menu()
            
    def show_stats(self):
        if self.model is None:
            messagebox.showinfo("Estadísticas", "No hay estadísticas disponibles. Juega alguna partida primero.")
            return

        #Asegura de que las puntuaciones estén cargadas (aunque el juego no haya comenzado).
        self.model.load_scores()

        scores = self.model.scores  #Acceder a las puntuaciones guardadas en el modelo.
        stats_message = "Ranking por dificultad:\n"
    
        for difficulty, score_list in scores.items():
            stats_message += f"\n{difficulty.capitalize()}:\n"
            for idx, entry in enumerate(score_list):
                stats_message += f"{idx + 1}. {entry['name']} - Movimientos: {entry['moves']}, Tiempo: {entry['time_taken']}s, Fecha: {entry['date']}\n"

        messagebox.showinfo("Estadísticas", stats_message)

    def update_time(self):
        if self.timer_started and self.time_label_exists():
            self.current_time += 1
            self.game_view.update_time(self.current_time)
            self.root.after(1000, self.update_time)

    def time_label_exists(self):
        return self.game_view.time_label and isinstance(self.game_view.time_label.master, tk.Toplevel)
    
    def quit_application(self):
        self.root.quit() 

    def return_to_main_menu(self):
        if self.game_view:
            self.game_view.destroy()
        self.menu.window.deiconify()