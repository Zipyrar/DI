import random

class Heroe:
    def __init__(self, nomb):
        self.nomb = nomb
        self.ataque = 70
        self.defensa = 45
        self.salud = 100
        self.salud_maxima = 100
        #Controlamos con esto las funciones de subida de defensa de forma más precisa.
        self.def_temporal = self.defensa
    
    def atacar(self, enemigo):
        print(f"{self.nomb} ataca a {enemigo.nomb}")
        
        daño = self.ataque - enemigo.defensa
    
        if daño > 0:
            enemigo.salud -= daño
            print(f"El enemigo {enemigo.nomb} ha recibido {daño} puntos de daño.")
        else:
            print(f"El enemigo {enemigo.nomb} ha bloqueado el ataque.")
    
    def curarse(self):
        if(self.salud == self.salud_maxima):
            print(f"{self.nomb} ya tiene salud máxima: {self.salud_maxima}.")
        else:
            self.salud += 30
        
            if(self.salud > self.salud_maxima):
                self.salud = self.salud_maxima
            
            print(f"{self.nomb} se ha curado. Salud actual: {self.salud}")
        
    def defenderse(self):
        self.def_temporal = self.defensa + 5
        
        print(f"{self.nomb} se defiende. Defensa aumentada temporalmente a {self.def_temporal}")
    
    def reset_defensa(self):
        self.def_temporal = self.defensa
        
        print(f"La defensa de {self.nomb} ha vuelto a la normalidad.")
        
    def vive(self):
        return self.salud > 0
    

class Monstruo:
    def __init__(self, nomb, ataque, defensa, salud):
        self.nomb = nomb
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        
    def atacar(self, heroe):
        print(f"El monstruo {self.nomb} ataca a {heroe.nomb}")
        
        daño = self.ataque - heroe.def_temporal
        
        if daño > 0:
            heroe.salud -= daño
            print(f"El héroe {heroe.nomb} ha recibido {daño} puntos de daño.")
        else:
            print(f"El héroe {heroe.nomb} ha bloqueado el ataque.")
    
    def vive(self):
        return self.salud > 0
    
    
class Tesoro:
    def __init__(self):
        self.beneficios = ["Poción de fuerza", "Poción de resistencia", "Poción de salud"]
        
    def encontrar_tesoro(self, heroe):
        beneficio = random.choice(self.beneficios)
        
        print(f"{heroe.nomb} ha encontrado un tesoro: {beneficio}")
        
        if beneficio == "Poción de fuerza":
            heroe.ataque += 10
            print(f"El ataque de {heroe.nomb} aumenta a {heroe.ataque}")
        elif beneficio == "Poción de resistencia":
            heroe.defensa += 5
            print(f"La defensa de {heroe.nomb} aumenta a {heroe.defensa}")
        else:
            heroe.salud = heroe.salud_maxima
            print(f"La salud de {heroe.nomb} ha sido restaurada a {heroe.salud_maxima}")
            
            
class Mazmorra:
    def __init__(self, heroe):
        self.heroe = heroe
        self.monstruos = [Monstruo("Duende", 10, 5, 30), Monstruo("Slime", 15, 20, 40), Monstruo("Orco", 30, 50, 80), Monstruo("Dragón", 90, 55, 150)]
        self.tesoro = Tesoro()
        
    def jugar(self):
        print(f"{self.heroe.nomb} ha entrado en la mazmorra.")
        
        while(self.heroe.vive() and len(self.monstruos) > 0):
            enemigo = self.monstruos.pop(0)
            print(f"Te has encontrado con un {enemigo.nomb}.")
            self.enfrentar_enemigo(enemigo)
            
            if not self.heroe.vive():
                print(f"{self.heroe.nomb} ha muerto.")
                
            if not enemigo.vive():
                print(f"{self.heroe.nomb} ha derrotado al {enemigo.nomb}")
                self.buscar_tesoro()
        
        if self.heroe.vive():
            print(f"¡{self.heroe.nomb} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")
            
    def enfrentar_enemigo(self, enemigo):  
        while self.heroe.vive() and enemigo.vive():
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
                
    def buscar_tesoro(self):
        print("Buscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe)
        
def main():
    nombre_heroe = input("Introduce el nombre de tu héroe: ")
    heroe = Heroe(nombre_heroe)
   
    mazmorra = Mazmorra(heroe)
    mazmorra.jugar()
    
if __name__ == "__main__":
    main() 