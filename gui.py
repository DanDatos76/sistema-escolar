from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import  uno
import sqlite3
import tkinter.font as tkFont
import  os

conexion=sqlite3.connect("ep4.sqlite")
print(conexion)

cone=conexion
cursor=cone.cursor()
def selec():
    monitor.config(text = "Opción {}".format(opcion.get() ) )

def test():
    MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje

def abrir(self):
        conexion=sqlite3.connect("ep4.sqlite")
        return conexion
  

def Consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql= 'SELECT grado, name, apellido, phone,dni,calle FROM student'
            cursor.execute(sql, student)
            return cursor.fetchall()
        finally:
            cone.close()
            
def Recuperar_todos(self):
        
           
            cursor=cone.cursor()
            sql= 'SELECT grado, name, apellido, phone,dni,calle FROM student'
            cursor.execute(sql)
            return cursor.fetchall()
def hola():
    print ("Hola!")

def impresora():

    os.startfile("esc29.csv", "print")

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
 
    lista_archivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if clave1 in verifica:
            exito_login() #...EJECUTAR FUNCIÓN "exito_login()"
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
        else:
            no_clave() #...EJECUTAR "no_clave()"
    #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
    else:
        no_usuario() #..EJECUTA "no_usuario()".


frame = Tk()
frame.title("     ***  REGISTRO ALUMNOS ESCUELA EP4 *** JOSÉ C PAZ  *** Desarrollado por Dan Datos   ***")
frame.maxsize(1700, 700)
# Hijo de root, no ocurre nada
frame = Frame(frame)  

#Tk.title("SISTEMA DE REGISTRO DE ALUMNOS")

# Empaqueta el frame en la raíz
frame.grid()      

# Como no tenemos ningún elemento dentro del frame, 
# no tiene tamaño y aparece ocupando lo mínimo posible, 0*0 px

# Color de fondo, background


# Podemos establecer un tamaño,
# la raíz se adapta al frame que contiene
frame.config(width=1200,height=750) 
#frame.config(bg="#ECCCC5")          # color de fondo, background
frame.config(cursor="circle ,red")    # tipo de cursor (arrow defecto)
frame.config(relief="ridge")    # relieve del root 
frame.config(bd=15) 
frame.config(pady= 2) 
frame.config(padx= 2)  

def openNewWindow(): 
      
    
    
    newWindow = Toplevel(frame) 
  
    
    
    newWindow.title("DATOS DEL PADRE") 
  
    
    newWindow.geometry("800x400") 
  
    
    Label(newWindow,  
          text ="This is a new window").pack() 
  
  
label = Label(frame,  
              text ="This is the main window") 




