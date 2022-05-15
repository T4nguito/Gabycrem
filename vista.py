from doctest import master
from operator import itemgetter
import os
from sympy import root
from pytest import Item
import modelo
from tkinter import *
from tkinter import DISABLED, Button
from tkinter.messagebox import *
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import StringVar, IntVar
import tkinter as tk
from PIL import ImageTk, Image


from tkinter import ttk
from tkinter.messagebox import *

import tkinter as tk


from tkinter import DISABLED, END, NORMAL  # StringVar, IntVar





"""
var_nombre, var_apellido, var_dni, var_nacimiento, var_categoria 

entry_nombre, entry_apellido, entry_dni, entry_nacimiento, entry_categoria
    
    
    var_nombre = StringVar()
    var_apellido = StringVar()
    var_dni = IntVar()
    var_nacimiento = IntVar()
    var_categoria = StringVar()
"""


##############################################################################
#VISTA
##############################################################################

'''--------------------
Hacemos una Clase para administrar "todo" vista.
Las funciones las ponemos adentro.
--------------------'''

class VistaPrincipal(): 
    

    def __init__(self, windows): 
        self.master = windows
        self.master.title("Planilla del Club")

    
        BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
        ruta = os.path.join(BASE_DIR, "logo.jpg")
        #master.geometry ("800x700")

        var_nombre = StringVar()
        var_apellido = StringVar()
        var_dni = IntVar()
        var_nacimiento = IntVar()
        var_categoria = StringVar()

        self.espacio = Label(master)
        self.espacio.grid(row=0, columnspan=4)
        self.nombre_del_club = Label(self.master, text="CLUB UNIVERSITARIO")
        self.nombre_del_club.grid(columnspan=8, row=1, column=0)

        self.nombre_del_club2 = Label(master, text="DE RUGBY")
        self.nombre_del_club2.grid(columnspan=8, row=2, column=0)
        self.espacio = Label(self.master)
        self.espacio.grid(row=4, columnspan=4)

        self.logo = Image.open(ruta)
        self.resize_logo = self.logo.resize((100, 100))
        self.logo2 = ImageTk.PhotoImage(self.resize_logo)
        self.mi_logo = ttk.Label(self.master, image=self.logo2)
        self.mi_logo.grid(row=0, column=6, rowspan=4, pady=10)

        self.nombre = Label(self.master, text="Nombre")
        self.nombre.grid(row=7, column=0, sticky="w", padx=10)

        self.apellido = Label(self.master, text="Apellido", anchor="n")
        self.apellido.grid(row=7, column=2, sticky="w", padx=10)

        self.dni = Label(self.master, text="DNI", anchor="n")
        self.dni.grid(row=8, column=0, sticky="w", padx=10)

        self.nacimiento = Label(self.master, text="Fecha de nacimiento", anchor="n")
        self.nacimiento.grid(row=8, column=2, sticky="w", padx=10)

        self.categoria = Label(self.master, text="Categoria", anchor="n")
        self.categoria.grid(row=9, column=0, sticky="w", padx=10)
        self.w_ancho = 25

        self.entry_nombre = Entry(self.master, textvariable=var_nombre, width=self.w_ancho)
        self.entry_nombre.grid(row=7, column=1)

        self.entry_apellido = Entry(self.master, textvariable=var_apellido, width=self.w_ancho)
        self.entry_apellido.grid(row=7, column=3)

        self.entry_dni = Entry(self.master, textvariable=var_dni, width=self.w_ancho)
        self.entry_dni.grid(row=8, column=1)

        self.entry_nacimiento = Entry(self.master, textvariable=var_nacimiento, width=self.w_ancho)
        self.entry_nacimiento.grid(row=8, column=3)

        self.entry_categoria = Entry(self.master, textvariable=var_categoria, width=self.w_ancho)
        self.entry_categoria.grid(row=9, column=1)

        self.espacio = Label(self.master)
        self.espacio.grid(row=10, columnspan=4)
        

        self.tree = ttk.Treeview(self.master)

        self.tree["columns"] = ("Nombre", "Apellido", "DNI", "Fecha de Nacimiento", "Categoria")

        self.tree.column("#0", width=50, minwidth=20, anchor="w")
        self.tree.column("Nombre", width=200, minwidth=20, anchor="w")
        self.tree.column("Apellido", width=200, minwidth=20, anchor="w")
        self.tree.column("DNI", width=100, minwidth=20, anchor="w")
        self.tree.column("Fecha de Nacimiento", width=150, minwidth=20, anchor="w")
        self.tree.column("Categoria", width=80, minwidth=20, anchor="w")

        self.tree.heading("#0", text="ID")
        self.tree.heading("Nombre", text="NOMBRE")
        self.tree.heading("Apellido", text="APELLIDO")
        self.tree.heading("DNI", text="DNI")
        self.tree.heading("Fecha de Nacimiento", text="FECHA DE NACIMIENTO")
        self.tree.heading("Categoria", text="CATEGORIA")

        self.tree.grid(column=0, row=11, columnspan=8, padx=10)

        

        

        

    def actualizar_treeview(self, selftree):
        bt_guardar = Button(
            text="Guardar",
            command=lambda: self.f_guardar(

                self.entry_nombre,
                self.entry_apellido,
                self.entry_dni,
                self.entry_nacimiento,
                self.entry_categoria,
                self.var_nombre,
                self.var_apellido,
                self.var_dni,
                self.var_nacimiento,
                self.var_categoria,
                self.tree,
            ),
            bg="#DCDCDC",
            width=20,
        )
        bt_guardar.grid(row=10, column=-0, pady=5, padx=5, columnspan=1)

        bt_modificar = Button(
            master,
            text="Modificar",
            command=lambda: self.f_modificar(
                self.entry_nombre,
                self.entry_apellido,
                self.entry_dni,
                self.entry_nacimiento,
                self.entry_categoria,
                self.var_nombre,
                self.var_apellido,
                self.var_dni,
                self.var_nacimiento,
                self.var_categoria,
                self.tree,
                bt_guardar,
                bt_modificar,
                bt_borrar,
            ),
            bg="#DCDCDC",
            width=20,
            state=DISABLED,
        )
        bt_modificar.grid(row=10, column=1, pady=5, padx=5, columnspan=1)

        bt_seleccionar = Button(
            master,
            text="Seleccionar",
            command=lambda: self.f_seleccionar(self.tree),
            bg="#DCDCDC",
            width=20,
        )
        bt_seleccionar.grid(row=10, column=3, pady=5, padx=5, columnspan=2)

        bt_borrar = Button(self,
            master,
            text="Borrar",
            command=lambda: self.f_borrar(
                self.entry_nombre,
                self.entry_apellido,
                self.entry_dni,
                self.entry_nacimiento,
                self.entry_categoria,
                bt_borrar,
                bt_modificar,
                bt_guardar,
                self.tree,
            ),
            bg="#DCDCDC",
            width=20,
            state=DISABLED,
        )
        bt_borrar.grid(row=10, column=5, pady=5, padx=5, columnspan=2)

        bt_salir = Button(master, text="Salir", command=master.quit, bg="#DCDCDC", width=15)
        bt_salir.grid(row=15, column=6, sticky="SE", padx=10, pady=10)

        
        
    #def limpiar_campos(delf, entry_nombre, entry_apellido, entry_dni, entry_nacimiento, entry_categoria):

