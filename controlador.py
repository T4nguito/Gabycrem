from tkinter import Tk
from sympy import im
import vista
import os



'''-------------
Controlador
--------------'''
class Controlador:

    def __init__(self, root_w):
        #PASO 2- Creo atributo de instancia mi_app guardo la ventana
        self.master = root_w
        #Atributo de instancia de TKvista
        self.objeto_vista = vista.VistaPrincipal(self.master)

if __name__ == "__main__": 
    master = Tk()
    
    #mi_app = vista.TKvista(root)
    #PASO 1 -Instancio el controlador
    mi_app = Controlador(master)
    master.mainloop()
