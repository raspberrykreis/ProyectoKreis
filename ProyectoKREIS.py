from Tkinter import *
from Autenticacion.Autenticacion import *
import RPi.GPIO as GPIO
import threading


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12,0)
def GeneraVentanadeAutenticado():
	VentanaAutenticado=Toplevel()
	VentanaAutenticado.geometry("650x400")
	LabelNombre=Label(VentanaAutenticado,text="BIENVENIDO",font=("Helvetica", 24))
	LabelNombre.place(x=800,y=0)
	VentanaAutenticado.resizable(0,0)
	VentanaAutenticado.config(bg="white")
	Label(VentanaAutenticado,image=imagenKreis).place(x=300,y=50)
	VentanaAutenticado.title("BIENVENIDO")

	button2=Button(VentanaAutenticado,text="Continuar",command=GeneraVentanadeSeguridad,font=("Helvetica", 24))
	button2.place(x=100,y=250)
#Funcion para generar la ventana que pregunta por los ITEM de seguridad
def GeneraVentanadeSeguridad():
	VentanaSeguridad=Toplevel()
	VentanaSeguridad.geometry("650x400")
	VentanaSeguridad.title("Elemento de Seguridad")
	Neumaticos = Checkbutton(VentanaSeguridad, text="Neumaticos", offvalue="L",font=("Helvetica", 36))
	Neumaticos.grid(row=1,column=0)
	Aceite = Checkbutton(VentanaSeguridad, text="Aceite ", offvalue="L",font=("Helvetica", 36))
	Aceite.grid(row=2,column=0)
	Luces = Checkbutton(VentanaSeguridad, text="Luces", offvalue="L",font=("Helvetica", 36))
	Luces.grid(row=3,column=0)
	Cinturon= Checkbutton(VentanaSeguridad, text="Cinturon", offvalue="L",font=("Helvetica", 36))
	Cinturon.grid(row=4,column=0)
	labelSeguridad=Label(VentanaSeguridad,text ="Por favor responda las siguientes preguntas",font=("Helvetica", 36))
	labelSeguridad.grid(row=0,column=0)
	button1=Button(VentanaSeguridad,text="Continuar",command=GeneraVentanaSensores,font=("Helvetica", 36))
	button1.grid(row=6,column=0)
#Funcion para generar la ventana que permitira ver los valores de los sensores
def GeneraVentanaSensores():
	VentanaSensores=Toplevel()
	VentanaSensores.geometry("650x400")
	VentanaSensores.title("Medicion de Sensores")
	labelSeguridad=Label(VentanaSensores,text ="Estos son los sensores del Sistema",font=("Helvetica", 24))

	labelSeguridad.grid(row=0,column=0)
	labelVelocidad=Label(VentanaSensores,text="Velocidad",font=("Helvetica", 36))
	labelVelocidad.grid(row=1,column=0)
	labelGx=Label(VentanaSensores,text="Gx",font=("Helvetica", 36))
	labelGx.grid(row=2,column=0)
	labelGy=Label(VentanaSensores,text="Gy",font=("Helvetica", 36))
	labelGy.grid(row=3,column=0)
	labelGz=Label(VentanaSensores,text="Gz",font=("Helvetica", 36))
	labelGz.grid(row=4,column=0)
	NombreUser=Label(VentanaSensores,text="Nombre del Usuario",font=("Helvetica", 36))
	NombreUser.grid(row=5,column=0)
	HorometroMaquina=Label(VentanaSensores,text="Hora de Uso maquina",font=("Helvetica", 36))
	HorometroMaquina.grid(row=6,column=0)
	HorometroUsuario=Label(VentanaSensores,text="Hora de Manejo Usuario",font=("Helvetica", 36))
	HorometroUsuario.grid(row=7,column=0)
	
#Ventana Principal esta mostrara el logo Kreis y esperara el usurario se autentique para seguir la aplicacion
raiz=Tk()
imagenKreis=PhotoImage(file="/home/pi/Desktop/ProyectoKREIS/kreis.png")
raiz.geometry("650x400")
raiz.title("PROYECTO KREIS")
raiz.resizable(0,0)
raiz.config(bg="white")

Label(raiz,image=imagenKreis).place(x=300,y=0)

#esta linea va a ser reemplazada por la funcion de autenticacion RFID
Autenticacion=Button(raiz,text="Autenticacion", command=Autenticar,font=("Helvetica", 24))
Autenticacion.place(x=100,y=250)
Autenticadob=Button(raiz,text="Autenticado?", command=GeneraVentanadeAutenticado,font=("Helvetica", 24))
Autenticadob.place(x=400,y=250)
#hiloLeerRFID=threading.Thread(target=LeerRFID)
#hiloLeerRFID.start()
#hiloLeerRFID



raiz.mainloop()


