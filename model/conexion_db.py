#import mysql.connector as mysql
import sqlite3

class ConexionDB:
    def __init__(self):
        #self.db = mysql.connect(host="192.168.0.68", user="excelec", passwd="1234", database="project") 
        #self.cursor = self.db.cursor()
        self.base_datos = 'database/peliculas.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
        

    def cerrar(self):
        # self.db.commit()
        # self.db.close()
        self.conexion.commit()
        self.conexion.close()