def openNewWindow2(): 
      
    
    
    newWindow2 = Toplevel(frame) 
  
    
    
    newWindow2.title("DATOS DE LA MADRE") 
  
    
    newWindow2.geometry("800x400") 
    newWindow2.maxsize(1600, 700)
  
    
    Label(newWindow2,  
          text ="This is a new window")
    
    Label(newWindow2, text="Nombre:",width=20).grid(pady=3,row=0, column=0)
    Label(newWindow2, text="Apellido:",width=20).grid( pady=3, row=0, column=2)
    Label(newWindow2, text="Nacionalidad:",width=12).grid( pady=3, row=0, column=4)
    Entry(newWindow2, width=20).grid(padx=3, row=0, column=1)
    Entry(newWindow2, width=20).grid(padx=3, row=0, column=3)
    Entry(newWindow2, width=12).grid(padx=3, row=0, column=5)

    Label(frame, text="Educación institucional",width=15).grid(pady=3, row=15, column=0)
    ttk.Combobox(frame,width= 20,values= values).grid(pady=3, row=15, column=1)
    #Button(frame, text="Aceptar", width=50).grid(padx=10, pady=10, row=22, column=2, columnspan=2)
    opciones=["Primario","Secundario completo","Secundario incompleto","Terciario","Terciario incompleto","Universitario","Universario incompleto"]
    Label(frame, text="Nivel alcanzado",width=40).grid(pady=3, row=15, column=2)
    ttk.Combobox(frame,width= 20,values= opciones).grid(pady=3, row=15, column=3)





    Label(newWindow2, text="Tipo documento:",width=20).grid(pady=3, row=16, column=0)
    Label(newWindow2, text="Número de documento:",width=20).grid( pady=3, row=16, column=2)

    Entry(newWindow2, width=10).grid(padx=3, row=16, column=1)
    Entry(newWindow2, width=15).grid(padx=3, row=16, column=3)

    Label(newWindow2, text="DOMICILIO",width=20,bg= "black",foreground="white").grid(pady=3, row=17, column=1)


    Label(newWindow2, text="Calle:",width=10).grid(pady=3, row=18, column=0)
    Label(newWindow2, text="Número de vivienda:",width=15).grid( pady=3, row=18, column=2)

    Entry(newWindow2, width=20).grid(padx=3, row=18, column=1)
    Entry(newWindow2, width=10).grid(padx=3, row=18, column=3)

    Label(newWindow2, text="piso:",width=10).grid(pady=3, row=19, column=0)
    Label(newWindow2, text="depto:",width=10).grid( pady=3, row=19, column=2)

    Entry(newWindow2, width=10).grid(padx=3, row=19, column=1)
    Entry(newWindow2, width=10).grid(padx=3, row=19, column=3)


    #Label(frame, text="DATOS DE DOMICILIO").grid(pady=3, row=8, column=2)

    Label(frame, text="Provincia",width=12).grid(pady=3, row=20, column=0)
    Label(frame, text="Distrito:",width=12).grid( pady=3, row=20, column=2)
    Label(frame, text="Localidad",width=30).grid(pady=3, row=20, column=4)

    Entry(frame, width=15).grid(padx=3, row=20, column=1)
    Entry(frame, width=15).grid(padx=3, row=20, column=3)
    Entry(frame, width=15).grid(padx=3, row=20, column=5)


    Label(frame, text="Es jefe de hogar",width=15).grid(pady=3, row=21, column=0)
    ttk.Combobox(frame,width= 12,  values= values).grid(pady=3, row=21, column=1)

     




fontStyle = tkFont.Font(family="Lucida Grande", size=10)
# Comenzamos el bucle de aplicación, es como un while True
Label(frame, text="Nombre:",width=20).grid(pady=3,row=0, column=0)
Label(frame, text="Apellido:",width=20).grid( pady=3, row=1, column=0)

Entry(frame, width=30).grid(padx=3, row=0, column=1)
Entry(frame, width=15).grid(padx=3, row=1, column=1)

Label(frame, text="Tipo documento:",width=20).grid(pady=3, row=2, column=0)
Label(frame, text="Número de documento:",width=20).grid( pady=3, row=3, column=0)

Entry(frame, width=30).grid(padx=3, row=2, column=1)
Entry(frame, width=30).grid(padx=3, row=3, column=1)

Label(frame, text="Nacionalidad:",width=20).grid(pady=3, row=0, column=2)
Label(frame, text="Lugar de nacimiento:",width=20).grid( pady=3, row=1, column=2)

Entry(frame, width=20).grid(padx=3, row=0, column=3)
Entry(frame, width=20).grid(padx=3, row=1, column=3)

Label(frame, text="Celular alternativo:",width=20).grid(pady=3, row=2, column=4)
Label(frame, text="Mail:",width=20).grid( pady=3, row=3, column=4)

Entry(frame, width=20).grid(padx=3, row=2, column=5)
Entry(frame, width=20).grid(padx=3, row=3, column=5)


#Label(frame, text="DATOS DE DOMICILIO").grid(pady=3, row=8, column=2)

Label(frame, text="Teléfono",width=20).grid(pady=3, row=0, column=4)
Label(frame, text="Celular:",width=20).grid( pady=3, row=1, column=4)

Entry(frame, width=20).grid(padx=3, row=0, column=5)
Entry(frame, width=20).grid(padx=3, row=1, column=5)

