import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk() #Clase que ejecua una interfaz
    root.title('Catalogo de Peliculas')
    # root.iconbitmap('img/catalogor.ico')
    root.resizable(0,0) #Modificar tamano de pantalla
    barra_menu(root)

    app = Frame(root = root)

    app.mainloop() #Va al final, porque indica el final de la ejecucion de la app

if __name__ == '__main__':
    main() #Ejecuta el metodo main