import tkinter as tk
from controlador import GameController
from modelo import GameModel

def main():
    root = tk.Tk()
    
    controller = GameController(root)

    root.mainloop()
    
if __name__ == "__main__":
    main()