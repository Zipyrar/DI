import tkinter as tk
from tkinter import simpledialog
from tkinter import Toplevel
from tkinter import PhotoImage
import gc


class GameView:
    def __init__(self, root, on_card_click_callback, update_move_count_callback, update_time_callback, model):
        self.root = root
        self.window = Toplevel() 
        self.labels = {}
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback
        self.model = model

        self.window.title("Juego de Memoria")
        
        self.moves_label = tk.Label(self.window, text="Movimientos: 0")  #Añadir el label para los movimientos.
        self.moves_label.grid(row=10, column=0, columnspan=2, padx=10, pady=10)
        
        #Etiqueta de tiempo (solo una vez).
        self.time_label = tk.Label(self.window, text="Tiempo: 0")
        self.time_label.grid(row=10, column=2, columnspan=2, padx=10, pady=10) #Ajustar la posición según sea necesario.
        
        #Crear el tablero.
        self.create_board()

    def create_board(self):
        for row in range(self.model.board_size):
            for col in range(self.model.board_size):
                label = tk.Label(self.window, image=self.model.hidden_image, width=self.model.size, height=self.model.size, borderwidth=2, relief="raised")
                label.grid(row=row, column=col) #Ajusta la posición.
                label.bind("<Button-1>", lambda e, r=row, c=col: self.on_card_click_callback((r, c)))
                self.labels[(row, col)] = label

    def get_unique_image(path):
        """Devuelve una nueva instancia de PhotoImage para evitar referencias compartidas."""
        return PhotoImage(file=path)

    def update_cell_image(self, row, col, new_image_path):
        #Obtener una nueva imagen única.
        new_image = self.get_unique_image(new_image_path)
        
        #Obtener la imagen actual en la celda.
        current_image = self.board[row][col].image
        
        #Comprobar si la imagen actual es diferente de la nueva.
        if current_image != new_image:
            print(f"Eliminando imagen previa de la celda ({row}, {col})")
            
            #Limpiar la imagen previa.
            self.board[row][col].image = None
            self.board[row][col].config(image=None)

            #Recolectar basura para eliminar referencias.
            gc.collect()  #Forzar recolección de basura.

            #Esperar para asegurar que la imagen previa sea eliminada antes de continuar.
            self.root.after(10, self.assign_new_image, row, col, new_image)  #10ms de retraso.

    def assign_new_image(self, row, col, new_image):
        #Asignar la nueva imagen única.
        print(f"Asignando nueva imagen a la celda ({row}, {col})")
        self.board[row][col].image = new_image
        self.board[row][col].config(image=new_image)
            
    def check_all_cells(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                current_image = self.board[row][col].image
                print(f"Celda ({row}, {col}) tiene imagen: {current_image}")
    
    def update_board(self, pos, image_id):
        row, col = pos
        cell = self.labels.get((row, col))  #Obtenemos el Label correspondiente.

        if cell:  #Verificamos si la celda existe.
            if hasattr(cell, 'image') and cell.image:
                print(f"Eliminando imagen previa de la celda {pos}")  #Mensaje de depuración.
                cell.config(image=None)  #Limpiar la imagen anterior.
                cell.image = None  #Limpiar la referencia de la imagen.
            
            print(f"Asignando nueva imagen a la celda {pos}")  #Mensaje de depuración.
            cell.config(image=image_id)  #Actualizar la celda con la nueva imagen.
            cell.image = image_id 
        
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
        #Pedir el nombre del jugador con simpledialog.
        player_name = simpledialog.askstring("Nombre del Jugador", "Ingresa tu nombre:")

        if not player_name:
            player_name = "Jugador"  #Valor predeterminado si no se ingresa un nombre.

        return player_name
    
    def show_stats(self, stats):
        stats_root = Toplevel()
        stats_root.title("Estadísticas")
        for level, entries in stats.items():
            tk.Label(stats_root, text=f"{level}").pack()
            for entry in entries:
                tk.Label(stats_root, text=f"{entry['Nombre']} - Movimientos: {entry['Movimientos']}").pack()
