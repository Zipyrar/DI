import tkinter as tk
from controlador import GameController
from modelo import GameModel
from vista import MainMenu, GameView

def main():
    root = tk.Tk()
    
    controller = GameController(root, GameModel, MainMenu, GameView)

    root.mainloop()
    
if __name__ == "__main__":
    main()