from monstruo import Monstruo
from tesoro import Tesoro

class Mazmorra:
    def __init__(self, heroe):
        self.heroe = heroe
        #Definimos una lista de monstruos con sus características.
        self.monstruos = [Monstruo("Duende", 10, 5, 30), Monstruo("Slime", 15, 20, 40), Monstruo("Orco", 30, 50, 80), Monstruo("Dragón", 90, 55, 150)]
        self.tesoro = Tesoro()
        
    def jugar(self):
        print(f"{self.heroe.nomb} ha entrado en la mazmorra.")
        
        #Comprueba que el héroe sigue vivo, y que siga habiendo monstruos.
        while(self.heroe.vive() and len(self.monstruos) > 0):
            #Hace que aparezca (en orden) los monstruos, uno por uno.
            enemigo = self.monstruos.pop(0)
            print(f"Te has encontrado con un {enemigo.nomb}.")
            self.enfrentar_enemigo(enemigo)
            
            if not self.heroe.vive():
                print(f"{self.heroe.nomb} ha muerto.")
                
            if not enemigo.vive():
                print(f"{self.heroe.nomb} ha derrotado al {enemigo.nomb}")
                self.buscar_tesoro()
        
        #Aparece el mensaje cuando completas la mazmorra.
        if self.heroe.vive():
            print(f"¡{self.heroe.nomb} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")
            
    def enfrentar_enemigo(self, enemigo):  
        while self.heroe.vive() and enemigo.vive():
            #Permite darle al jugador la información salud actual del héroe.
            x = f'''------------------------------------
                {self.heroe.nomb}
                {self.heroe.salud}/{self.heroe.salud_maxima}\n------------------------------------'''
            #Centra la info en la pantalla.
            info = x.center(10)
            print(info)
            
            print("¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Defender")
            print("3. Curarse")
            
            opc = input("Elige una opción: ")
            
            if opc == "1":
                self.heroe.atacar(enemigo)
            elif opc == "2":
                self.heroe.defenderse()
            elif opc == "3":
                self.heroe.curarse()
            else:
                print("Opción no válida.")
                continue
            
            if enemigo.vive():
                enemigo.atacar(self.heroe)
                self.heroe.reset_defensa()
      
    #Da al azar un beneficio cada vez que se derrote a un monstruo.          
    def buscar_tesoro(self):
        print("Buscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe)