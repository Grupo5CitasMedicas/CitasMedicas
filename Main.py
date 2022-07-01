from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import Image, ImageTk

raiz = Tk()
#-----configuración de la ventana------------------
raiz.geometry("600x400")
raiz.title("EPS Pepito")
#--------------------------------------------------

#------------------Configuración de Pestañas----------------------
mainPestania = ttk.Notebook(raiz)
mainPestania.pack(fill='both', expand='yes')
pes1 = ttk.Frame(mainPestania)
pes2 = ttk.Frame(mainPestania)
pes3 = ttk.Frame(mainPestania)
mainPestania.add(pes1, text='Agendar Citas')
mainPestania.add(pes2, text='Historial')
mainPestania.add(pes3, text='Información del usuario')
#-------------------------------------------------

#-------------------Pestaña 1---------------------

#-------------------Calendario--------------------
#--------Funciones------------

#----Funcion mostrar------
def mostrar():
    l1.config(text=calendario.get_date())


#-----------------------------

calendario = Calendar(pes1, selectmode='day')
calendario.grid(rowspan=3, columnspan=3, padx=30, pady=30)

#---------Label de verificación-------
l0 =Label(pes1, text="Fecha seleccionada: ")
l0.grid(row=4, column=1)
l1 = Label(pes1)
l1.grid(row=4, column=2)
#---------------------------------------
#---------Boton seleccionar---
selecc = Button(pes1, text="Agendar Cita", command=lambda:mostrar())
selecc.grid(row=0, column=3)
#------------------------------

#---------Boton limpiar-------
limpi = Button(pes1, text="Limpiar Seleeción")
limpi.grid(row=1, column=3)
#------------------------------


#---------------pestaña 2 ---------------
#-------------Funciones--------------
#------------------------------------
#------------Tabla---------------------
tabla = ttk.Treeview(pes2, columns=2)
tabla.grid(rowspan=5, column=0, padx=15, pady=15)
tabla.heading("#0", text="Fecha")
tabla.heading("#1", text="Lugar")
#---------------------------------------


#---------Boton Agregar cita-------
agreg1 = Button(pes2, text="Agendar nueva cita")
agreg1.grid(row=0, column=3)
#------------------------------
#---------Boton limpiar-------
limpi2 = Button(pes2, text="Limpiar")
limpi2.grid(row=1, column=3)
#------------------------------

#---------Pestaña 3-----------------
#----------funciones----------
#-----------------------------

#----------Columna 1--------

lFoto=Label(pes3, text="Foto de perfil")
lFoto.grid(row=0, column=0, padx=10, pady=10)

Foto = Image.open('72648.png')
new_foto = Foto.resize((36,36))
render = ImageTk.PhotoImage(new_foto)
lFotoPerfil=Label(pes3, image=render)
lFotoPerfil.image = render
lFotoPerfil.grid(row=1, column=0, padx=5, pady=5)
#--------------------------
#-----------columna 2---------

lName =Label(pes3, text="Nombre: ")
lName.grid(row=0, column=3, padx=10, pady=10)
tName = Entry(pes3)
tName.grid(row = 0, column =4, padx = 10, pady = 10)


lLastName =Label(pes3, text="Apellido: ")
lLastName.grid(row=1, column=3, padx=10, pady=10)
tLastName = Entry(pes3)
tLastName.grid(row = 1, column =4, padx = 10, pady = 10)

lTel =Label(pes3, text="Teléfono: ")
lTel.grid(row=2, column=3, padx=10, pady=10)
tTel = Entry(pes3)
tTel.grid(row=2, column =4, padx = 10, pady = 10)

lAddress =Label(pes3, text="Dirección: ")
lAddress.grid(row=3, column=3, padx=10, pady=10)
tAddress = Entry(pes3)
tAddress.grid(row = 3, column =4, padx = 10, pady = 10)

lSede =Label(pes3, text="Sede de atención: ")
lSede.grid(row=4, column=3, padx=10, pady=10)
tSede = Entry(pes3)
tSede.grid(row = 4, column =4, padx = 10, pady = 10)

lEstado =Label(pes3, text="Estado civil: ")
lEstado.grid(row=5, column=3, padx=10, pady=10)
tEstado = Entry(pes3)
tEstado.grid(row = 5, column =4, padx = 10, pady = 10)

botonActualizar = Button(pes3, text="Actualizar Datos")
botonActualizar.grid(row=6, column=3, columnspan=2, padx=10, pady=10)
botonEliminar = Button(pes3, text="Eliminar Datos")
botonEliminar.grid(row=6, column=4, columnspan=2, padx=10, pady=10)
#-----------------------------------

#-------------columna 3
lCitasP =Label(pes3, text="Citas pendientes: ")
lCitasP.grid(row=0, column=5, padx=10, pady=10)
botonCitas=Button(pes3, text="Historial")
botonCitas.grid(row=0, column=6, columnspan=2, padx=10, pady=10)

lAgendarC =Label(pes3, text="Agendar nueva cita: ")
lAgendarC.grid(row=1, column=5, padx=10, pady=10)
botonAgendar=Button(pes3, text="Agendar")
botonAgendar.grid(row=1, column=6, columnspan=2, padx=10, pady=10)



#------------

raiz.mainloop()