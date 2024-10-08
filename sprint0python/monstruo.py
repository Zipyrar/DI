class Monstruo:
    #Definimos sus atributos.
    def __init__(self, nomb, ataque, defensa, salud):
        self.nomb = nomb
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        
    def atacar(self, heroe):
        print(f"El monstruo {self.nomb} ataca a {heroe.nomb}")
        
        daño = self.ataque - heroe.def_temporal
        
        if daño > 0: #El daño es mayor a la defensa del héroe.
            heroe.salud -= daño
            print(f"El héroe {heroe.nomb} ha recibido {daño} puntos de daño.")
        else:
            print(f"El héroe {heroe.nomb} ha bloqueado el ataque.")
    
    #Comprueba si está vivo.
    def vive(self):
        return self.salud > 0