Label(frame, text="Fecha de nacimiento",width=20).grid(pady=3, row=2, column=2)
Label(frame, text="CUIL:",width=20).grid( pady=3, row=3, column=2)

Entry(frame, width=20).grid(padx=3, row=2, column=3)
Entry(frame, width=20).grid(padx=3, row=3, column=3)
'''
Label(frame, text="",width=30).grid(pady=3, row=4, column=0)
Label(frame, text="",width=30).grid( pady=3, row=5, column=0)

Entry(frame, width=30).grid(padx=3, row=4, column=1)
Entry(frame, width=30).grid(padx=3, row=5, column=1)

Label(frame, text="",width=30).grid(pady=3, row=6, column=0)
Label(frame, text="",width=30).grid( pady=3, row=7, column=0)

Entry(frame, width=30).grid(padx=3, row=6, column=1)
Entry(frame, width=30).grid(padx=3, row=7, column=1)
'''

Label(frame, text="País",width=15).grid(pady=3, row=4, column=0)
Entry(frame, width=20).grid(padx=3, row=4, column=1)

Checkbutton(frame, text='Hermanos').grid(column=0, row=6)
Label(frame, text="Cantidad de hermanos",width=20).grid(pady=3, row=6, column=1)
Entry(frame, width=20).grid(padx=3, row=6, column=2)
Label(frame, text="Cant.que asiste al establecimiento",width=20).grid(pady=3, row=6, column=3)
Entry(frame, width=20).grid(padx=3, row=6, column=4)

Label(frame, text="Cantidad  de hab. en el hogar",width=25).grid(pady=3, row=7, column=0)
Entry(frame, width=20).grid(padx=3, row=7, column=1)
Label(frame, text="Cant. de habitaciones en el hogar",width=30).grid(pady=3, row=7, column=2)
Entry(frame, width=20).grid(padx=3, row=7, column=3)
Label(frame, text="Otra lengua que se hable",width=25).grid(pady=3, row=7, column=4)
Entry(frame, width=20).grid(padx=3, row=7, column=5)

values= ["SI","NO"]
Label(frame, text="Recibe ayuda escolar",width=18).grid(pady=3, row=8, column=0)
ttk.Combobox(frame,width= 20,values= values).grid(pady=3, row=8, column=1)

Label(frame, text="Obra Social",width=15).grid(pady=3, row=8, column=2)
ttk.Combobox(frame,width= 20,values= values).grid(pady=3, row=8, column=3)

Label(frame, text="Inscripto en Plan o Programa",width=22).grid(pady=3, row=9, column=0)
ttk.Combobox(frame,width= 25,values= values).grid(pady=3, row=9, column=1)



Checkbutton(frame, text='AUH').grid(column=0, row=10)

Checkbutton(frame, text='Progresar').grid(column=1, row=10)

Checkbutton(frame, text='Beca para judicializados').grid(column=2, row=10)



Checkbutton(frame, text='Becas por excepción').grid(column=3, row=10)

Checkbutton(frame, text='Otros').grid(column=4, row=10)



Label(frame, text="Medio de transporte que lo acerca al establecimiento",width=40).grid(pady=3, row=11, column=1)
Checkbutton(frame, text='A pié').grid(column=0, row=12)

Checkbutton(frame, text='Ómnibus').grid(column=1, row=12)

Checkbutton(frame, text='Auto particular').grid(column=2, row=12)



Checkbutton(frame, text='Taxi/Remis').grid(column=3, row=12)

Checkbutton(frame, text='Otros').grid(column=4, row=12)

Label(frame, text="DATOS DE LA MADRE",width=30,bg= "black",foreground="white").grid(pady=3, row=13, column=1)


Label(frame, text="Nombre:",width=20).grid(pady=3,row=14, column=0)
Label(frame, text="Apellido:",width=20).grid( pady=3, row=14, column=2)
Label(frame, text="Nacionalidad:",width=12).grid( pady=3, row=14, column=4)
Entry(frame, width=20).grid(padx=3, row=14, column=1)
Entry(frame, width=20).grid(padx=3, row=14, column=3)
Entry(frame, width=12).grid(padx=3, row=14, column=5)

