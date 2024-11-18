import threading, time, random
from datetime import datetime
from recursos import descargar_imagen
import os

class GameModel:
    def __init__(self, difficulty, player_name, cell_size=100):
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = 100
        
        self.board_size = {
            'facil': 4,
            'normal': 6,
            'dificil': 8,
        }.get(difficulty, 6)
            
        self.start_time = None
        self.timer_running = False
        self.moves = 0
        self.pairs_found = 0
        self.images_loaded_event = threading.Event()  # Evento para saber cuando las imágenes están cargadas
        self.matched_positions = []  #Lista para almacenar posiciones de cartas encontradas.
        
        self.scores = self.load_scores()
        self._generate_board()
        threading.Thread(target=self._load_images).start()  # Usar un hilo para cargar imágenes de forma asíncrona.
        
    def _generate_board(self):
        # Genera un tablero con pares de identificadores de imágenes mezclados.
        total_pairs = (self.board_size ** 2) // 2
        identifiers = list(range(total_pairs)) * 2
        random.shuffle(identifiers)
        self.board = [identifiers[i:i + self.board_size] for i in range(0, len(identifiers), self.board_size)]
        
    def _load_images(self):
        # URL base que apunta a la rama master de GitHub
        base_url = 'https://raw.githubusercontent.com/Zipyrar/Imagenes-juego-de-memoria/master/'

        # Nombres de las imágenes en el repositorio
        images_names = [
            'Ciclomotor.png', 'Coche.png', 'mesa.png', 'Moto.png',
            'nevera.png', 'silla.jpg', 'silla_ruedas.jpg', 'taburete.png',
            'afilalapices.png', 'aguila.png', 'avestruz.png', 'avion.png',
            'boli.jpg', 'cabra.png', 'camion.png', 'furgoneta.png', 
            'gato.png', 'gaviota.png', 'lapiz.png', 'leon.png', 'leona.png',
            'lince.png', 'lobo.png', 'mapache.png', 'mesa.png', 'mofeta.png',
            'montaña.png', 'oveja.png', 'perro.png', 'rueda.png', 'tigre.png',
            'tren.jpg', 'vaca.png'
        ]

        # Cargar la imagen oculta
        self.hidden_image = descargar_imagen(f"{base_url}tkinter_logo.png", size=(self.cell_size, self.cell_size))

        # Lista temporal para almacenar las imágenes cargadas (sin duplicar)
        loaded_images = []
        cnt = 0
        
        for image_name in images_names:
            url = f"{base_url}{image_name}"
            image = descargar_imagen(url, size=(self.cell_size, self.cell_size))
            if image and cnt < (self.board_size**2) // 2:  # Solo cargar las imágenes necesarias para el tablero
                loaded_images.append(image)
                cnt += 1

        # Selecciona solo el número necesario de pares de imágenes
        total_pairs = (self.board_size ** 2) // 2
        unique_images = list(set(loaded_images))
        if len(unique_images) >= total_pairs:
            selected_images = unique_images[:total_pairs]
            self.images = selected_images # Duplicar para pares
            random.shuffle(self.images)
        else:
            print("Error: No hay suficientes imágenes únicas cargadas.")

        # Señaliza que las imágenes están cargadas.
        self.images_loaded_event.set()
            
    def images_are_loaded(self):
        # Verifica si todas las imágenes han sido cargadas
        return self.images_loaded_event.is_set()  # Verifica si el evento ha sido señalizado.
    
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            # Inicia el temporizador
            self.start_time = time.time()
        
    def get_time(self):
        # Devuelve el tiempo transcurrido desde que se inició el temporizador.
        if self.start_time is None:
            return 0
        return int(time.time() - self.start_time)
    
    def check_match(self, pos1, pos2):
        self.moves += 1
    
        first_card = self.board[pos1[0]][pos1[1]]
        second_card = self.board[pos2[0]][pos2[1]]
        
        if first_card == second_card:
            self.pairs_found += 1
            # Guarda las posiciones de las cartas emparejadas.
            self.matched_positions.extend([pos1, pos2])
            return True
        return False
    
    def is_card_matched(self, pos):
        return pos in self.matched_positions
    
    def is_game_complete(self):
        # Verifica si se han encontrado todas las parejas en el tablero
        total_pairs = (self.board_size ** 2) // 2
        return total_pairs == self.pairs_found
    
    def save_score(self, player_name, moves, time_taken):
        """Guardar la puntuación en el archivo ranking.txt y en memoria"""
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        score_line = f"{player_name},{self.difficulty},{moves},{time_taken},{fecha}\n"

        # Guardar la puntuación en el archivo
        with open("ranking.txt", "a") as file:
            file.write(score_line)

        # Guardar la puntuación en memoria
        self.scores[self.difficulty].append({
            "name": player_name,
            "difficulty": self.difficulty,
            "moves": moves,
            "time_taken": time_taken,
            "date": fecha
        })

        # Ordenar y mantener solo las 3 mejores puntuaciones
        self.sort_scores()

    def sort_scores(self):
        """Ordenar las puntuaciones por dificultad y mantener las 3 mejores"""
        # Ordenamos por dificultad, luego por el número de movimientos (menos es mejor), y finalmente por el tiempo (menos es mejor)
        for difficulty in self.scores:
            # Ordenamos por número de movimientos (menos es mejor) y luego por tiempo (menos es mejor)
            self.scores[difficulty] = sorted(self.scores[difficulty], key=lambda x: (x['moves'], x['time_taken']))[:3]
        
        # Depuración: Imprimir las puntuaciones ordenadas
        print("Puntuaciones ordenadas:", self.scores)

    def load_scores(self):
        """Cargar las puntuaciones desde el archivo ranking.txt"""
        # Si el archivo no existe, retornamos las puntuaciones vacías
        scores = {"facil": [], "normal": [], "dificil": []}

        if not os.path.exists("ranking.txt"):
            return scores  # Si el archivo no existe, retornamos las puntuaciones vacías

        # Leer el archivo y cargar las puntuaciones
        with open("ranking.txt", "r") as file:
            for line in file:
                name, difficulty, moves, time_taken, date = line.strip().split(",")
                # Añadir la puntuación al diccionario correspondiente
                scores[difficulty].append({
                    "name": name,
                    "difficulty": difficulty,
                    "moves": int(moves),
                    "time_taken": int(time_taken),
                    "date": date
                })

        # Ordenar las puntuaciones tras cargar los datos
        for difficulty in scores:
            scores[difficulty] = sorted(scores[difficulty], key=lambda x: (x['moves'], x['time_taken']))[:3]

        return scores