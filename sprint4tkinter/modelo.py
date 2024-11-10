import threading, time, random, datetime
from recursos import descargar_imagen

class GameModel:
    def __init__(self, difficulty, player_name, cell_size=100):
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = cell_size
        
        self.board_size = {
            'Fácil': 4,
            'Normal': 6,
            'Difícil': 8,
        }.get(difficulty, 6)
            
        self.start_time = None
        self.moves = 0
        self.pairs_found = 0
        
        self._generate_board()
        threading.Thread(target=self._load_images).start()  #Usa un hilo para cargar imágenes de forma asíncrona.
        
    def _generate_board(self):
        #Genera un tablero con pares de identificadores de imágenes mezclados.
        total_pairs = (self.board_size ** 2) // 2
        identifiers = list(range(total_pairs)) * 2
        random.shuffle(identifiers)
        self.board = [identifiers[i:i + self.board_size] for i in range(0, len(identifiers), self.board_size)]
        
    def _load_images(self):
        # URL base que apunta a la rama `master`
        base_url = 'https://raw.githubusercontent.com/Zipyrar/Imagenes-juego-de-memoria/master/'
    
        # Nombres de las imágenes en el repositorio
        images_names = [
            'Ciclomotor.png', 'Coche.png', 'mesa.png', 'Moto.png',
            'nevera.png', 'silla.png', 'Silla_con_ruedas.png', 'taburete.png'
        ]
    
        # URL para la imagen oculta
        self.hidden_image = descargar_imagen(f"{base_url}tkinter_logo.png", size=(self.cell_size, self.cell_size))
        
        self.images = []
        for image_name in images_names:
            #URL completa de cada imagen.
            url = f"{base_url}{image_name}"
            image = descargar_imagen(url, size=(self.cell_size, self.cell_size))
            if image:
                #Añade dos copias de cada imagen para las parejas.
                self.images.extend([image, image]) 
            
            random.shuffle(self.images)  #Mezcla las imágenes.
            
    def images_are_loaded(self):
        #Verifica si todas las imágenes han sido cargadas.
        return len(self.images) >= (self.board_size ** 2)
    
    def start_timer(self):
        #Inicia el temporizador.
        self.start_time = time.time()
        
    def get_time(self):
        #Devuelve el tiempo transcurrido desde que se inició el temporizador.
        if self.start_time is None:
            return 0
        
        return int(time.time() - self.start_time)
    
    def check_match(self, pos1, pos2):
        #Verifica si las cartas en las dos posiciones dadas coinciden.
        self.moves += 1
        
        first_card = self.board[pos1[0]] [pos1[1]]
        second_card = self.board[pos2[0]] [pos2[1]]
        
        if first_card == second_card:
            self.pairs_found +=1
            return True
        return False
    
    def is_game_complete(self):
        #Verifica si se han encontrado todas las parejas en el tablero.
        total_pairs = (self.board_size ** 2) // 2
        return total_pairs == self.pairs_found
    
    def save_score(self):
        #Guarda la puntuación del jugador en un archivo de ranking.
        score_data = {
            'Nombre': self.player_name,
            'Dificultad': self.difficulty,
            'Movimientos': self.moves,
            'Fecha': datetime.datetime.now().strftime('%d/%m/%Y  %H:%M:%S')
        }
        
        try:
            scores = self.load_scores()
            scores[self.difficulty].append(score_data)
            #Ordena las puntuaciones y guarda solo las 3 mejores.
            scores[self.difficulty] = sorted(scores[self.difficulty], key=lambda x: x['Movimientos'])[:3]

            with open('sprint4tkinter\\ranking.txt', 'w') as file:
                for level, entries in scores.items():
                    for entry in entries:
                        file.write(f"{entry['Nombre']},{level},{entry['Movimientos']},{entry['Fecha']}\n")
        except Exception as e:
            print(f"Error al guardar la puntuación: {e}")

    def load_scores(self):
        #Carga las puntuaciones desde el archivo de ranking.
        scores = {'Fácil': [], 'Normal': [], 'Difícil': []}
        try:
            with open('sprint4tkinter\\ranking.txt', 'r') as file:
                for line in file:
                    name, level, moves, date = line.strip().split(',')
                    scores[level].append({
                        'Nombre': name,
                        'Dificultad': level,
                        'Movimientos': int(moves),
                        'Fecha': date
                    })
        except FileNotFoundError:
            pass 
        return scores