Label(frame, text="Educación institucional",width=15).grid(pady=3, row=15, column=0)
ttk.Combobox(frame,width= 20,values= values).grid(pady=3, row=15, column=1)
#Button(frame, text="Aceptar", width=50).grid(padx=10, pady=10, row=22, column=2, columnspan=2)
opciones=["Primario","Secundario completo","Secundario incompleto","Terciario","Terciario incompleto","Universitario","Universario incompleto"]
Label(frame, text="Nivel alcanzado",width=40).grid(pady=3, row=15, column=2)
ttk.Combobox(frame,width= 20,values= opciones).grid(pady=3, row=15, column=3)





Label(frame, text="Tipo documento:",width=20).grid(pady=3, row=16, column=0)
Label(frame, text="Número de documento:",width=20).grid( pady=3, row=16, column=2)

Entry(frame, width=10).grid(padx=3, row=16, column=1)
Entry(frame, width=15).grid(padx=3, row=16, column=3)

Label(frame, text="DOMICILIO",width=20,bg= "black",foreground="white").grid(pady=3, row=17, column=1)


Label(frame, text="Calle:",width=10).grid(pady=3, row=18, column=0)
Label(frame, text="Número de vivienda:",width=15).grid( pady=3, row=18, column=2)

Entry(frame, width=20).grid(padx=3, row=18, column=1)
Entry(frame, width=10).grid(padx=3, row=18, column=3)

Label(frame, text="piso:",width=10).grid(pady=3, row=19, column=0)
Label(frame, text="depto:",width=10).grid( pady=3, row=19, column=2)

Entry(frame, width=10).grid(padx=3, row=19, column=1)
Entry(frame, width=10).grid(padx=3, row=19, column=3)


#Label(frame, text="DATOS DE DOMICILIO").grid(pady=3, row=8, column=2)

Label(frame, text="Provincia",width=12).grid(pady=3, row=20, column=0)
Label(frame, text="Distrito:",width=12).grid( pady=3, row=20, column=2)
Label(frame, text="Localidad",width=30).grid(pady=3, row=20, column=4)

Entry(frame, width=15).grid(padx=3, row=20, column=1)
Entry(frame, width=15).grid(padx=3, row=20, column=3)
Entry(frame, width=15).grid(padx=3, row=20, column=5)


Label(frame, text="Es jefe de hogar",width=15).grid(pady=3, row=21, column=0)
ttk.Combobox(frame,width= 12,  values= values).grid(pady=3, row=21, column=1)




buttonExample = ttk.Button(frame, text="DATOS DEL PADRE",command=openNewWindow).grid(pady=3, row=24, column=0)
frame.config(bd=15)

buttonExample = ttk.Button(frame, text="DATOS DE LA MADRE",command=openNewWindow2).grid(pady=3, row=24, column=2)
frame.config(bd=15)

opcion = IntVar() # Como StrinVar pero en entero

Radiobutton(frame, text="Opción 1", variable=opcion, 
            value=1, command=selec)
Radiobutton(frame, text="Opción 2", variable=opcion,
            value=2, command=selec)
Radiobutton(frame, text="Opción 3", variable=opcion, 
            value=3, command=selec)

monitor = Label(frame)
monitor.grid()

Button(frame, text = "Clícame", command=test)


leche = IntVar()      # 1 si, 0 no
azucar = IntVar()    # 1 si, 0 no

Label(frame,text="¿Cómo quieres el café?")
Checkbutton(frame, text="Con leche", variable=leche, 
            onvalue=1, offvalue=0)
Checkbutton(frame, text="Con azúcar",variable=leche, 
            onvalue=1, offvalue=0)

#imprimir =ttk.Button("IMPRIMIR",command= impresora)
frame.mainloop() 
#acceder a impresora
#os.startfile("C:/Users/Jdash/Desktop/TestFile.txt", "print")