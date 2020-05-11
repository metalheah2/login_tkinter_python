'''
	Autor : Marco Jhoel Churata Torres
	Fecha : 09 - 05 - 2020
	Nombre : Login_sqlite_Tkinter.py
	Descripcion : Les presento uno de mis primeros programas de escritorio usando Tkinter ...
				  se trata de un pequeño login , conectado a una base de datos 'sqlite' , este pequeño
				  programa tambien nos permitira el registro de nuevos usuarios.
				  Creo q' este programa puede ser mejorado de muchas maneras ... Ojala les sirva de algo :D.
'''

from tkinter import *						
import tkinter as tk	
from PIL import ImageTk,Image			#para manipular imagenes
from tkinter import messagebox as mb	#Nos permite abrir ventanas de mensajes
import sqlite3							#Nos permite conectarnos a una base de datos (sqlite3)

ventana=tk.Tk()
ventana.title("_Mi primer Login_")	#Titulo de la ventana principal
ventana.geometry("280x450+300+250")	#Tamaño de nuestra ventana Principal
	
color='#c5e2f6'			#Codigo HEX del color de fondo usado
ventana['bg']=color		#Definimos nuestra ventana 'bg' con el valor 'color'

Label(ventana,bg=color,text="Login",font=("Arial Black",16)).pack()	#Mostramos texto 'Login'

#Abrir imagen para ventana principal
imagen=Image.open("logo.png")						#Abrimos la imagen 'logo.png'
imagen=imagen.resize((180,180),Image.ANTIALIAS)		#Redimensionamos la imagen a 180x180
photoImg=ImageTk.PhotoImage(imagen)					#Le damos nombre a nuestra imagen redimensionada (photoImg)
panel=tk.Label(ventana,image=photoImg).pack()		#Mostramos la imagen en nuestra ventana
#Abrir imagen para ventana de registro
img_reg=Image.open("logo2.jpg")						#Abrimos la imagen 'rak.jpg'
img_reg=img_reg.resize((100,220),Image.ANTIALIAS)	#Redimensionamos la imagen
photo_reg=ImageTk.PhotoImage(img_reg)				#Le damos nombre a nuestra imagen redimensionada (photo_reg)
#Cajas de nuestra ventana Principal
Label(ventana,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Usuario:'
caja1=Entry(ventana,font=("Arial",10))										#Creamos una caja de texto 'caja1'
caja1.pack()																#Posicion de la 'caja1'
Label(ventana,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Contraseña:'
caja2=Entry(ventana,show="*")												#Creamos la 'caja2' (contraseña)
caja2.pack()																#Posicion de 'caja2'

db=sqlite3.connect('login.db')		#Nos conectamos a nuestra base de datos 'login.db'
c=db.cursor()						#Establecemos un cursor

def login():				#Funcion login ... Nos permitira comprobar 'usuario' y 'contraseña' con la base de datos
	usuario=caja1.get()		#Obtenemos el valor de la 'caja1' (usuario)
	contr=caja2.get()		#Obtenemos el valor de la 'caja2' (contraseña)
	c.execute('SELECT * FROM usuarios WHERE Usuario = ? AND Pass = ?',(usuario,contr))	#Seleccionamos datos '(usuario,contr)'
	if c.fetchall():
		mb.showinfo(title="Login Correcto",message="Usuario y contraseña correctos")		#Mostramos 'Login Correcto'
	else:
		mb.showerror(title="Login incorrecto",message="Usuario o contraseña incorrecto")	#Mostramos 'Login incorrecto'
	#c.close()

def nuevaVentana():							#Funcion nuevaVentana ... Nos permitira el registro de nuevos usuarios
	newVentana=tk.Toplevel(ventana)			#Definimos 'newVentana'
	newVentana.title("Registro de Usuario")	#Le damos el titulo 'Registro de Usuario'
	newVentana.geometry("300x290+800+250")	#Tamaño de la ventana
	newVentana['bg']=color					#Definimos newVentana 'bg' con el valor de 'color'
	
	labelExample=tk.Label(newVentana,text="Registro : ",bg=color,font=("Arial Black",12)).pack(side="top")	#Texto 'Registro'
	panel_reg=tk.Label(newVentana,image=photo_reg).pack(side="left")	#Mostramos la imagen en la posicion 'left' (Izquierda)

	Label(newVentana,text="Nombre : ",bg=color,font=("Arial Black",10)).pack()		#Texto 'Nombre:'
	caja3=Entry(newVentana)															#Creamos 'caja3' (Nombre)
	caja3.pack()
	Label(newVentana,text="Apellidos : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Apellidos'
	caja4=Entry(newVentana)															#Creamos 'caja4' (Apellidos)
	caja4.pack()
	Label(newVentana,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()		#Texto 'Usuario'
	caja5=Entry(newVentana)															#Creamos 'caja5' (Usuario)
	caja5.pack()
	Label(newVentana,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Contraseña'
	caja6=Entry(newVentana,show="*")												#Creamos 'caja6' (Contraseña)
	caja6.pack()	
	Label(newVentana,text="Repita la Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Repita la Contraseña'
	caja7=Entry(newVentana,show="*")															#Creamos 'caja7' 
	caja7.pack()
	def registro():				#Funcion registro ... Nos permitira escribir los datos a nuestra base de datos
		Nombre=caja3.get()		#Obtenemos el valor de 'caja3'
		Apellido=caja4.get()	#Obtenemos el valor de 'caja4'
		Usr_reg=caja5.get()		#Obtenemos el valor de 'caja5'
		Contra_reg=caja6.get()	#Obtenemos el valor de 'caja6'
		Contra_reg_2=caja7.get() #Obtenemos el valor de 'caja7'
		if(Contra_reg==Contra_reg_2):		#Esta condicion nos permite saber si las contraseñas coinciden
			#El siguiente comando es el encargado de insertar los datos obtenidos en el registro
			c.execute("INSERT INTO usuarios values(\'"+Nombre+"\',\'"+Apellido+"\',\'"+Usr_reg+"\',\'"+Contra_reg+"')")
			db.commit()			#Confirmamos los datos
			mb.showinfo(title="Registro Correcto",message="Hola "+Nombre+" "+Apellido+" ¡¡ \nSu registro fue exitoso.")
			newVentana.destroy()		#Cerramos la ventana de registro
		else:	#Se ejecutara si las contraseñas no coinciden
			mb.showerror(title="Contraseña Incorrecta",message="Error¡¡¡ \nLas contraseñas no coinciden.")	#Mostramos un mensaje
		#c.close()		#Nos permite cerrar el cursor ...
		#db.close()
	#El siguiente comando (boton) nos permite llamar ala funcion registro
	buttons=tk.Button(newVentana,text="Registrar ¡",command=registro,bg=color,font=("Arial Rounded MT Bold",10)).pack(side="bottom")
	
Label(ventana,text=" ",bg=color,font=("Arial",10)).pack()		#Solo es una linea vacia ... (lo use para separar el boton) 
Button(text=" ENTRAR ",command=login,bg='#a6d4f2',font=("Arial Rounded MT Bold",10)).pack()		#Boton ==> funcion 'login'
Label(ventana,text=" ",bg=color,font=("Arial Black",10)).pack()
Label(ventana,text="No tienes una cuenta ? : ",bg=color,font=("Arial Black",10)).pack()		#Simple texto
#La siguiente linea (boton) nos llama ala funcion 'nuevaVentana' ==> ( ventana de registro)
boton1=Button(ventana,text="REGISTRO",bg='#a6d4f2',command=nuevaVentana,font=("Arial Rounded MT Bold",10)).pack()

ventana.mainloop()