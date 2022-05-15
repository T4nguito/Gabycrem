from faulthandler import disable
import sqlite3
import re
from tkinter import DISABLED, END
from tkinter.font import NORMAL
from tkinter.messagebox import *
import vista

"""var_nombre = StringVar()
var_apellido = StringVar()
var_dni = IntVar()
var_nacimiento = IntVar()
var_categoria = StringVar()
"""

class Abmc():
    def __init__(self, ): pass
        
    def crear_base(self,):
        con = sqlite3.connect("mi_base.db")
        return con


    def crear_tabla(self, con):
        cursor = con.cursor()
        sql = """CREATE TABLE socios
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre varchar(20) NOT NULL,
                apellido varchar(20) NOT NULL,
                dni integer NOT NULL,
                fecha integer NOT NULL,
                categoria varchar(20) NOT NULL)
        """
        cursor.execute(sql)
        con.commit()


    try:
        con = crear_base()
        crear_tabla()
    except:
        pass


    def seleccionado(self, tree):
        valor = tree.selection()
        item = tree.item(valor)
        mi_idd = item["text"]
        return mi_idd, valor


    def insertar(
        self,
        entry_nombre,
        entry_apellido,
        entry_dni,
        entry_nacimiento,
        entry_categoria,
        nombre,
        apellido,
        dni,
        fecha,
        categoria,
        tree,
    ):
        cadena1 = nombre
        cadena2 = apellido
        patron = "^[A-Za-záéíóú]*$"
        if re.match(patron, cadena1):
            if re.match(patron, cadena2):
                con = self.crear_base()
                cursor = con.cursor()
                # mi_id = int(mi_id)
                data = (nombre, apellido, dni, fecha, categoria)
                sql = "INSERT INTO socios(nombre, apellido,  dni, fecha, categoria) VALUES (?, ?, ?, ?, ?);"
                cursor.execute(sql, data)
                con.commit()
                self.actualizar_treeview(tree)
                self.limpiar_campos(
                    entry_nombre,
                    entry_apellido,
                    entry_dni,
                    entry_nacimiento,
                    entry_categoria,
                )
            else:
                self.f_error("Campos ingresados en 'Apellido' incorrectos")
        else:
            self.f_error("Campos ingresados en 'Nombre' incorrectos")


    """
    def f_seleccionar(tree):
        # bt_guardar["state"] = DISABLED
        limpiar_campos()

        if tree.selection():
            valor = tree.selection()
            item = tree.item(valor)
            mi_id = item["text"]
            campos = item["values"]
            mi_id = int(mi_id)
            completar_campos(campos)
            # bt_modificar["state"] = NORMAL
            # bt_borrar["state"] = NORMAL
            return mi_id
        else:
            f_error("No hay ningún ítem seleccionado")


    def f_borrar(tree):
        # bt_borrar["state"] = DISABLED
        # bt_modificar["state"] = DISABLED
        if tree.selection():

            mi_id, valor = seleccionado()
            con = crear_base()
            cursor = con.cursor()
            data = (mi_id,)
            sql = "DELETE FROM socios WHERE id = ?;"
            cursor.execute(sql, data)
            con.commit()
            tree.delete(valor)
            limpiar_campos()
            # bt_guardar["state"] = NORMAL

        else:
            f_error("No hay ningún ítem seleccionado")
    """


    def actualizar_bd(self, nombre, apellido, dni, fecha, categoria, tree):

        con = self.crear_base()
        cursor = con.cursor()
        valor = tree.selection()
        item = tree.item(valor)
        mi_id = item["text"]
        mi_id = int(mi_id)
        data = (nombre, apellido, dni, fecha, categoria, mi_id)
        sql = "UPDATE socios SET nombre=?, apellido=?,  dni=?, fecha=?, categoria=? WHERE id= ?;"
        cursor.execute(sql, data)
        con.commit()
        self.actualizar_treeview(tree)


    def f_borrar(
        self,
        entry_nombre,
        entry_apellido,
        entry_dni,
        entry_nacimiento,
        entry_categoria,
        bt_borrar,
        bt_modificar,
        bt_guardar,
        tree,
    ):
        bt_borrar["state"] = DISABLED
        bt_modificar["state"] = DISABLED
        if tree.selection():

            mi_id, valor = self.seleccionado(tree)
            con = self.crear_base()
            cursor = con.cursor()
            data = (mi_id,)
            sql = "DELETE FROM socios WHERE id = ?;"
            cursor.execute(sql, data)
            con.commit()
            tree.delete(valor)
            self.limpiar_campos(
                entry_nombre,
                entry_apellido,
                entry_dni,
                entry_nacimiento,
                entry_categoria,
            )
            bt_guardar["state"] = NORMAL

        else:
            self.f_error("No hay ningún ítem seleccionado")


    def actualizar_treeview(self, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

        sql = "SELECT * FROM socios ORDER BY id DESC"
        con = self.crear_base()
        cursor = con.cursor()
        datos = cursor.execute(sql)

        resultado = datos.fetchall()
        for fila in resultado:
            mitreview.insert(
                "", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5])
            )


    def f_error(self, un_string):
        showerror("ERROR", un_string)


    def f_guardar(
        self,
        entry_nombre,
        entry_apellido,
        entry_dni,
        entry_nacimiento,
        entry_categoria,
        nombre,
        apellido,
        dni,
        nacimiento,
        categoria,
        tree,
    ):
        self.insertar(
            self,
            entry_nombre,
            entry_apellido,
            entry_dni,
            entry_nacimiento,
            entry_categoria,
            nombre.get(),
            apellido.get(),
            dni.get(),
            nacimiento.get(),
            categoria.get(),  # PERMITE GUARDAR AUNQUE EL CAMPO CATEGORIA ESTE VACIO. PORQUE????
            tree,
        )


    def limpiar_campos(

        self, nombre, apellido, dni, nacimiento, categoria
    ):  # Vacia los campos de ingreso de datos

        nombre.delete(0, END)
        apellido.delete(0, END)
        dni.delete(0, END)
        nacimiento.delete(0, END)
        categoria.delete(0, END)

        nombre.insert(0, "")
        apellido.insert(0, "")
        dni.insert(0, "")
        nacimiento.insert(0, "")
        categoria.insert(0, "")


    def f_modificar(
        self,
        entry_nombre,
        entry_apellido,
        entry_dni,
        entry_nacimiento,
        entry_categoria,
        nombre,
        apellido,
        dni,
        nacimiento,
        categoria,
        tree,
        bt_guardar,
        bt_modificar,
        bt_borrar,
    ):
        bt_modificar["state"] = DISABLED
        bt_borrar["state"] = DISABLED
        bt_guardar["state"] = NORMAL
        self.actualizar_bd(
            nombre.get(),
            apellido.get(),
            dni.get(),
            nacimiento.get(),
            categoria.get(),
            tree,
        )
        self.limpiar_campos(
            entry_nombre,
            entry_apellido,
            entry_dni,
            entry_nacimiento,
            entry_categoria,
        )

    def completar_campos(self, campos):  # Completa los campos de ingreso de datos me lo llevo al modelo a ver que onda

        self.entry_nombre.insert(0, campos[0])
        self.entry_apellido.insert(0, campos[1])
        self.entry_dni.insert(0, campos[2])
        self.entry_nacimiento.insert(0, campos[3])
        self.entry_categoria.insert(0, campos[4])

        def f_seleccionar(self, tree):
            self.bt_guardar["state"] = DISABLED
            self.limpiar_campos(
            self.entry_nombre, self.entry_apellido, self.entry_dni, self.entry_nacimiento, self.entry_categoria)

            if tree.selection():
                valor = tree.selection()
                item = tree.item(valor)
                mi_id = item["text"]
                campos = item["values"]
                mi_id = int(mi_id)
                self.completar_campos(campos)
                self.bt_modificar["state"] = NORMAL
                self.bt_borrar["state"] = NORMAL
                return mi_id
            else:
                self.f_error("No hay ningún ítem seleccionado")