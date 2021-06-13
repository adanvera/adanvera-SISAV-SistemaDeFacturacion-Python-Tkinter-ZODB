#!/usr/bin/env python3
'''Modulo de model : encargado de la persistencia de los datos en la base de datos
y al mismo tiempo la de obtener datos e informacion de la misma. 
PARADIGMAS DE LA PROGRAMACUION'''


from Persistencia.zobd import MiZODB
import transaction

class Model:
    base_de_datos = ''

    def extraer_objetos_alojados(self,direccion,codigo):
        '''Metodo que recibe un directorio donde se encuentra la base de datos, y la clave del objeto.
        Si la misma lo obtiene, si el obejto esta alojado en la base de datos
        lo retorna'''
        Model.base_de_datos = MiZODB(direccion)
        base_de_datos_root = Model.base_de_datos.raiz
        objetos = base_de_datos_root[codigo]
        Model.base_de_datos.close()
        return objetos

    def objeto_lista(self, direccion):
        '''Metodo que recibe como parametro directorio en donde se encuentra la base de datos.
        Genera una lista a cuyos elementos son todos los objetos que se encuentran alojados en la misma'''
        Model.base_de_datos = MiZODB(direccion)
        base_de_datos_root = Model.base_de_datos.raiz
        objectos = []
        for key in base_de_datos_root.keys():
            objecto = base_de_datos_root[key]
            objectos.append(objecto)
        Model.base_de_datos.close()
        return objectos

    def objecto_eliminar(self, direccion, codigo):
        '''Metodo que elimina un objeto de ka base de datos, el objeto eliminado es aquel que coincide con el codigo cargado como parametro
        .Retorn a un mensaje tipo String'''
        Model.base_de_datos = MiZODB(direccion)
        base_de_datos_root = Model.base_de_datos.raiz
        del base_de_datos_root[codigo]
        transaction.commit()
        Model.base_de_datos.close()
        return 'Eliminacion exitosa de datos'
    
    def objeto_guardar(self, direccion, objetos, codigo):
        '''Metodo que que recibe como parametro un directorio, en el cual se guarda el objeto junto con el codigo/clave de la misma
        . Retorna un mensaje tipo string'''
        Model.base_de_datos = MiZODB(direccion)
        base_de_datos_root = Model.base_de_datos.raiz 
        base_de_datos_root[codigo] = objetos
        transaction.commit()
        Model.base_de_datos.close()
        return 'Datos guardados exitosamente'


if __name__ == '__main__':
    pass