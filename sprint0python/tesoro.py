import random

class Tesoro:
    #Definimos los tipos de beneficios.
    def __init__(self):
        self.beneficios = ["Poción de fuerza", "Poción de resistencia", "Poción de salud"]
        
    def encontrar_tesoro(self, heroe):
        #Elige al azar uno de los tres tesoros de la lista definida anteriormente.
        beneficio = random.choice(self.beneficios)
        
        print(f"{heroe.nomb} ha encontrado un tesoro: {beneficio}")
        
        if beneficio == "Poción de fuerza":
            heroe.ataque += 20
            print(f"El ataque de {heroe.nomb} aumenta a {heroe.ataque}")
        elif beneficio == "Poción de resistencia":
            heroe.defensa += 15
            print(f"La defensa de {heroe.nomb} aumenta a {heroe.defensa}")
        else:
            #Mensaje adicional si su salud ya está al máximo.
            if heroe.salud == heroe.salud_maxima:
                print(f"{heroe.nomb} se bebió la poción de salud, pero ya tenía la salud al máximo.")
            else:
                heroe.salud = heroe.salud_maxima
                print(f"La salud de {heroe.nomb} ha sido restaurada al máximo.")