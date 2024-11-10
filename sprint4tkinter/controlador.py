import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label
from modelo import GameModel
from vista import MainMenu, GameView
import time

class GameController:
    def __init__(self, root):
        self.root = root
        self.model = None
        self.selected = []
        self.timer_started = False
        self.player_name = ""
        
        self.menu = MainMenu(root, self.show_difficulty_selection, self.show_stats, self.return_to_main_menu)

    def show_difficulty_selection(self):
        #Solicitar la dificultad al jugador.
        difficulty = simpledialog.askstring("Dificultad", "Selecciona la dificultad (fácil, normal, difícil):")
        
        if difficulty in ['fácil', 'normal', 'difícil']:
            #Guardar el nombre del jugador después de seleccionar la dificultad.
            self.player_name = self.menu.ask_player_name()
            
            if self.player_name:
                #Llamar a start_game con la dificultad seleccionada.
                self.start_game(difficulty)
            else:
                messagebox.showerror("Error", "Nombre del jugador no introducido.")
        else:
            messagebox.showerror("Error", "Debe seleccionar una dificultad.")

    def start_game(self, difficulty):
        #Este es el método que maneja la lógica de inicio del juego.
        self.show_loading_window("Cargando tablero...")

        if self.player_name and difficulty:
            # Crear la instancia de GameModel con la dificultad y nombre del jugador
            self.model = GameModel(difficulty, self.player_name)

            # Cargar las imágenes
            self.model._load_images()

            # Verificar si las imágenes se cargaron correctamente
            self.check_images_loaded()
        else:
            messagebox.showerror("Error", "El nombre del jugador o la dificultad no son válidos.")
            
        
    def show_loading_window(self, message):
        self.loading_root = Toplevel(self.root)
        self.loading_root.title("Pantalla de carga")
        label = tk.Label(self.loading_root, text=message)
        label.pack()
        self.loading_root.grab_set()
    
    def check_images_loaded(self):
        if self.model.images_are_loaded():
            self.loading_root.destroy()
            self.game_view = GameView(self.on_card_click, self.update_move_count, self.update_time)
            self.game_view.create_board(self.model)
        else:
            self.root.after(100, self.check_images_loaded)
            
    def on_card_click(self, pos):
        if not self.timer_started:
            self.timer_started = True
            self.update_time()
        self.selected.append(pos)

        #Añadir posición a la lista seleccionada y actualizar la vista.
        if pos not in self.selected:
            self.selected.append(pos)
            self.game_view.update_board(pos, self.model.get_image(pos))

        if len(self.selected) == 2:
            #Añade un pequeño retraso para mostrar la segunda carta.
            self.root.after(1000, self.handle_card_selection)  
            
    def handle_card_selection(self):
        pos1, pos2 = self.selected
        
        if self.model.check_match(pos1, pos2):
            self.game_view.update_board(pos1, self.model.get_image(pos1))
            self.game_view.update_board(pos2, self.model.get_image(pos2))
        else:
            #Pausa de 1 segundo antes de ocultar las cartas.
            time.sleep(1)
            self.game_view.reset_cards(pos1, pos2)
            
        self.selected.clear()
        self.update_move_count(len(self.selected))

        if self.model.is_game_complete():
            self.check_game_complete()

    def update_move_count(self, moves):
        self.game_view.update_move_count(moves)

    def check_game_complete(self):
        if self.model.is_game_complete():
            messagebox.showinfo("Fin de la partida", "¡Has encontrado todas las parejas!")
            self.return_to_main_menu()

    def show_stats(self):
        if self.model:
            stats = self.model.load_scores()  # Ahora cargamos los puntajes
            stats_root = tk.Toplevel(self.root)
            stats_root.title("Estadísticas")
            for level, entries in stats.items():
                tk.Label(stats_root, text=f"{level}").pack()
                for entry in entries:
                    tk.Label(stats_root, text=f"{entry['Nombre']} - Movimientos: {entry['Movimientos']}").pack()
        else:
            messagebox.showerror("Error", "No se puede cargar las estadísticas sin un modelo válido.")

    def update_time(self):
        if self.timer_started:
            self.current_time += 1
            self.game_view.update_time(self.current_time)
            self.root.after(1000, self.update_time)
            
    def return_to_main_menu(self):
        self.root.quit()