#!/usr/bin/env python3
'''Modulo de los Controladores: esta se encarga de llevar a cabo la tarea de realizar toda la logica que se
halla en el sistema del negocio.
PARADIGMAS DE LA PROGRAMACUION
'''

from abc import ABCMeta, abstractmethod
from os import execve
import re

from ZODB.DB import KeyedConnectionPool
from zodbpickle.pickle_3 import INT
from Modulos.item import *
from Modulos.cliente import *
from Modulos.comprobantes import *
from model import *
from view import *
from datetime import *

class Empresa(metaclass = ABCMeta):
    '''Clase abstracta que tiene la finalidad la de representar o hacer referencia
    al negocio'''
    def __init__(self, name):
        self.__nombre = name

class Negocio(Empresa):
    '''Clase que representa de manera general al negocio y a las actividades
    que llegue a hacer dentro de la misma'''
    def __init__(self):
        Empresa.__init__(self, 'AV SERVICIOS DIGITALES E IMPRENTAS')
        self.model = Model()
        '''Directorio donde se encuentran las bases de datos de los items, clientes y 
        boletas del negocio'''
        self.directorio_item = './Persistencia/BaseItems/Items.fs'
        self.directorio_cliente = './Persistencia/BaseClientes/Clientes.fs'
        self.directorio_boleta = './Persistencia/BaseBoletas/Boletas.fs'
        self.cliente = ClienteIncognito()
        self.__items = self.model.objeto_lista(self.directorio_item)
        self.__clientes = self.model.objeto_lista(self.directorio_cliente)
        self.__boletas = self.model.objeto_lista(self.directorio_boleta)
        '''Si se tiene el caso que hay boletas ya alamacenadas en la base de datos de boletas
        , esta misma recupera el ultimo numero de boleta generado, para poder continuar a 
        partir de ese numero'''
        if self.__boletas:
            BoletaDeVenta.num_de_boleta = self.__boletas[-1].get_num_de_boleta()

    def vender(self, boleta_de_venta, cliente_ingresado):
        '''Metodo encargada de guardar la boleta de venta generada, y en caso contrario que el cliente no este
        en la base de datos, la misma indicara que la venta ha sido realizada'''
        if not isinstance (cliente_ingresado, ClienteIncognito):
            try:
                #obtner el cliente por su ruc
                cliente = self.model.extraer_objetos_alojados(self.directorio_cliente, cliente_ingresado.get_ruc())
            except KeyError:
                self.model.base_de_datos.close()
                '''si el cliente no se encuentra almancenada en la base de datos, la misma
                se guarda para poder preoceder con al venta'''
                self.model.objeto_guardar(self.directorio_cliente, cliente_ingresado,cliente_ingresado.get_ruc())
                self.__clientes = self.model.objeto_lista(self.directorio_cliente)
        '''Se guarda la boleta generada en la base de datos y la misma actualiza la lista de boletas'''
        self.model.objeto_guardar(self.directorio_boleta, boleta_de_venta, str(boleta_de_venta.num_de_boleta))
        self.__boletas = self.model.objeto_lista(self.directorio_boleta)

    def generacion_de_boleta(self,items_ingresados, cantidades, nombre_de_cliente= '', apellido_de_cliente='', ruc_cliente=''):
        '''METODO encargado de generar una boleta de venta, recibiendo parametros
        lista de articulos, las cantidades correspondientes, y llenado automatico del campo cliente si se encuentra en la base de datos o
        en todo caso su registro en la misma.
        La misma retornara 
        1 si hubo algun error, emitiendo un mensaje en la misma
        0 indicando que la operacion fue exitosa
        '''
        items_a_vender = []
        items = []
        indice_cant_items = 0
        #recorrido de la lista de items que se recibe
        for item in items_ingresados:
            for cantidad in range(int(cantidades[indice_cant_items])):
                #se genera la cantidad de un item
                items.append(item)
            indice_cant_items+=1
            #se agrega los items generados en cantidad, a una lista de items
            items_a_vender.append(items)
        try:
            #HACE Una busqueda del cliente en la base de datos de clientes mediante el parametro ruc
            cliente = self.model.extraer_objetos_alojados(self.directorio_cliente, ruc_cliente)
        except KeyError:
            self.model.base_de_datos.close()
            if not nombre_de_cliente and not apellido_de_cliente and not ruc_cliente:
                '''en el caso de no haberse ingresado ningun campo del cliente, se utilizara el cliente por defecto'''
                cliente = self.cliente 
            #En el caso de que no se haya ingrsado alguno de los datos del
            #cliente hará un return con los errores o advertencias correspodientes'''
            elif not ruc_cliente:
                return 1, 'RUC DE CLIENTE NO INGRESADO'
            elif not nombre_de_cliente:
                return 1,'NOMBRE DE CLIENTE NO INGRSADO'
            elif not apellido_de_cliente:
                return 1, 'APELLIDO DE CLIENTE NO INGRESADO'
            else:
                '''Se preocede a crear un nuevo cliente si los campos estan
                completos y la misma no esta en la base de datos de clientes
                del negocio'''
                cliente = ClienteExistente(nombre_de_cliente, apellido_de_cliente, ruc_cliente)
        boleta_de_venta = BoletaDeVenta(cliente, items_a_vender)
        #si se lleva todo a cabo, procede a retornar 0 y tambien la boleta generada
        return 0, boleta_de_venta

    def actualizacion_boleta_items(self, boleta, items_ingresados, cantidades):
        '''Metodo que tiene tiene como proposito actualizar los articulos de una boleta de un cliente
        si requiera modificarlos'''
        items_a_vender = []
        items =[]
        indice_cantidad_item = 0
        #procede a realizar un recorrido en la lista de items que recibe como parametro
        for item in items_ingresados:
            for cantidad in range(int(cantidades[indice_cantidad_item])):
                #se genera la cantidad de un item 
                items.append(item)
            indice_cantidad_item += 1
            #se va agregando los items que se generan en cantidad a una lista de items
            items_a_vender.append(items)
            items = []
        #procede a actualizar la boleta de venta correspondiente, con los nuevos items que el cliente este adquiriendo
        boleta.set_item(items_a_vender)
        return boleta

    def validar_cantidad_item(self, cantidad):
        '''Metodo que fiene como finalidad la de verficiar y o mas bien validar la cantidad
        del item. Si la cantidad es valida retorna 1 o 0 con el mensaje correspondiente'''
        if not cantidad:
            return 1, 'CANTIDAD DE ITEM NO INGRESADA'
        try:
            cantidad = int(cantidad)
            if cantidad<1:
                raise ValueError
            else:
                return 0, 'CANTIDAD CORRECTA'
        except ValueError:
            return 1, 'ERROR. CANTIDAD NO VALIDA'

    def modificar_descripcion_item(self, codigo_item, descripcion):
        '''Metodo que se encarga de modificar/actualizar la descipcion de un determinado
        item.
        Retorna 1 o 0 dependiendo si el proceso se llevó a cabo exitosamente o en caso
        contrario si hubo algun error, el retorno dará un mensaje determinado si se presentan
        los casos'''
        #obtenemos el articulo de la base de datos a partir de su codigo de item
        item = self.model.extraer_objetos_alojados(self.directorio_item,codigo_item)
        '''la verificacion correspondiente si se ha ingresado la nueva descipcion del item en 
        cuestion'''
        if not descripcion:
            return 1,'NO SE INGRESSO NINGUNA DESCRIPCION'
        #se actualiza la descipcion correspondiente del item
        item.set_descripcion(descripcion)
        '''Por ultimo tenemos la actualizacion correspondiente de items del negocio'''
        self.model.objeto_guardar(self.directorio_item, item, item.get_codigo_item())
        self.__items = self.model.objeto_lista(self.directorio_item)
        return 0,('Descripcion: '+ item.get_descripcion()+ ' Precio: '+str(item.get_precio_unitario()))

    def modificar_precio_item(self, codigo_item, precio):
        '''Metodo para actualizar el precio de un item.
        como parametros recibe el codigo del item, y tambien el nuevo precio que tendra
        dicho item en el negocio. El metodo retornara si la oprecion presento un error al cargar
        o si la operacion fue llevada a cabo con exito, con el correspondiente mensaje'''
        #Obtenemos el item en custion de la base de datos con el codigo
        item = self.model.extraer_objetos_alojados(self.directorio_item, codigo_item)
        if not precio:#se verifica si el precio ha sido cargado
            return 1,'PRECIO NO CARGADO'
        try: #Conversion del precio en entero numerico
            precio_item= int(precio)
        except ValueError:
            return 1, 'PRECIO ES INCORRECTO'
        try:#verificacion corrspondiente para asegurar que el numero ingrseado no sea negativo'''
            if precio_item<1:
                raise ValueError
        except ValueError:
            return 1,'PRECIO ES INCORRECTO'
        #se actualiza el precio del item 
        item.set_precio_unitario(precio_item)
        #se actualiza el item correspondiente del negocio
        self.model.objeto_guardar(self.directorio_item, item, item.get_codigo_item())
        #se actualiza la lista de items que posee el negocio
        self.__items = self.model.objeto_lista(self.directorio_item)
        '''Se procede a actualizar la lista de items correspindiente del negocio'''
        return 0,('Descripcion: '+ item.get_descripcion()+' Precio: ' + str(item.get_precio_unitario()))

    def registrar_item(self, codigo_item, descipcion, precio, tipo):
        '''Metodo encargado de registrar un item en el sistema, que sera invocado en la vista cuando se lo requiera'''
        if not codigo_item:
            #hace la validacion correspondiente en el caso de que no se haya ingresado el codigo lanza adevertencia notificando la misma
            return 1, 'CODIGO DE ITEM NO INGRESADO'
        for item in self.__items:
            #hace la verificacion correspondiente y busca si el item ya esta registrado en la base de datos
            if item.get_codigo_item() == codigo_item:
                return 1, 'Item ya se encuentra en la base de datos'
        tipo_de_item= {1: Articulo, 2: Servicios}
        if not descipcion:
            #verifica si se ingreso la descripcion del item
            return 1, 'No se ingreso descripcion del item'
        try:
            precio_item = int(precio)
            if precio_item<1:
                #validacion correspondiente si se ingreso un precio valido
                raise ValueError
        except ValueError:
            return 1, 'PRECIO NO VALIDO'
        #procede a guardar el item en la base de datos y actualiza la lista de items del negocio
        item = tipo_de_item[tipo](codigo_item, descipcion, precio_item)
        self.model.objeto_guardar(self.directorio_item, item, codigo_item)
        self.__items = self.model.objeto_lista(self.directorio_item)
        return 0, item

    def elimirnar_item(self, codigo_item):
        '''Metodo encargado de eliminar aticulo del negocio, mediante el parametro qie se le paso, 
        em este caso seria con el codigo correspondiente del item'''
        obtejo_mensaje = self.model.objecto_eliminar(self.directorio_item, codigo_item)
        self.model.base_de_datos.close()
        self.__items = self.model.objeto_lista(self.directorio_item)

    def buscar_item(self, codigo_item):
        '''MEtodo encargado de buscar un item del negocio en la base de datos a travez del codigo del mismo, realiza los pasos siguientes a continuacion,
        en cada caso se estará emitiendo mensajes en el cual toma los parametros, si ingreso el codigo, si el item se encentra en la base de datos y o tambien si dicho item
        no se encuentra alojado'''
        if not codigo_item:
            return 1, 'CODIGO ITEM NO INGRESADO'
        try:
            item = self.model.extraer_objetos_alojados(self.directorio_item, codigo_item)
            return 0, ('Descripcion: '+item.get_descripcion()+'\tPrecio: ' + str(item.get_precio_unitario())), item
        except KeyError:
            self.model.base_de_datos.close()
            return 2, 'ITEM NO ALMACENADO EN LA BASE DE DATOS'

    def visualizar_items(self):
        '''Metodo que tiene la finalidad de retornar los items con los que cuentan el negocio,
        retorna si hubo algun error en el proceso para obtener los items con los que cuenta el negocio
        o si se llevo a cabo correctamente el proceso con  la lista correspondiente de items '''
        if not self.__items:
            return 1, 'NO EXISTEN ITEMS ALMACENADOS'
        else:
            return 0, self.__items

    def visualizar_boletas(self, fecha_ingresada):
        '''Metodo encargado de mostrar las boletas generadas por el negocio, mediante el parametro ingresado
        por el usuario del sistema, procede a hacer la logica correspondiente y retorna si se ingreso la fecha
        las boletas generadas en esa fecha o si no se ingreso ninguna fecha retorna todas las boletas generadas
        de las ventas del negocio'''
        if not self.__boletas:
            return 1, 'NO EXISTEN BOLETAS GENERADAS'
        else:
            if fecha_ingresada:#verificacion correspondiente del formato de fecha a ingresar por el usuario
                try:
                    datetime.strptime(fecha_ingresada,"%d/%m/%y")
                except ValueError:
                    return 1, 'FECHA NO ES VALIDA'
            boletas = []
            bandera = 0
            if fecha_ingresada:#una vez ingresada la fecha, procede a buscar las boletas generedas con esa fecha
                for boleta in self.__boletas: 
                    if boleta.get_fecha() == fecha_ingresada: #comparacion correspondiente de la fecha en el cual se genero las boletas
                        boletas.append(boleta)
                        bandera = 1
            else:#en el caso de que no se haya ingresado una fecha, procede a mostrar todas las boletas generadas por las ventas del negocio
                boletas = self.__boletas
                bandera = 1

            if bandera == 0:
                return 1, 'NO EXISTEN BOLETAS GENERADAS CON ESA FECHA' 
            else:
                return 0, boletas

    def visualizar_clientes(self):
        '''Metodo encargado de mostrar al usuario la lista correspondiente de clientes con los que cuenta el negocio 
        retorna 1: si hubo algun error durante el proceso,
        retorna 0: si se llevo a cabor correctamente el proceso con la lista de clientes del negocio'''
        if not self.__clientes:#verificacion correspondiente si es que se encuentra almacenado clientes en la base de datos
            return 1, 'NO EXISTEN CLIENTES ALMACENADOS'
        else:
            return 0, self.__clientes

    def modificacion_nombre_cliente(self, ruc_cliente, nombre_cliente):

        '''Metodo encargado de modificar el nombre de un cliente en especifico, recibe del usuario
        el ruc del cliente del cual se quiera modificar, hace la verficicacion correspodiente si se
        encuentra almacenado en la base de datos del negocio, si esta se halla en la base de datos
        el usuario carga el nuevo nombre y realiza la logica correspodiente mas abajo'''
        cliente = self.model.extraer_objetos_alojados(self.directorio_cliente, ruc_cliente)#obtenemos el cliente mediante el ruc ingrsado
        if not nombre_cliente:#verificacion correspondiente si es que existen clientes en la base de datos
            return 1, 'NO SE INGRESO NOMBRE DEL CLIENTE'
        #procede a modificar el nombre del cliente
        cliente.cambiar_nombre_cliente(nombre_cliente)
        self.model.objeto_guardar(self.directorio_cliente, cliente, cliente.get_ruc())#se actualiza los datos de ese clientes
        self.__clientes = self.model.objeto_lista(self.directorio_cliente) #se actualiza la lista de clientes del negocio
        return 0, ('Nombre: '+ cliente.get_nombre()+' Apellido: '+ cliente.get_apellido())

    def modificacion_apellido_cliente(self, ruc_cliente, apellido_cliente):
        '''Metodo encargado de modificar el apellido de un cliente en especifico, recibe del usuario
        el ruc del cliente del cual se quiera modificar, hace la verficicacion correspodiente si se
        encuentra almacenado en la base de datos del negocio, si esta se halla en la base de datos
        el usuario carga el nuevo nombre y realiza la logica correspodiente mas abajo'''
        cliente = self.model.extraer_objetos_alojados(self.directorio_cliente, ruc_cliente)#obtenemos el cliente mediante el ruc ingrsado
        if not apellido_cliente:#verificacion correspondiente si es que existen clientes en la base de datos
            return 1, 'NO SE INGRESO APELLIDO DEL CLIENTE'
        
        #procede a modificar el nombre del cliente
        cliente.cambiar_apellido_cliente(apellido_cliente)
        self.model.objeto_guardar(self.directorio_cliente, cliente, cliente.get_ruc())#se actualiza los datos de ese clientes
        self.__clientes = self.model.objeto_lista(self.directorio_cliente) #se actualiza la lista de clientes del negocio
        return 0, ('Nombre: '+ cliente.get_nombre()+' Apellido: '+ cliente.get_apellido())

    def buscar_clientes(self, ruc_cliente):
        '''Metodo que tiene la funcionalidad de buscar el cliente en la base de datos de clientes del negocio mediante
        el Ruc ingresado por el usuario al sistema'''
        if not ruc_cliente:
            return 1, 'NO SE INGRESO RUC DEL CLIENTE'
        try: #verifica si el cliente se encuentre guardado
            cliente = self.model.extraer_objetos_alojados(self.directorio_cliente, ruc_cliente)
            return 0, ('Nombre: ' + cliente.get_nombre() + '\nApellido: ' + cliente.get_apellido()), cliente
        except KeyError:
            self.model.base_de_datos.close()
            return 2,'CLIENTE NO ALMACENADO'





  





