import threading, time, random
from datetime import datetime
from recursos import descargar_imagen
import os

class GameModel:
    def __init__(self, difficulty, player_name, cell_size=100):
        #Inicializa el modelo del juego con dificultad, nombre del jugador y tamaño de las celdas del tablero.
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = 100
        
        #Configura el tamaño del tablero dependiendo de la dificultad.
        self.board_size = {
            'facil': 4,
            'normal': 6,
            'dificil': 8,
        }.get(difficulty, 6)  #El valor predeterminado es 'normal'.
            
        self.start_time = None  #Almacena el tiempo de inicio del juego.
        self.timer_running = False  #Estado del temporizador.
        self.moves = 0  #Número de movimientos realizados.
        self.pairs_found = 0  #Número de pares encontrados.
        self.images_loaded_event = threading.Event()  #Evento para verificar si las imágenes se han cargado.
        self.matched_positions = []  #Lista de posiciones de cartas emparejadas.
        
        #Cargar puntuaciones desde archivo.
        self.scores = self.load_scores()
        self._generate_board()  #Genera el tablero de juego.
        threading.Thread(target=self._load_images).start()  #Cargar las imágenes en un hilo para no bloquear la UI.
        
    def _generate_board(self):
        #Genera un tablero con pares de identificadores de imágenes mezclados.
        total_pairs = (self.board_size ** 2) // 2  #La cantidad total de pares (mitad del total de celdas).
        identifiers = list(range(total_pairs)) * 2  #Genera los identificadores (duplicados).
        random.shuffle(identifiers)  #Mezcla los identificadores.
        #Crea el tablero de juego a partir de los identificadores.
        self.board = [identifiers[i:i + self.board_size] for i in range(0, len(identifiers), self.board_size)]
        
    def _load_images(self):
        #URL base donde se encuentran las imágenes en el repositorio de GitHub.
        base_url = 'https://raw.githubusercontent.com/Zipyrar/Imagenes-juego-de-memoria/master/'

        #Lista de nombres de las imágenes que se usarán en el juego.
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

        #Cargar la imagen oculta que se usará en las cartas no descubiertas.
        self.hidden_image = descargar_imagen(f"{base_url}tkinter_logo.png", size=(self.cell_size, self.cell_size))

        #Lista temporal para almacenar las imágenes cargadas.
        loaded_images = []
        cnt = 0
        
        for image_name in images_names:
            #Construir la URL completa para cada imagen.
            url = f"{base_url}{image_name}"
            image = descargar_imagen(url, size=(self.cell_size, self.cell_size))  #Cargar la imagen.
            #Asegurarse de no cargar más imágenes de las necesarias para el tablero.
            if image and cnt < (self.board_size**2) // 2:  
                loaded_images.append(image)
                cnt += 1

        #Seleccionar un número adecuado de imágenes únicas para los pares.
        total_pairs = (self.board_size ** 2) // 2
        unique_images = list(set(loaded_images))  #Eliminar duplicados de la lista de imágenes cargadas.
        if len(unique_images) >= total_pairs:
            selected_images = unique_images[:total_pairs]  #Seleccionar solo las imágenes necesarias.
            self.images = selected_images  #Duplicar las imágenes para los pares.
            random.shuffle(self.images)  #Mezclar las imágenes.
        else:
            print("Error: No hay suficientes imágenes únicas cargadas.")  #Mensaje de error si no hay suficientes imágenes.

        #Señaliza que las imágenes han sido cargadas.
        self.images_loaded_event.set()
            
    def images_are_loaded(self):
        #Verifica si las imágenes han sido cargadas completamente.
        return self.images_loaded_event.is_set()  #Retorna True si las imágenes están listas.
    
    def start_timer(self):
        #Inicia el temporizador si no está en ejecución.
        if not self.timer_running:
            self.timer_running = True
            self.start_time = time.time()  #Captura el tiempo de inicio.
        
    def get_time(self):
        #Devuelve el tiempo transcurrido desde que comenzó el temporizador.
        if self.start_time is None:
            return 0
        return int(time.time() - self.start_time)
    
    def check_match(self, pos1, pos2):
        #Verifica si dos cartas coinciden.
        self.moves += 1  #Incrementa el número de movimientos.
        
        first_card = self.board[pos1[0]][pos1[1]]  #Obtiene la carta en la primera posición.
        second_card = self.board[pos2[0]][pos2[1]]  #Obtiene la carta en la segunda posición.
        
        if first_card == second_card:  #Si las cartas coinciden.
            self.pairs_found += 1  #Incrementa el número de pares encontrados.
            #Guarda las posiciones de las cartas emparejadas.
            self.matched_positions.extend([pos1, pos2])
            return True  #Retorna True si las cartas coinciden.
        return False  #Retorna False si no coinciden.
    
    def is_card_matched(self, pos):
        #Verifica si una carta en una posición dada ya ha sido emparejada.
        return pos in self.matched_positions
    
    def is_game_complete(self):
        #Verifica si el juego ha terminado (cuando se encuentran todos los pares).
        total_pairs = (self.board_size ** 2) // 2
        return total_pairs == self.pairs_found
    
    def save_score(self, player_name, moves, time_taken):
        """Guardar la puntuación en el archivo ranking.txt y en memoria"""
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        score_line = f"{player_name},{self.difficulty},{moves},{time_taken},{fecha}\n"

        #Guardar la puntuación en el archivo.
        with open("ranking.txt", "a") as file:
            file.write(score_line)

        #Guardar la puntuación en memoria.
        self.scores[self.difficulty].append({
            "name": player_name,
            "difficulty": self.difficulty,
            "moves": moves,
            "time_taken": time_taken,
            "date": fecha
        })

        #Ordenar y mantener solo las 3 mejores puntuaciones.
        self.sort_scores()

    def sort_scores(self):
        """Ordenar las puntuaciones por dificultad y mantener las 3 mejores"""
        #Ordenamos las puntuaciones primero por dificultad, luego por el número de movimientos, y finalmente por el tiempo.
        for difficulty in self.scores:
            self.scores[difficulty] = sorted(self.scores[difficulty], key=lambda x: (x['moves'], x['time_taken']))[:3]
        
        #Depuración: Imprimir las puntuaciones ordenadas.
        print("Puntuaciones ordenadas:", self.scores)

    def load_scores(self):
        """Cargar las puntuaciones desde el archivo ranking.txt"""
        scores = {"facil": [], "normal": [], "dificil": []}  #Inicializar las puntuaciones por dificultad.

        if not os.path.exists("ranking.txt"):  #Si el archivo no existe, retornamos puntuaciones vacías.
            return scores  

        #Leer el archivo y cargar las puntuaciones.
        with open("ranking.txt", "r") as file:
            for line in file:
                name, difficulty, moves, time_taken, date = line.strip().split(",")  #Separar los valores de cada línea.
                #Añadir la puntuación al diccionario correspondiente.
                scores[difficulty].append({
                    "name": name,
                    "difficulty": difficulty,
                    "moves": int(moves),
                    "time_taken": int(time_taken),
                    "date": date
                })

        #Ordenar las puntuaciones tras cargar los datos.
        for difficulty in scores:
            scores[difficulty] = sorted(scores[difficulty], key=lambda x: (x['moves'], x['time_taken']))[:3]

        return scores