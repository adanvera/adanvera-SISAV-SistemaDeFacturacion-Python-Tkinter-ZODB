#!/usr/bin/env python3
'''Modulo view: Tiene la tarea de mostrar de manera general la vista, es decir, las ventanas,
 mensajes, en ella tambien se envian los datos para el controlador para proceder a realizar la logica del negocio.
PARADIGMAS DE LA PROGRAMACUION'''

from tkinter import*
from tkinter import messagebox

from ZODB.ConflictResolution import state


class View(Frame):
    def __init__(self, controlador, ventana = None):
        '''Se encarga de crear la ventana principal del sistema'''
        Frame.__init__(self,ventana)
        ventana.title('SITEMA DE FACTURACION')
        ventana.geometry('860x570')
        ventana.resizable(0,0)
        #ESTABLECIENDO ICONO DEL SISTEMA
        self.icono = PhotoImage(file='icon.png')
        ventana.tk.call('wm', 'iconphoto', ventana._w, self.icono)
        #ITEMS. Para guardar datos/atributos de la misma
        self.tipo_item = StringVar()
        self.clase_item = StringVar()
        self.codigo = StringVar()
        self.descripcion = StringVar()
        self.precio = StringVar()
        self.cant_item = StringVar()
        self.cantidades_items = []
        self.items_a_vender = []
        self.tipo_item.set('0')
        self.clase_item.set('0')
        #CLIENTES. Para guardar datos/atributos de la misma
        self.ruc = StringVar()
        self.nombre = StringVar()
        self.apellido = StringVar()
        #BOLETAS. Para guardar datos/atributos de la misma
        self.fecha = StringVar()
        self.boleta = StringVar()
        #MAIN VENTAN. Ventana principal del sistema
        self.ventana = ventana
        self.control = controlador
        self.place(relwidth = 1, relheight = 1)
        self.configure(bg='#d3d3d3')
        self.main_menu()

    def  main_menu(self):
        '''Metodo encargado de mostrar el menu principal del sistema'''
        main_title= 'SISTEMA DE FACTURACIÓN \n SISAV'
        self.titulo = Tag(self, text = main_title)
        self.titulo.configure(font=('Lato', '16', 'bold'), bg ='#000')
        self.titulo.place(relx=0.60, rely=0.15, anchor = CENTER)
        #Background. Fondo de la ventana principal del sistema
        self.background= PhotoImage(file='prueba.png')
        self.back = Label(self, image=self.background)
        self.back.place(x=0, y=0)
        #Logotipo de negocio
        self.logotipo = PhotoImage(file='OP.png')
        self.logo = Label(self, image=self.logotipo)
        self.logo.place(x=20,y=20, relx='0.63', rely='0.19', anchor=CENTER)
        #Widgets de la ventana
        self.titulo = Tag(self, text= main_title)
        self.titulo.configure(font=("Lato ", "15","bold"))
        self.titulo.place(relx='0.65', rely='0.35', anchor=CENTER)
        btn_venta = Boton(self, text='REALIZAR VENTA', command = self.realizar_ventas)
        btn_venta.place(relx = 0.66, rely = 0.45, anchor = CENTER)
        btn_item = Boton(self, text='ITEMS', command = self.menu_items)
        btn_item.place(relx = 0.66, rely = 0.51, anchor = CENTER)
        btn_boletas = Boton(self, text='BOLETAS GENERADAS', command = self.menu_boletas)
        btn_boletas.place(relx = 0.66, rely = 0.57, anchor = CENTER)
        btn_clientes = Boton(self, text='  CLIENTES  ', command = self.menu_clientes)
        btn_clientes.place(relx = 0.66, rely = 0.63, anchor = CENTER)

    def realizar_ventas(self):
        #INICALIZAMOS LOS PARAMETROS
        self.codigo.set('')
        self.cant_item.set('')
        self.ruc.set('')
        self.nombre.set('')
        self.apellido.set('')
        #PROCEDEMOS A CREAR LA VENTANA DE VENTAS
        self.ventana_de_ventas = Ventana('900x500')
        self.ventana_de_ventas.title('VENTAS')
        #Titulo dentro de la ventana
        tag_titulo_ventas = Tag(self.ventana_de_ventas, text = 'REALIZAR UNA VENTA')
        tag_titulo_ventas.place(relx=0.39, rely=0.02)
        tag_titulo_ventas.configure(font=("Lato ", "20","bold"))
        #Widgets de la ventana
        tag_ruc = Tag(self.ventana_de_ventas, text = 'RUC')
        tag_ruc.place(relx = 0.06, rely = 0.125)  
        self.cargar_ruc = Entry(self.ventana_de_ventas, textvariable= self.ruc) 
        self.cargar_ruc.place(relx = 0.10, rely = 0.12)   
        self.btn_buscar_cliente = Boton(self.ventana_de_ventas,65, text ='Buscar', command = self.boleta_cliente)
        self.btn_buscar_cliente.place(relx = 0.3, rely=  0.115)
        tag_nombre = Tag(self.ventana_de_ventas, text = 'Nombre')
        tag_nombre.place(relx=0.46, rely = 0.125)
        self.cargar_nombre= Entry(self.ventana_de_ventas,textvariable=self.nombre,  state = DISABLED)
        self.cargar_nombre.place(relx=0.52, rely = 0.12)
        tag_apellido = Tag(self.ventana_de_ventas, text = 'Apellido')
        tag_apellido.place(relx=0.72, rely= 0.125)
        self.cargar_apellido = Entry(self.ventana_de_ventas, textvariable=self.apellido,  state = DISABLED)
        self.cargar_apellido.place(relx = 0.78, rely= 0.12)
        tag_titulo_cargar = Tag(self.ventana_de_ventas, text ='INGRESAR ITEMS A VENDER')
        tag_titulo_cargar.place(relx=0.06, rely=0.20 )
        tag_titulo_cargar.configure(font=("Lato ", "15","bold"))
        tag_codigo = Tag(self.ventana_de_ventas, text = 'Ingresar codigo de item')
        tag_codigo.place(relx=0.06, rely=0.28 )
        self.cargar_codigo = Entry(self.ventana_de_ventas, textvariable=self.codigo)
        self.cargar_codigo.place(relx=0.21, rely = 0.275, width=50)
        tag_cantidad = Tag(self.ventana_de_ventas, text = 'Cantidad')
        tag_cantidad.place(relx= 0.06, rely= 0.35 )
        self.cargar_cantidad = Entry(self.ventana_de_ventas, textvariable=self.cant_item)
        self.cargar_cantidad.place(relx=0.12, rely = 0.345, width=50)
        self.btn_cargar = Boton(self.ventana_de_ventas, text = 'Cargar', command = self.cargar_item_boleta)
        self.btn_cargar.place(relx=0.06, rely=0.50, width= 80)
        self.btn_conf_venta = Boton(self.ventana_de_ventas,text ='Confirmar Venta', state = DISABLED, command = self.guardar_boleta )
        self.btn_conf_venta.place(relx=0.16, rely=0.90, width= 120)
        self.btn_salir = Boton(self.ventana_de_ventas, text = 'Salir', command = self.ventana_de_ventas.destroy)
        self.btn_salir.place(relx=0.30,rely=0.90, width= 60)
        #Lista y scroll correspondientes donde se podran visualizar la boleta generada por la venta hecha
        self.scroll = Scrollbar(self.ventana_de_ventas, orient=VERTICAL)
        self.scroll.place(x=860, y=100, height=380)
        self.ver_boleta = Text(self.ventana_de_ventas, yscrollcommand=self.scroll.set)
        self.ver_boleta.place(x=340, y= 100, width=520, height=380)
        self.scroll.config(command= self.ver_boleta.yview)

    def cargar_item_boleta(self):
        '''Metodo que tiene la finalidad de crear la boleta e ir agregarndo los items a ka misma'''
        message_cantidad = self.control.validar_cantidad_item(self.cant_item.get())
        system_pass = False
        if message_cantidad[0] == 1:
            messagebox.showinfo('ADVERTENCIA', message_cantidad[1], parent = self.ventana_de_ventas)
        else:
            item = self.control.buscar_item(self.codigo.get())
            if item[0] == 1:
                #si se presenta un error, se lanza una advertencia notificando la misma
                messagebox.showinfo('ADVERTENCIA', item[1], parent = self.ventana_de_ventas)
            elif item[0] == 2:
                '''si no encuentra el item en el sistema, procede a invocar a la ventana de registro de item correspondiente
                desde la ventana de ventas'''
                messagebox.showinfo('ADVERTENCIA', item[1], parent = self.ventana_de_ventas)
                self.continue_agregar_mas_items_a_boleta()
            else:
                #si no se presenta ningun error, procede a cargar el item a una lista de items
                self.items_a_vender.append(item[2])
                system_pass = True
        if system_pass:
            #si todo el proceso se hallan correctos, se agrega el item a una lista de items
            self.cantidades_items.append(self.cant_item.get())
            if len(self.items_a_vender) ==1:
                #se procede a crear la boleta com los parametros que se requieren
                message = self.control.generacion_de_boleta(self.items_a_vender, self.cantidades_items, self.nombre.get(), self.apellido.get(), self.ruc.get())
                if message[0] == 1:
                    #si se presenta algun error, notifica la misma
                    messagebox.showinfo('ADVERTENCIA', message[1], parent = self.ventana_de_ventas)
                else:
                    #si no sucede ningun error, procede al guardado temporal de dicha boleta
                    self.boleta = message[1]
            else:
                #si ya se genero la boleta y el cliente quiere mas adquirir mas items, se actualiza la boleta ya existente
                self.boleta = self.control.actualizacion_boleta_items(self.boleta, self.items_a_vender, self.cantidades_items)
            # Validaciones de botones y campos para poder continuar con la venta
            self.btn_conf_venta.config(state = NORMAL)
            self.cargar_nombre.config(state= DISABLED)
            self.cargar_apellido.config(state = DISABLED)
            self.cargar_ruc.config(state= DISABLED)
            self.btn_buscar_cliente.config(state = DISABLED)
            self.cant_item.set('')
            self.codigo.set('')
            #se elimina cualquier dato que haya en ver_boleta y se actualiza lanzando con los nuevos items ingresados
            self.ver_boleta.delete(0.0, END)
            self.imprimir_boleta(self.ver_boleta, self.boleta)
        
    def boleta_cliente(self):
        '''Metodo encargado de hacer la busqueda correspondiente de un cliente a travez de su ruc, cuando 
        la misma este realizando una compra de algun item del negocio'''
        #obtenemos el cliente mediante la invocacion dela funcion buscar cliente, mediante el ruc del cliente
        message = self.control.buscar_clientes(self.ruc.get())
        if message[0] == 1:
            messagebox.showinfo('ADVERTENCIA', message[1] , parent = self.ventana_de_ventas)
        if message[0] == 2:
            messagebox.showinfo('ADVERTENCIA', message[1] , parent =  self.ventana_de_ventas)
            self.cargar_nombre.config(state= NORMAL)
            self.cargar_apellido.config(state= NORMAL)
        else:
            self.nombre.set(message[2].get_nombre())
            self.apellido.set(message[2].get_apellido())
            self.cargar_ruc.config(state= DISABLED)
            self.btn_buscar_cliente.config(state= DISABLED)

    def continue_agregar_mas_items_a_boleta(self):
        '''Metodo encargado de crear la ventana de registro de un item desde la ventana de realizar ventas'''
        #inicializamos los atributos correspondientes para utilizarlos en el registro
        self.tipo_item.set('')
        self.descripcion.set('')
        self.precio.set('')
        #se crea la ventana
        self.ventana_nuevo_item = Ventana()
        self.ventana_nuevo_item.geometry('500x200')
        self.ventana_nuevo_item.title('CARGAR NUEVO ITEM')
        tag_titulo_registro = Tag(self.ventana_nuevo_item, text = 'REGISTRO DE ITEM')
        tag_titulo_registro.configure(font=("Lato ", "15","bold"))
        tag_titulo_registro.place(x=150, y=10)   
        #widgets de la ventana 
        tag_code = Tag(self.ventana_nuevo_item, text = 'Codigo: ')
        tag_code.place(x= 55, y= 52)
        cargar_code = Entry(self.ventana_nuevo_item, textvariable=self.codigo, width=5)
        cargar_code.place(x= 120, y= 50)
        tag_item = Tag(self.ventana_nuevo_item, text = 'Tipo de Item: ')
        tag_item.place(x =250, y=52)
        item_articulo = BotonRedondo(self.ventana_nuevo_item, text = 'Articulo', value = '1', variable = self.tipo_item)
        item_articulo.place(x=350, y=38)
        item_servicios = BotonRedondo(self.ventana_nuevo_item, text = 'Servicio', value = '2', variable = self.tipo_item)
        item_servicios.place(x=350, y=55)
        tag_descripcion = Tag(self.ventana_nuevo_item, text = 'Descripcion: ')
        tag_descripcion.place(x=55, y= 92)
        cargar_descripcion = Entry(self.ventana_nuevo_item, textvariable=self.descripcion, width=25)
        cargar_descripcion.place(x= 130, y = 90)
        tag_precio= Tag(self.ventana_nuevo_item, text = 'Precio: ')
        tag_precio.place(x= 55, y= 120)
        cargar_precio = Entry(self.ventana_nuevo_item, textvariable=self.precio)
        cargar_precio.place(x=100,y=118) 
        btn_guradar = Boton(self.ventana_nuevo_item,70, text = 'Guardar', command = self.guradar_item_boleta)
        btn_guradar.place(x= 180, y= 155)

    def guradar_item_boleta(self):
        '''Metodo encargado de agregar un nuevo item ingresado en la ventana de ventas'''
        message = self.control.registrar_item(self.codigo.get(), self.descripcion.get(), self.precio.get(),int(self.tipo_item.get()))
        if message[0] == 1:
            #procede a notificar un error si ocurre la misma
            messagebox.showinfo('ADVERTENCIA', message[1], parent = self.ventana_item_desde_boleta)
        else:
            #si no ocurre ningun error, cierra la ventana de registro y continua con el proceso a realizar
            self.ventana_nuevo_item.destroy()
            self.cargar_item_boleta()

    def imprimir_boleta(self, text_a_salir, boleta):
        '''Metodo que tiene la funcion de mostrar todos los datos de una boleta'''
        text_a_salir.insert(INSERT, '\t\tAV SERVICIOS DIGITALES E IMPRENTA\n\n')
        text_a_salir.insert(INSERT, '\tNUMERO DE BOLETA: ')
        text_a_salir.insert(INSERT,'\t' +str(boleta.get_num_de_boleta())+'\t')
        text_a_salir.insert(INSERT,'\t\tFecha. '+ boleta.get_fecha()+'\n')
        text_a_salir.insert(INSERT, '\n'+ boleta.get_cliente().__str__())
        text_a_salir.insert(INSERT, '\n_______________________________________________________________\n')
        text_a_salir.insert(INSERT,'CANT\tDESCRIPCION\t\t     PRECIO UNITARIO\t\t  VALOR DE VENTA\n')
        items = boleta.get_items()
        subtotales = boleta.caluclo_de_subtotales()
        item_numero = 0
        for item in items:
            text_a_salir.insert(INSERT, str(len(item))+ '\t'+ item[0].vender()+ '         ' + str(subtotales[item_numero])+'\n')
            item_numero += 1
        text_a_salir.insert(INSERT, '\nTotal a pagar: '+ str(boleta.calculo_de_total(subtotales)))
        text_a_salir.insert(INSERT,'\n\n')
        text_a_salir.insert(INSERT,'\n================================================================\n\n')

    def menu_items(self):
        '''Metodo encargado de  mostrar la ventana de menu de items'''
        #se crea la ventana correspondiente a la misma
        self.ventana_items = Ventana()
        self.ventana_items.geometry('800x500')
        self.ventana_items.title('MENU DE ITEMS')
        #widgets de la ventana
        tag_titulo_items = Tag(self.ventana_items, text = 'ITEMS')
        tag_titulo_items.place(relx=0.49, rely=0.10, anchor=CENTER)
        tag_titulo_items.configure(font=("Lato ", "15","bold"))
        btn_registrar_item= Boton(self.ventana_items, text = 'Registar Item', command = self.cargar_item)
        btn_registrar_item.place(relx = 0.02,rely= 0.27, width= 100)
        btn_visualizar_items = Boton(self.ventana_items, text = 'Lista de items', command = self.visualizacion_items)
        btn_visualizar_items.place(relx = 0.02, rely = 0.35, width= 100 )
        btn_modificar_item = Boton(self.ventana_items, text ='Modificar Item', command = self.modificacion_item)
        btn_modificar_item.place(relx = 0.02, rely = 0.43, width= 100)
        btn_eliminar_item = Boton(self.ventana_items, text = 'Elimiar item', command = self.eliminacion_item)
        btn_eliminar_item.place(relx =0.02, rely= 0.51, width= 100)
        btn_salir = Boton(self.ventana_items, text = 'Salir', command = self.ventana_items.destroy)
        btn_salir.place(relx=0.22,rely=0.91, width= 60)
        #Lista y scroll donde estaran los datos del cliente
        self.scroll = Scrollbar(self.ventana_items, orient=VERTICAL)
        self.scroll.place(x=770, y=135, height=350)
        self.lista_de_items = Text(self.ventana_items, yscrollcommand=self.scroll.set)
        self.lista_de_items.place(x=250, y= 135, width=520, height=350)
        self.scroll.config(command = self.lista_de_items.yview)

    def cargar_item(self):
        '''Metodo que se encarga generar la ventana correspondiente para registar un nuevo item'''
        #procede a vaciar la lista de items e inicializan los campos correspondientes en el caso de que tengan alojados datos en ella
        self.lista_de_items.config(state = NORMAL)
        self.lista_de_items.delete(0.0, END)
        self.lista_de_items.config(state = DISABLED)
        self.codigo.set('')
        self.tipo_item.set('0')
        self.descripcion.set('')
        self.precio.set('')
        #se crea la ventana
        self.ventana_cargar_item = Ventana()
        self.ventana_cargar_item.geometry('500x200')
        self.ventana_cargar_item.title('CARGAR NUEVO ITEM')
        tag_titulo_registro = Tag(self.ventana_cargar_item, text = 'REGISTRO DE ITEM')
        tag_titulo_registro.configure(font=("Lato ", "15","bold"))
        tag_titulo_registro.place(x=150, y=10)
        #widgets correspondientes de la ventana
        tag_code = Tag(self.ventana_cargar_item, text = 'Codigo: ')
        tag_code.place(x= 55, y= 52)
        cargar_code = Entry(self.ventana_cargar_item, textvariable=self.codigo, width=5)
        cargar_code.place(x= 120, y= 50)
        tag_item = Tag(self.ventana_cargar_item, text = 'Tipo de Item: ')
        tag_item.place(x =250, y=52)
        item_articulo = BotonRedondo(self.ventana_cargar_item, text = 'Articulo', value = '1', variable = self.tipo_item)
        item_articulo.place(x=350, y=38)
        item_servicios = BotonRedondo(self.ventana_cargar_item, text = 'Servicio', value = '2', variable = self.tipo_item)
        item_servicios.place(x=350, y=55)
        tag_descripcion = Tag(self.ventana_cargar_item, text = 'Descripcion: ')
        tag_descripcion.place(x=55, y= 92)
        cargar_descripcion = Entry(self.ventana_cargar_item, textvariable=self.descripcion, width=25)
        cargar_descripcion.place(x= 130, y = 90)
        tag_precio= Tag(self.ventana_cargar_item, text = 'Precio: ')
        tag_precio.place(x= 55, y= 120)
        cargar_precio = Entry(self.ventana_cargar_item, textvariable=self.precio)
        cargar_precio.place(x=100,y=118) 
        btn_guradar = Boton(self.ventana_cargar_item,70, text = 'Guardar', command = self.guradar_item )
        btn_guradar.place(x= 180, y= 155)
        btn_salir = Boton(self.ventana_cargar_item,70, text = 'Salir', command = self.ventana_cargar_item.destroy )
        btn_salir.place(x= 270, y= 155)

    def visualizacion_items(self):
        '''Metodo encargado de mostrar en la ventana la lista correspondiente de items que posee el negocio'''
        self.lista_de_items.config(state=NORMAL)
        self.lista_de_items.delete(0.0, END)
        items = self.control.visualizar_items()
        if items[0] == 1:
            #Notificacion correspondiente que lanzara si ocurre algun error en el proceso
            messagebox.showinfo('ADVERTENCIA',items[1], parent= self.ventana_items)
        else:
            #imprime la cebecera de la lista
            titulo_de_lista = '{0:>40}'.format('LISTA DE ITEMS\n')
            self.lista_de_items.insert(INSERT, titulo_de_lista)
            head_lista = ('\nCodigo\t\tDescripcion\t\t\tPrecio Unitario\n-------------------------------------------------------------\n')
            self.lista_de_items.insert(INSERT, head_lista)
            #procede a imprimir la lista de items con los que cuenta el negocio
            for item in items[1]:
                self.lista_de_items.insert(INSERT, item.__str__()+'\n')
        self.lista_de_items.config(state=DISABLED)

    def modificacion_item(self):
        '''Metodo que tiene la finalidad la de crear la ventana de modificar los atributos de un item'''
        #Procede a vaciar completamente la lista, y se inicializa los campos a utilizar en cuestion
        self.lista_de_items.config(state = NORMAL)
        self.lista_de_items.delete(0.0, END)
        self.lista_de_items.config(state = DISABLED)
        self.codigo.set('')
        #Procede a crear la ventana para modificiar el item en cuestion
        self.ventana_modificar_item = Ventana()
        self.ventana_modificar_item.geometry('500x250')
        self.ventana_modificar_item.title('MODIFICAR ITEM')
        #widgets de la ventana 
        self.tag_code_editar = Tag(self.ventana_modificar_item, text = 'Codigo: ')
        self.tag_code_editar.place(x= 55, y= 52)
        self.cargar_code_editar = Entry(self.ventana_modificar_item, textvariable=self.codigo, width=5)
        self.cargar_code_editar.place(x= 120, y= 50, width=60)
        self.btn_buscar_editar= Boton(self.ventana_modificar_item,70, text = 'Buscar', command = self.buscat_item_editar)
        self.btn_buscar_editar.place(x=200, y= 47)
        self.btn_otro_busc_editar = Boton(self.ventana_modificar_item, 90, text = 'Buscar Otro', command = self.buscar_otro)
        self.btn_otro_busc_editar.place(x= 55, y=115 )
        self.info_item = Tag(self.ventana_modificar_item)
        self.info_item.place(x=55, y= 92)
        self.btn_mod_descripcion = Boton(self.ventana_modificar_item, text = 'Modificar Descripcion',state = DISABLED, command = self.mod_desc_ventana)
        self.btn_mod_descripcion.place(x=55, y=180, width= 140)
        self.btn_mod_price = Boton(self.ventana_modificar_item, text = 'Modificar Precio', state = DISABLED,command = self.mod_price_ventana)
        self.btn_mod_price.place(x=200, y=180, width= 120)
        self.btn_salir = Boton(self.ventana_modificar_item, text = 'Salir', command = self.ventana_modificar_item.destroy)
        self.btn_salir.place(x=400, y=180, width= 60)

    def mod_desc_ventana(self):
        '''Metodo que tiene la finalidad de crear la ventan correspondiente para poder modificar la descripcion de un item'''
        #se inicializa los atributos en cuestion y se procede a crear la ventana
        self.descripcion.set('')
        self.ventana_desc_item = Ventana('200x100')
        self.ventana_desc_item.title('MODIFICAR')
        #widgets que se requiere en la ventana
        tag_descripcion = Tag(self.ventana_desc_item, text ='Nueva descripcion')
        tag_descripcion.place(relx=0.20, rely=0.10)
        self.cargar_nueva_desc = Entry(self.ventana_desc_item, textvariable=self.descripcion)
        self.cargar_nueva_desc.place(relx= 0.06, rely= 0.28)
        boton_guardar = Boton(self.ventana_desc_item, 100, text='Guardar', command = self.mod_item_desc)
        boton_guardar.place(relx=0.08, rely=0.55, width=80)
        self.btn_salir = Boton(self.ventana_desc_item, text = 'Salir', command = self.ventana_desc_item.destroy)
        self.btn_salir.place(relx=0.50, rely=0.55, width=80)

    def mod_item_desc(self):
        '''Metodo encargado de modificar las descripciones corresponditens de cada item con los
        que cuenta el negocio'''
        message = self.control.modificar_descripcion_item(self.codigo.get(), self.descripcion.get())
        if message[0] == 1:
            #si se presenta algun error, lanza advertencia 
            messagebox.showinfo('ADVERTENCIA', message[1], parent = self.ventana_desc_item)
        else:
            #si no se presenta ningun error, procede a mostar la el item con la descripcion actualizada
            self.info_item.config(text = message[1])
            self.descripcion.set('')
            self.ventana_desc_item.destroy()

    def mod_price_ventana(self):
        '''Metodo encargado de crear la ventana de modificacion del precio de un item'''
        self.precio.set('')
        self.ventana_price_item = Ventana('200x100')
        self.ventana_price_item.title('MODIFICAR')
        #widgets correspondientes de la ventana
        tag_price = Tag(self.ventana_price_item, text ='Nuevo precio')
        tag_price.place(relx= 0.20, rely=0.10)
        self.cargar_precio = Entry(self.ventana_price_item, textvariable=self.precio)
        self.cargar_precio.place(relx= 0.06, rely=0.28)
        self.btn_guardar = Boton(self.ventana_price_item, 100,text = 'Guardar', command = self.mod_price_item)
        self.btn_guardar.place(relx=0.08,rely=0.55, width=80)
        self.btn_salir = Boton(self.ventana_price_item, text= 'Salir', command = self.ventana_price_item.destroy)
        self.btn_salir.place(relx = 0.50, rely=0.55, width=80)

    def mod_price_item(self):
        '''Metodo encargado de realizar el cambio de precio de un item'''
        message = self.control.modificar_precio_item(self.codigo.get(),self.precio.get())
        if message[0] ==1:
            #lanza una advertencia si se presenta un error notificando la misma
            messagebox.showinfo('ADVERTENCIA', message[1], parent = self.ventana_price_item)
        else:
            #si no se presenta ningun eror, procede a mostrar el item actualizado
            self.info_item.config(text = message[1])
            self.precio.set('')
            self.ventana_price_item.destroy()
            
    def buscat_item_editar(self):
        '''Metodo encargado de realizar la busqueda de un item mediante su codigo '''
        message = self.control.buscar_item(self.codigo.get())
        if message[0] == 1 or message[0] == 2:
            #si se presenta un error, lanza la advertencia
            messagebox.showinfo('ADVERTENCIA', parent = self.ventana_modificar_item)
            #procede a inicializaar nuevamente los campos para poder ingresar otra busqueda
            self.codigo.set('')
            self.info_item.config(text = '')
            self.btn_mod_descripcion.config(state = DISABLED)
            self.btn_mod_price.config(state = DISABLED)
        else:
            #en el caso de que no se presente ningun error, procede a mostrar los atributos de un item y las acciones sobre la misma
            self.info_item.config(text = message[1])
            self.tag_code_editar.config(state = DISABLED)
            self.btn_buscar_editar.config(state = DISABLED)
            self.btn_otro_busc_editar.config(state= NORMAL)
            self.btn_mod_descripcion.config(state= NORMAL)
            self.btn_mod_price.config(state= NORMAL)

    def buscar_otro(self):
        '''Metodo encargado de inicializar nuevamentes los campos para poder hacer otra busqueeeda si se desea en la ventana de modificar item'''
        self.tag_code_editar.config(state= NORMAL)
        self.codigo.set('')
        self.btn_buscar_editar.config(state= NORMAL)
        self.btn_mod_descripcion.config(state= DISABLED)
        self.btn_mod_price.config(state = DISABLED)
        self.btn_otro_busc_editar.config(state= DISABLED)
        self.info_item.config(text ='')

    def eliminacion_item(self):
        '''Metodo encargado de crear la ventana para la eliminacion de un item'''
        self.lista_de_items.config(state = NORMAL)
        self.lista_de_items.delete(0.0, END)
        self.lista_de_items.config(state = DISABLED )
        #se crea la ventana
        self.ventana_eliminacion_item = Ventana('500x200')
        self.ventana_eliminacion_item.title('ELIMINACION DE ITEMS')
        #widgets de la ventana
        tag_code = Tag(self.ventana_eliminacion_item, text = 'Codigo: ')
        tag_code.place(x= 55, y= 52)
        self.cargar_code = Entry(self.ventana_eliminacion_item, textvariable=self.codigo, width=5)
        self.cargar_code.place(x= 120, y= 50, width=60)
        self.btn_buscar_eliminar= Boton(self.ventana_eliminacion_item,70, text = 'Buscar', command = self.buscar_eliminar_item)
        self.btn_buscar_eliminar.place(x=200, y= 47)
        self.btn_otro_busc_eliminar = Boton(self.ventana_eliminacion_item, 90, text = 'Buscar Otro', command = self.buscar_eliminar_otro)
        self.btn_otro_busc_eliminar.place(x= 55, y=100 )
        self.info_item = Tag(self.ventana_eliminacion_item)
        self.info_item.place(x = 55, y=85, width= 420)
        self.btn_eliminar_item= Boton(self.ventana_eliminacion_item, text = 'ELiminar', command = self.eliminar_un_item)
        self.btn_eliminar_item.place(x = 350, y =140, width=65 )
        self.btn_salir= Boton(self.ventana_eliminacion_item, text = 'Salir', command = self.ventana_eliminacion_item.destroy)
        self.btn_salir.place(x = 420, y =140, width=65 )

    def buscar_eliminar_item(self):
        '''Metodo que tiene como finalidad la de buscar el item mediante su codigo, para despues poder eliminarlo'''
        message = self.control.buscar_item(self.codigo.get())
        if message[0]== 1 or message[0] == 2:
            #procede a notificar si se presenta un error en el proceso que se lleve a cabo
            messagebox.showinfo('ADVERTENCIA',message[1] ,parent =self.ventana_eliminacion_item )
            #al mismo tiempo inicializa nuevamente para poder hacer otra busqueda
            self.codigo.set('')
            self.btn_eliminar_item.config(state= DISABLED)
        else:
            #en el caso de que no se de ningun error, procede a mostrar los detalles del item y habilita la opcion de eliminacion
            self.info_item.config(text= message[1])
            self.btn_otro_busc_eliminar.config(state= NORMAL)
            self.cargar_code.config(state= DISABLED)
            self.btn_buscar_eliminar.config(state= DISABLED)
            self.btn_eliminar_item.config(state= NORMAL)

    def buscar_eliminar_otro(self):
        '''Metodo encargado de reiniciar los campos correspondientes para poder hacer una nueva busqueda para eliminar un item en
        concreto'''
        self.cargar_code.config(state= NORMAL)
        self.codigo.set('')
        self.info_item.config(text='')
        self.btn_eliminar_item.config(state= DISABLED)
        self.btn_buscar_eliminar.config(state= NORMAL)
        self.btn_otro_busc_eliminar.config(state= NORMAL)

    def eliminar_un_item(self):
        '''Metodo encargado de eliminar un item tomando como parametro su codigo al controlador para realizar dicho procedimiento'''
        self.control.elimirnar_item(self.codigo.get())
        self.codigo.set('')
        self.info_item.config(text='')
        self.btn_buscar_eliminar.config(state= NORMAL)
        self.cargar_code.config(state= NORMAL)
        self.btn_otro_busc_eliminar.config(state= DISABLED)
        self.btn_eliminar_item.config(state= DISABLED)

    def guradar_item(self):
        '''Metodo que tiene la funcion de pasar los parametros al controlador para poder guardar los detalles de un item que se va a registrar'''
        message = self.control.registrar_item(self.codigo.get(), self.descripcion.get(), self.precio.get(), int(self.tipo_item.get()))
        if message[0]== 1:
            #Lanza el mensaje correspondiente del sistema para notificar el resultado obtenido de dicho proceso
            messagebox.showinfo('ADVERTENCIA', message[1], parent = self.ventana_cargar_item)
        else:
            #Limpia los campos del item para poder agregar un nuevo item al sistema
            self.codigo.set('')
            self.descripcion.set('')
            self.precio.set('')
            self.tipo_item.set('0')

    def menu_boletas(self):
        '''Metodo correspondiente a la ventana de menu de las boletas'''
        self.fecha.set('')
        #se crea la ventana
        self.ventana_de_boletas = Ventana('800x450')
        self.ventana_de_boletas.title('MENU DE BOLETAS')
        #widgets correspondientes de la ventana
        titulo_boleta = Tag(self.ventana_de_boletas, text = 'Buscar boleta por fecha')
        titulo_boleta.place(relx=0.12, rely=0.11, anchor=CENTER)
        titulo_boleta.configure(font=("Lato ", "11","bold"))
        tag_fecha = Tag(self.ventana_de_boletas, text = 'Ingresar fecha de la boleta (dd/mm/yy): ')
        tag_fecha.place(relx=0.025, rely=0.15)
        self.cargar_fecha = Entry(self.ventana_de_boletas, text = 'Buscar', textvariable= self.fecha)
        self.cargar_fecha.place(relx= 0.025, rely=0.20, width= 100)
        btn_buscar_boleta = Boton(self.ventana_de_boletas, text = 'Buscar' ,command = self.mostar_boletas )
        btn_buscar_boleta.place(relx=0.18, rely=0.19, width=80)
        btn_salir = Boton(self.ventana_de_boletas, text = 'Salir', command = self.ventana_de_boletas.destroy)
        btn_salir.place(relx= 0.21, rely=0.84, width= 80)
        self.scroll = Scrollbar(self.ventana_de_boletas, orient=VERTICAL)
        self.scroll.place(x=770, y=60, height=350)
        #Lista y scroll correspondientes a boletas donde se podran ver los datos que se encuntran en el sistema
        self.lista_de_boletas = Text(self.ventana_de_boletas, yscrollcommand=self.scroll.set)
        self.lista_de_boletas.place(x=250, y= 60, width=520, height=350)
        self.scroll.config(command = self.lista_de_boletas.yview)

    def mostar_boletas(self):
        '''Metodo encargado de mostrar la lista de todas las boletas generadas por el sistema'''
        self.lista_de_boletas.config(state = NORMAL)
        self.lista_de_boletas.delete(0.0, END)
        boletas = self.control.visualizar_boletas(self.fecha.get())
        if boletas[0] == 1:
            #si se presenta algun error, lanza la advertencia
            messagebox.showinfo('ADVERTENCIA', boletas[1],parent = self.ventana_de_boletas)
        else:
            #en el caso de que no se presente ningun error, procede a imprimir la cabecera de la boleta
            #y al mismo tiempo imprime la lista de boletas que hayan
            title = '{0:>43}'.format('BOLETAS GENERADAS\n\n')
            self.lista_de_boletas.insert(INSERT, title)
            for boleta in boletas[1]:
                self.imprimir_boleta(self.lista_de_boletas, boleta)
        self.lista_de_boletas.config(state= DISABLED)

    def menu_clientes(self):
        '''Metodo que tiene la finalidad de mostrar la ventana que tiene potestad sobre los clientes, y 
        las acciones correspondientes que se pueden llevar a cabo en ella'''
        #Se crea la correspondiente ventana menu de clientes
        self.ventana_clientes = Ventana()
        self.ventana_clientes.geometry('800x500')
        self.ventana_clientes.title('MENU DE CLIENTES')
        #widgets de la ventana
        tag_titulo_clientes = Tag(self.ventana_clientes, text = 'CLIENTES')
        tag_titulo_clientes.place(relx=0.495, rely=0.11, anchor=CENTER)
        tag_titulo_clientes.configure(font=("Lato ", "15","bold"))
        btn_editar_cliente = Boton(self.ventana_clientes, text = 'Modificar Cliente', command = self.modificar_cliente)
        btn_editar_cliente.place(relx = 0.02,rely= 0.27)
        btn_visualizar_clientes = Boton(self.ventana_clientes, text = 'Lista de Clientes', command = self.mostrar_clientes)
        btn_visualizar_clientes.place(relx = 0.02, rely = 0.35 )
        btn_salir = Boton(self.ventana_clientes, text = 'Salir', command = self.ventana_clientes.destroy)
        btn_salir.place(relx=0.22,rely=0.91, width=60)
        #Lista y scroll donde estaran los datos del cliente
        self.scroll = Scrollbar(self.ventana_clientes, orient=VERTICAL)
        self.scroll.place(x=770, y=135, height=350)
        self.lista_de_cliente = Text(self.ventana_clientes, yscrollcommand=self.scroll.set)
        self.lista_de_cliente.place(x=250, y= 135, width=520, height=350)
        self.scroll.config(command= self.lista_de_cliente.yview)

    def mostrar_clientes(self):
        '''Metodo encargado de mostrar la lista de clientes con los que cuenta el negocio'''
        self.lista_de_cliente.config(state = NORMAL)
        self.lista_de_cliente.delete(0.0, END)
        clientes = self.control.visualizar_clientes()
        if clientes[0] == 1:
            #si se presenta algun error salta la siguiente advertencia
            messagebox.showinfo('ADVERTENCIA', clientes[1], parent = self.ventana_clientes)
        else:
            '''si no ocurre ningun error, procede a imprimir la cabecera y la consiguiente lista
            de cliente que se encuentran en ka vase de datos'''
            title = '{0:^65}'.format('Lista de clientes\n')
            self.lista_de_cliente.insert(INSERT, title)
            head = ('\nRUC\t\tNombre\t\t\tApellido\n\n')
            self.lista_de_cliente.insert(INSERT, head)
            for cliente in clientes[1]:
                client = (cliente.get_ruc() + '\t\t'+ cliente.get_nombre()+'\t\t\t'+ cliente.get_apellido()+'\n')
                self.lista_de_cliente.insert(INSERT, client)
        self.lista_de_cliente.config(state = DISABLED)

    def modificar_cliente(self):
        '''Metodo que tiene la finalidad de crear la ventana para poder modificar los datos de un cliente'''
        self.lista_de_cliente.config(state = NORMAL)
        self.lista_de_cliente.delete(0.0, END)
        self.lista_de_cliente.config(state = DISABLED)
        self.ruc.set('')
        #se procede a la creacion correspondiente de la ventana
        self.ventana_cliente_modificar = Ventana()
        self.ventana_cliente_modificar.geometry('600x300')
        self.ventana_cliente_modificar.title('MODIFICAR CLIENTE')
        #widgets respectivos de la ventana
        tag_ruc = Tag(self.ventana_cliente_modificar, text = 'RUC')
        tag_ruc.place(relx = 0.10, rely= 0.1)  
        self.cargar_ruc = Entry(self.ventana_cliente_modificar, textvariable= self.ruc) 
        self.cargar_ruc.place(relx = 0.22, rely = 0.1)   
        self.btn_buscar_cliente = Boton(self.ventana_cliente_modificar, text = 'Buscar', command = self.buscar_clientes)
        self.btn_buscar_cliente.place(relx = 0.75, rely= 0.12, anchor= CENTER, width= 130)
        self.btn_otra_busqueda = Boton(self.ventana_cliente_modificar, text = 'Buscar otra', state = DISABLED, command = self.otra_busqueda_cliente)
        self.btn_otra_busqueda.place(relx= 0.10, rely= 0.4, anchor= W, width=130)
        self.info_cliente = Tag(self.ventana_cliente_modificar)
        self.info_cliente.place(relx= 0.02, rely=0.25, width=250)
        self.btn_cambiar_nombre = Boton(self.ventana_cliente_modificar,text ='MODIFICAR NOMBRE', state = DISABLED, command = self.ventana_nombre)
        self.btn_cambiar_nombre.place(relx= 0.10, rely=0.57)

        self.btn_cambiar_apellido = Boton(self.ventana_cliente_modificar,text ='MODIFICAR APELLIDO', state = DISABLED, command = self.ventana_apellido)
        self.btn_cambiar_apellido.place(relx= 0.10, rely=0.68)


        btn_salir = Boton(self.ventana_cliente_modificar, text ='Salir' ,command= self.ventana_cliente_modificar.destroy)
        btn_salir.place(relx=0.75, rely=0.78, width=70)

    def buscar_clientes(self):
        '''Metodo encargado de buscar un cliente mediante su ruc'''
        #invocamos a la funcion de busqueda mediante el controlador para buscar al cliente
        message = self.control.buscar_clientes(self.ruc.get())
        if message[0] == 1 or message[0] == 2:
            #Si ocurre algun error se lanza la notificacion correspondiente en pantalla
            messagebox.showinfo('ADVERTENCIA', message[1], parent =self.ventana_cliente_modificar)
            #se inicializa los campos nuevamente para poder hacer otra busqueda si asi se desea
            self.ruc.set('')
            self.info_cliente.config( text='')
            self.btn_cambiar_nombre.config(state = DISABLED)
            self.btn_cambiar_apellido.config(state = DISABLED)
        else:
            #en el caso de que se encuentre al cliente en cuestion se habilitan los campos correspondiente para poder hacer las modificaciones correspondientes
            self.info_cliente.config(text = message[1])
            self.cargar_ruc.config(state = DISABLED)
            self.btn_buscar_cliente.config(state = DISABLED)
            self.btn_otra_busqueda.config(state = NORMAL)
            self.btn_cambiar_nombre.config(state = NORMAL)
            self.btn_cambiar_apellido.config(state = NORMAL)

    def guardar_boleta(self):
        '''Metodo encargado de guardar la boleta generada. 
        por medio de el controlador, y tambien cumple con la funcion la de inicalizar los campos
        para poder generar otras boletas para las siguientes ventas'''
        self.control.vender(self.boleta, self.boleta.get_cliente())
        self.ver_boleta.delete(0.0,END)
        self.boleta = ''
        self.items_a_vender = []
        self.cantidades_items = []
        self.cargar_ruc.config(state=NORMAL)
        self.codigo.set('')
        self.ruc.set('')
        self.nombre.set('')
        self.apellido.set('')
        self.btn_buscar_cliente.config(state= NORMAL)
        self.btn_conf_venta.config(state = DISABLED)

    def otra_busqueda_cliente(self):
        '''Metodo encargado de reestablecer los campos, si se da el caso de que se quiera buscar
        otro cliente de la ventana de modificar items'''
        self.ruc.set('')
        self.info_cliente.config(text ='')
        self.cargar_ruc.config(state = NORMAL)
        self.btn_buscar_cliente.config(state = NORMAL)
        self.btn_otra_busqueda.config(state = DISABLED)
        self.btn_cambiar_nombre.config(state = DISABLED)
        self.btn_cambiar_apellido.config(state = DISABLED)

    def ventana_nombre(self):
        '''Metodo correspondiente a la ventana de modificacion del nombre de un cliente'''
        #inicialzamos los parametros a utilizar y se crea la ventana correspondiente
        self.nombre.set('')
        self.ventana_de_nombre = Ventana('200x100')
        self.ventana_de_nombre.title('Modificar nombre')
        #widgets de la ventana
        tag_nombre = Tag(self.ventana_de_nombre, text = 'Ingrese nuevo nombre' )
        tag_nombre.place(relx=0.15, rely=0.10)
        self.cargar_nombre = Entry(self.ventana_de_nombre, textvariable= self.nombre)
        self.cargar_nombre.place(relx= 0.06, rely= 0.28)
        btn_guardar = Boton(self.ventana_de_nombre, text ='Guardar', command = self.cambiar_nombre_cliente)
        btn_guardar.place(relx=0.08, rely=0.55, width=80)
        btn_salir = Boton(self.ventana_de_nombre, text ='Salir', command = self.ventana_de_nombre.destroy)
        btn_salir.place(relx=0.50, rely=0.55, width=80)

    def ventana_apellido(self):
        '''Metodo correspondiente a la ventana de modificacion del apellido de un cliente'''
        #inicialzamos los parametros a utilizar y se crea la ventana correspondiente
        self.apellido.set('')
        self.ventana_de_apellido = Ventana('200x100')
        self.ventana_de_apellido.title('Modificar apellido')
        #widgets de la ventana
        tag_apellido = Tag(self.ventana_de_apellido, text = 'Ingrese nuevo apellido' )
        tag_apellido.place(relx=0.15, rely=0.10)
        self.cargar_apellido = Entry(self.ventana_de_apellido, textvariable= self.apellido)
        self.cargar_apellido.place(relx= 0.06, rely= 0.28)
        btn_guardar = Boton(self.ventana_de_apellido, text ='Guardar', command = self.cambiar_apellido_cliente)
        btn_guardar.place(relx=0.08, rely=0.55, width=80)
        btn_salir = Boton(self.ventana_de_apellido, text ='Salir', command = self.ventana_de_apellido.destroy)
        btn_salir.place(relx=0.50, rely=0.55, width=80)

    def cambiar_nombre_cliente(self):
        '''Metodo que tiene la finalidad de modificar el nombre del cliente'''
        message = self.control.modificacion_nombre_cliente(self.ruc.get(), self.nombre.get())
        if message[0]==1:
            messagebox.showinfo('ADVERTENCIA', message[1], parent = self.ventana_de_nombre)
        else:
            self.info_cliente.config(text=message[1])
            self.nombre.set('')
            self.ventana_de_nombre.destroy()

    def cambiar_apellido_cliente(self):
        '''Metodo que tiene la finalidad de modificar el apellido del cliente'''
        message = self.control.modificacion_apellido_cliente(self.ruc.get(), self.apellido.get())
        if message[0]==1:
            messagebox.showinfo('ADVERTENCIA', message[1], parent = self.ventana_de_apellido)
        else:
            self.info_cliente.config(text=message[1])
            self.apellido.set('')
            self.ventana_de_apellido.destroy()

class Ventana(Toplevel):
    '''Clase para crear las ventanas en el sistema, esta hereda de Toplevel'''
    def __init__(self, size='1200x800'):
        super().__init__()
        super().geometry(size)
        super().config(bg='#F1F2F7')
        super().grab_set()
        super().resizable(0,0)

class Tag(Label):
    '''Clase para crear las etiquetas, esta hereda de Label'''
    def __init__(self,parent, **config):
        Label.__init__(self,parent,**config)
        super().configure(bg='#F1F2F7', fg='black', font= 'Lato 9')

class Boton(Button):
    '''Clase para crear los botones, esta hereda de Button'''
    def __init__(self, parent, size = 180, **config):
        Button.__init__(self, parent, **config)
        self.configure( border= 3 ,fg='black', bg = '#50CFBC', relief='raised', font='Lato 9')
        self.place(width=size)

class BotonRedondo(Radiobutton):
    '''Clase para crear los botones de seleccion, esta hereda de Radiobutton'''
    def __init__(self, parent, **config):
        Radiobutton.__init__(self, parent, **config)
        super().configure(bg= '#50CFBC', font='Lato 9')

if __name__ == '__main__':
    pass