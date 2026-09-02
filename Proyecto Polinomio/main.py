import tkinter as tk
from model import Polinomio
from view import VistaPolinomio
from controller import ControladorPolinomio

def main():
    root = tk.Tk()
    root.title("Tkinter MVC App")
    
    model = Polinomio()
    view = VistaPolinomio(root)
    controller = ControladorPolinomio(view,model)
    
    root.mainloop()

if __name__ == "__main__":
    main()