class Heroe:
    #Definimos sus atributos.
    def __init__(self, nomb):
        self.nomb = nomb
        self.ataque = 70
        self.defensa = 45
        self.salud = 100
        self.salud_maxima = 100
        #Controlamos con esto las funciones de subida de defensa de forma más precisa.
        self.def_temporal = self.defensa
    
    def atacar(self, enemigo): 
        #'enemigo' llama al monstruo que el héroe está enfrentando en ese momento.
        print(f"{self.nomb} ataca a {enemigo.nomb}")
        
        daño = self.ataque - enemigo.defensa
    
        if daño > 0: #El daño es mayor a la defensa del monstruo.
            enemigo.salud -= daño
            print(f"El enemigo {enemigo.nomb} ha recibido {daño} puntos de daño.")
        else:
            print(f"El enemigo {enemigo.nomb} ha bloqueado el ataque.")
    
    def curarse(self):
        if(self.salud == self.salud_maxima):
            print(f"{self.nomb} ya tiene su salud al máximo.")
        else:
            self.salud += 30
        
            #Comprueba que la salud del héroe no exceda la máxima.
            if(self.salud > self.salud_maxima):
                self.salud = self.salud_maxima
            
            print(f"{self.nomb} se ha curado 30 de vida.")
        
    def defenderse(self):
        self.def_temporal = self.defensa + 15
        
        print(f"{self.nomb} se defiende. Defensa aumentada temporalmente a {self.def_temporal}")
    
    def reset_defensa(self):
        #Gracias al atributo def. temporal, se controla que vuelva a la normalidad.
        self.def_temporal = self.defensa
        
        print(f"La defensa de {self.nomb} ha vuelto a la normalidad.")
        
    #Comprueba si está vivo.
    def vive(self):
        return self.salud > 0