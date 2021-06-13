#!/usr/bin/env python3
'''Modulo app:es la encargada de inicar el sistema y tiene la tarea de que el controlador proceda a llevar
a cabo las funciones debidas que el usuario va ingresando al utilizar el sistema.
PARADIGMAS DE LA PROGRAMACUION'''


from controlador import*
from view import*
import sys
from tkinter import Tk

class App:
    '''Clase que se utiliza para iniciar el sistema'''
    @staticmethod
    def main():
        control = Negocio()
        root = Tk()  #raiz de la vista Tkinter
        vista = View(control, root)
        vista.mainloop()

if __name__ == '__main__':
    App.main()