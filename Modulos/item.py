#!/usr/bin/env python3
'''
Modulo de los items: posee las clases que se necesitan para el negocio para utilizar los items
o servicios que posee el negocio 
PARADIGMAS DE LA PROGRAMACUION'''

from abc import ABCMeta, abstractmethod

class Vendible(metaclass = ABCMeta):

    '''Clase abstracta que tiene como finalidad la de representar que un item y/o servicio
    puede venderse'''
    @abstractmethod
    def vender(self):
        pass
    
    @abstractmethod
    def reponer(self):
        pass

class Item(Vendible):
    '''Clase que representa de manera general a los articulos/servicios de manera general
    que cuenta el negocio'''
    def __init__(self, codigo_item, descripcion, precio_unitario):
        self.__codigo_item = codigo_item
        self.__descripcion = descripcion
        self.__precio_unitario = precio_unitario

    def get_codigo_item(self):
        return self.__codigo_item
    
    def set_codigo_item(self, codigo_item):
        self.__codigo_item = codigo_item
    
    def get_descripcion(self):
        return self.__descripcion
    
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
        
    def get_precio_unitario(self):
        return self.__precio_unitario
    
    def set_precio_unitario(self, precio_unitario):
        self.__precio_unitario = precio_unitario


    def vender(self):
        '''Metodo que tiene como finalidad la de retornar los
        atributos correspondientes a cada item'''
        return '{:<28}{:<1}'.format(self.__descripcion, str(self.__precio_unitario))

    def reponer(self):
        pass

        '''restar items de total para que despues se pueda reponer que en un futuro podria implementarse'''

    def __eq__(self,codigo_item):
        '''Este metodo tiene como finalidad la de determinar si dos items 
        son iguales'''
        return self.__codigo_item == codigo_item

    def __str__(self):
        return '{:<14}{:<28}{:<1}'.format(self.__codigo_item , self.__descripcion , str(self.__precio_unitario))




class Articulo(Item):
    '''Clase que representan a los articulos de papeleria que estan dentro del negocio'''

    def __init__(self, codigo_item, descripcion, precio_unitario):
        Item.__init__(self, codigo_item, descripcion, precio_unitario)

    def __eq__(self, item):
        return Item.__eq__(self, item.get_codigo_item())


class Servicios(Item):
    '''Clase que representan a los servicios ofrecidos por el negocio, que seran tratados como
    articulos, solo que tendran la etiqueta de servicio a la hora de ser cargado por el usuario'''

    def __init__(self, codigo_item, descripcion, precio_unitario):
        Item.__init__(self, codigo_item, descripcion, precio_unitario)

    def __eq__(self, item):
        return Item.__eq__(self, item.get_codigo_item())



class Pedido(Servicios):
    '''Clase abstracta que representa un pedido hecho por el cliente ante un servicio.
    A ser implementada en un futuro por la empresa'''
    pass

