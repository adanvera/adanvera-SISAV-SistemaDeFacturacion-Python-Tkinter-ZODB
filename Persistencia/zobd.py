#!/usr/bin/env python3
'''Modulo de la base de datos ZOBD: es la encargada de abrir 
y cerrar la base de datos, y al mismo tiempo de la persistencia 
de los datos. 
PARADIGMAS DE LA PROGRAMACUION'''

from ZODB import FileStorage, DB
import transaction

class MiZODB(object):
    def __init__(self, file):
        '''Es la encargada de crear la base de datos, y o al mismo tiempo de abrirla
        si la misma ya esta creada'''
        self.storage = FileStorage.FileStorage(file)
        self.database = DB(self.storage)
        self.conexion = self.database.open()
        self.raiz = self.conexion.root()

    def close(self):
        '''Encargada de cerrar la base de datos'''
        self.conexion.close()
        self.database.close()
        self.storage.close()

if __name__ == '__main__':
    pass