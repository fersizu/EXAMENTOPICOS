# Erick Fernando Siqueiros Zuñiga 
# Brandon Isaac Leyva Gonzalez
# Brandon David Vargas Nuñez
from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN
from turtle import width
import base_datos
# * = todo

mysql = base_datos.BD()
ventana = Tk()
ventana.title("Crud Python MySQL")
ventana.geometry("1100x400")

#   Variables con tkinter de la tabla peliculas

idp = StringVar()
nombre_pelicula = StringVar()
duracion = StringVar()
genero  = StringVar()
director = StringVar()

# LabelFrames

butones = LabelFrame(ventana,background="#A4D3EE")
butones.place(x = 0, y = 0, width = 70, height = 400)

labels = LabelFrame(ventana,background="#CDCDC1")
labels.place(x = 70, y = 0, width = 210, height = 400)

marco = LabelFrame(ventana)
marco.place(x = 260, y = 0, width = 720, height = 400)

#   Botones, Labels, TextInputs

btnNuevo = Button(butones,background="#1C86EE", text = "Nuevo", command = lambda:agregar())
btnNuevo.grid(column = 0, row = 0, pady = 5)

btnModificar = Button(butones,background="#1C86EE", text = "Modificar", command = lambda:actualizar())
btnModificar.grid(column = 0, row = 1, pady = 5)

btnEliminar = Button(butones,background="#1C86EE", text = "Eliminar", command = lambda:eliminar())
btnEliminar.grid(column = 0, row = 2, pady = 5)

lblPelicula = Label(labels, text = "Pelicula ")
lblPelicula.grid(column = 1, row = 0, padx = 5, pady = 5)
txtPelicula = Entry(labels, textvariable = nombre_pelicula)
txtPelicula.grid(column = 1, row = 1)

lblGenero = Label(labels, text = "Genero ")
lblGenero.grid(column = 1, row = 2, padx = 5, pady = 5)
txtGenero = Entry(labels, textvariable = genero)
txtGenero.grid(column = 1, row = 3)

lblDuracion = Label(labels, text = "Duracion: ")
lblDuracion.grid(column = 1, row = 4, padx = 5, pady = 5)
txtDuracion = Entry(labels, textvariable = duracion)
txtDuracion.grid(column = 1, row = 5)

lblDirector = Label(labels, text = "Director: ")
lblDirector.grid(column = 1, row = 6, padx = 5, pady = 5)
txtDirector = Entry(labels, textvariable = director)
txtDirector.grid(column = 1, row = 7)

btnGuardar = Button(labels,background="#458B00", text = "Guardar", command = lambda:agregar())
btnGuardar.grid(column = 1, row = 8, pady = 5)

btnCancelar = Button(labels,background="#FF3030", text = "Cancelar", command = lambda:actualizar())
btnCancelar.grid(column = 2, row = 8, pady = 5)

tvPelicula = ttk.Treeview(marco)
tvPelicula.grid(column = 2, row = 3, columnspan = 4, padx = 5)
tvPelicula["columns"] = ("Id", "Pelicula", "Genero", "Duracion","Director")
tvPelicula.column("#0", width = 0, stretch = NO)
tvPelicula.column("Id", width = 100, anchor = CENTER)
tvPelicula.column("Pelicula", width = 200, anchor = CENTER)
tvPelicula.column("Genero", width = 100, anchor = CENTER)
tvPelicula.column("Duracion", width = 100, anchor = CENTER)
tvPelicula.column("Director", width = 200, anchor = CENTER)
tvPelicula.heading("Id", text = "Id", anchor = CENTER)
tvPelicula.heading("Pelicula", text = "Pelicula", anchor = CENTER)
tvPelicula.heading("Genero", text = "Genero", anchor = CENTER)
tvPelicula.heading("Duracion", text = "Duracion", anchor = CENTER)
tvPelicula.heading("Director", text = "Director", anchor = CENTER)


def validar():
    return len(idp.get()) and len( nombre_pelicula.get()) and len( duracion.get()) and len( genero.get()) and len(director.get())
def vaciar_tabla():
    filas = tvPelicula.get_children()
    for fila in filas:
        tvPelicula.delete(fila)

def llenar_tabla():
    vaciar_tabla()
    consulta = mysql.select("pelicula")
    for fila in consulta:
        id = fila[0]
        tvPelicula.insert("",END, text = id, values = fila)

def limpiar():
    idp.set('')
    nombre_pelicula.set('')
    duracion.set('')
    genero.set('')
    director.set('')

def agregar():
    if validar():
        variables = idp.get(), nombre_pelicula.get(), duracion.get(), genero.get(), director.get()
        sql = "insert from pelicula into (id, nombre_pelicula, duracion, id_genero, id_director) values (%s, %s, %s, %s, %s)"
        mysql.agregar(sql)
        llenar_tabla()
        limpiar()

def actualizar():
    pass

def eliminar():
    item_seleccionado = tvPelicula.focus()
    detalle = tvPelicula.item(item_seleccionado)
    id = detalle.get("values")[0]
    if id > 0:
        sql = 'delete from pelicula where id = ' + str(id)
        mysql.eliminar(sql)
        llenar_tabla()

llenar_tabla()
ventana.mainloop()
