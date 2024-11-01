class NotasModel:
    def __init__(self, notas):
        self.notas = notas
        self.coordenadas = (0, 0)
        
    def agregar_nota(self, nueva_nota):
        self.notas.append(nueva_nota)
        
    def eliminar_nota(self, indice):
        del self.notas[indice]
        
    def obtener_notas(self):
        return self.notas
    
    #Sobreescribe el archivo de texto por uno con las nuevas notas.
    def guardar_notas(self):
        with open("Sprint2tkinter\\notas.txt", "w", encoding="UTF-8", newline='') as arch:
            for nota in self.notas:
                arch.write(nota + "\n")
                
    def cargar_notas(self):
        with open("Sprint2tkinter\\notas.txt", "r", encoding="UTF-8") as arch:
            self.notas = [linea.strip() for linea in arch]
            
    #Obtiene las coordenadas del ratón cuando se hace clic.
    def actualizar_coordenadas(self, x, y):
        self.coordenadas = (x, y)