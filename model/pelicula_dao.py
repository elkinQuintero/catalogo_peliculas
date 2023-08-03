from .conexion_db import ConexionDB
from tkinter import messagebox

class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'

def crear_tabla():
    conexion = ConexionDB()
    
    # query = ''' 
    # CREATE TABLE  project.peliculas(
    #     id_pelicula INT auto_increment NOT NULL,
    #     nombre varchar(100) NULL,
    #     duracion varchar(10) NULL,
    #     genero varchar(100) NULL,
    #     PRIMARY KEY(id_pelicula)
    # )
    # '''

    query = ''' 
    CREATE TABLE  peliculas(
        id_pelicula INTEGER,
        nombre varchar(100),
        duracion varchar(10),
        genero varchar(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(query)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)


def borrar_tabla():
    conexion = ConexionDB()

    query = 'DROP TABLE peliculas'
    try:
        conexion.cursor.execute(query)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla de la base de datos se borro con éxito'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)


def guardar(pelicula):
    conexion = ConexionDB()
    # query = 'INSERT INTO peliculas(nombre,duracion,genero) VALUES(%s,%s,%s)'
    query = f"INSERT INTO peliculas(nombre,duracion,genero) VALUES('{pelicula.nombre}','{pelicula.duracion}', '{pelicula.genero}')"
    try:
        # valores = (pelicula.nombre,pelicula.duracion,pelicula.genero)
        # conexion.cursor.execute(query,valores)
        conexion.cursor.execute(query)
        conexion.cerrar()
        titulo = 'Creación Pelicula'
        mensaje = 'La pelicula se creó con exito'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Creación Pelicula'
        mensaje = 'Error: la pelicula no se pudo guardar ya que la tabla no esta creada'
        messagebox.showerror(titulo, mensaje)


def listar():
    conexion = ConexionDB()
    lista_peliculas = []
    query = 'SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(query)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Error: no existe tabla. Creala'
        messagebox.showerror(titulo, mensaje)
    
    return lista_peliculas


def editar(pelicula, id_pelicula):
    conexion = ConexionDB()

    query = f"UPDATE peliculas SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}', genero = '{pelicula.genero}' WHERE id_pelicula = {id_pelicula}"

    try:
        conexion.cursor.execute(query)
        conexion.cerrar()
        titulo = 'Actualización Pelicula'
        mensaje = 'La pelicula se actualizo exitosamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Actualización Pelicula'
        mensaje = 'La pelicula no se pudo actualizar'
        messagebox.showerror(titulo, mensaje)

       
def eliminar(id_pelicula):
    conexion = ConexionDB()
    query = f"DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}"

    try:
        conexion.cursor.execute(query)
        conexion.cerrar()
        titulo = "Eliminar Pelicula"
        mensaje = 'Pelicula eliminada exitosamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Eliminar Pelicula'
        mensaje = 'Error: no se puede eliminar la pelicula'
        messagebox.showerror(titulo, mensaje)        

        
