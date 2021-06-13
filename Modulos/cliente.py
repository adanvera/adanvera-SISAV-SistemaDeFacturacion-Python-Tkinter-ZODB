#!/usr/bin/env python3
'''
Modulo de los Clientes: este contiene los datos que se necesitan para cuando se lo 
requiera, ya sea para crear las boletas de ventas de items y o adquisicion de 
servicios de la Microempresa 'AV Servicos Digitales e Imprenta'
 
PARADIGMAS DE LA PROGRAMACUION'''


from abc import ABCMeta, abstractmethod

class Persona(metaclass = ABCMeta):

    '''Metodo cuyo proposito es representar a las personas
    que posteriormente seran utilizadas dentro de las diferentes clases en el 
    sistema'''
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def __str__(self):
        '''Metodo que se encargara de retornar los datos de la 
        persona'''
        return 'Sr./Sra.: '+ self.__nombre +' '+ self.__apellido



class Cliente(metaclass = ABCMeta):
    '''Clase abstracta que tiene como finalidad la de representar de manera general
    los clientes que tendrá la empresa'''

    def __init__(self, ruc):
        self.__ruc = ruc 
    
    def get_ruc(self):
        return self.__ruc 

    def set_ruc(self, ruc):
        self.__ruc = ruc

    def __eq__(self, cliente_ruc):
        return self.__ruc == cliente_ruc

    def __str__(self):
        return ' RUC: ' + self.__ruc

class ClienteExistente(Cliente):
    '''Clase que tiene como finalidad la de representar de manera general los clientes que pueda llegar a tener el negocio.'''
    def __init__(self, nombre, apellido, ruc):
        Persona.__init__(self, nombre, apellido)
        Cliente.__init__(self, ruc)

    def get_nombre(self):
        return Persona.get_nombre(self)

    def get_apellido(self):
        return Persona.get_apellido(self)

    def cambiar_nombre_cliente(self, nombre):
        Persona.set_nombre(self, nombre)
    
    def cambiar_apellido_cliente(self, apellido):
        Persona.set_apellido(self, apellido)
    
    def __str__(self):
        return Persona.__str__(self) + Cliente.__str__(self)


class ClienteIncognito(Cliente):
    '''Clase que representa a un cliente primario, o por defecto, esta  clase tiene como finalidad si el cliente requiera 
    una boleta de venta y no desee entregar sus datos personales para la misma'''
    cantidad = 0
    def __init__(self):
        self.__nombre = 'N/A'
        Cliente.__init__(self, 'xxx')
        self.cantidad = 1
    def __str__(self):
        return 'Sr./Sra.: ' + self.__nombre + '\t' +'  '+Cliente.__str__(self)



if __name__ == '__main__':
    pass
