from heroe import Heroe
from mazmorra import Mazmorra
    

def main():
    nombre_heroe = input("Introduce el nombre de tu héroe: ")
    heroe = Heroe(nombre_heroe)
   
    mazmorra = Mazmorra(heroe)
    mazmorra.jugar()
   
#Solo deja que se ejecute el main el programa principal. 
if __name__ == "__main__":
    main() 