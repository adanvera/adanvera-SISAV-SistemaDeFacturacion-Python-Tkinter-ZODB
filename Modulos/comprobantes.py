#!/usr/bin/env python3
'''
Modulo de los comprobantes: la misma posee todas las clases necesarias para generar las
boletras de ventas del negocio.
PARADIGMAS DE LA PROGRAMACUION
'''


from abc import ABCMeta, abstractmethod
from Modulos.cliente import *
from Modulos.item import *
import time


class Comprobantes(metaclass = ABCMeta):
    '''Una clase abstracta que tiene la funcion de 
    representar un tipo cualquiera de comprobantes
    que podria llegar a tener el negocio'''

    def __init__(self, cliente, items):
        self.__cliente = cliente
        self.__items = items

    def set_item(self, items):
        self.__items = items

    def get_items(self):
        return self.__items
    
    def get_cliente(self):
        return self.__cliente

class BoletaDeVenta(Comprobantes):
    '''Clase queTiene como finalidad la de representar la boleta de 
    venta emitida por el Negocio como comprobante de compras
    para los clientes.. Esta clase  es heredada de Comprobantes'''
    num_de_boleta = 0

    def __init__(self, cliente, items):
        Comprobantes.__init__(self, cliente, items)
        self.__fecha = time.strftime('%d/%m/%y')
        BoletaDeVenta.num_de_boleta +=1
        self.__num_de_boleta = BoletaDeVenta.num_de_boleta

    def get_fecha(self):
        return self.__fecha

    def get_num_de_boleta(self):
        return self.__num_de_boleta

    def caluclo_de_subtotales(self):
        '''Metodo para llevar a cabo la obtencion de los subtotales
        de cada item'''
        sub_totales = []
        for items in Comprobantes.get_items(self):
            sub_total = 0
            for item in items:
                sub_total += item.get_precio_unitario()
            sub_totales.append(sub_total)

        return sub_totales

    def calculo_de_total(self, sub_totales):
        '''Metodo para calcular el monto total a pagar
        por el cliente, usando como parametro el calculo de 
        los subtotales para realizar dicho calculo'''
        monto_total = 0
        for sub_total in sub_totales:
            monto_total += sub_total
        return monto_total


    def __eq__(self, boleta_de_venta):
        return self.__num_de_boleta == boleta_de_venta.get_num_de_boleta()


class BoletaDeCompra(Comprobantes):
    '''Tiene como funcion la de representar la boleta emitida por 
    el proveedor para el Negocio que podria llegar a implementarse en un futuro'''
    @abstractmethod
    def __init__(self):
        pass


if __name__== '__main__':
    pass