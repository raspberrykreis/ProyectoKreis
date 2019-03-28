from Tkinter import *
from Autenticacion.Autenticacion import *
import RPi.GPIO as GPIO
import threading
import Queue

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12,0)

#Funcion para generar la ventana que pregunta por los ITEM de seguridad
def GeneraVentanadeSeguridad():
	VentanaSeguridad=Toplevel()
	VentanaSeguridad.geometry("600x400")
	VentanaSeguridad.title("Elemento de Seguridad")
	labelSeguridad=Label(VentanaSeguridad,text ="Por favor responda las siguientes preguntas")
	labelSeguridad.place(x=20,y=20)
	button1=Button(VentanaSeguridad,text="Continuar",command=GeneraVentanaSensores)
	button1.place(x=160,y=105)
#Funcion para generar la ventana que permitira ver los valores de los sensores
def GeneraVentanaSensores():
	VentanaSensores=Toplevel()
	VentanaSensores.geometry("600x400")
	VentanaSensores.title("Medicion de Sensores")
	labelSeguridad=Label(VentanaSensores,text ="Estos son los sensores del Sistema")
	labelSeguridad.grid(row=0,column=2)
	labelVelocidad=Label(VentanaSensores,text="Velocidad")
	labelVelocidad.grid(row=1,column=1)
	labelGx=Label(VentanaSensores,text="Gx")
	labelGx.grid(row=2,column=1)
	labelGy=Label(VentanaSensores,text="Gy")
	labelGy.grid(row=3,column=1)
	labelGz=Label(VentanaSensores,text="Gz")
	labelGz.grid(row=4,column=1)
	NombreUser=Label(VentanaSensores,text="Nombre del Usuario")
	NombreUser.grid(row=20,column=1)
	
#Ventana Principal esta mostrara el logo Kreis y esperara el usurario se autentique para seguir la aplicacion
#raiz=Tk()
#imagenKreis=PhotoImage(file="/home/pi/Desktop/ProyectoKREIS/kreis.png")
#raiz.geometry("600x400")
#raiz.title("PROYECTO KREIS")
#raiz.resizable(0,0)
#raiz.config(bg="white")
#Label(raiz,image=imagenKreis).place(x=160,y=105)

#esta linea va a ser reemplazada por la funcion de autenticacion RFID
Autenticacion=Button(raiz,text="Autenticacion", command=GeneraVentanadeSeguridad)
Autenticacion.place(x=220,y=300)

#hiloLeerRFID=threading.Thread(target=LeerRFID)
#hiloLeerRFID.start()
#hiloLeerRFID

#if Leido:
#AutenticadoR=Autenticar()
#if AutenticadoR==False:
	#labelAutenticado=Label(raiz,text="No Autenticado")
	#labelAutenticado.grid(row=1,column=1)
#else:
	#labelAutenticado=Label(raiz,text="Autenticado")
	#labelAutenticado.grid(row=1,column=1)


class GuiPart:
    def __init__(self, master, queue, endCommand):
        self.queue = queue
        # Set up the GUI
        console = Tkinter.Button(master, text='Done', command=endCommand)
        console..place(x=0,y=0)

		raiz=Tk()
		imagenKreis=PhotoImage(file="/home/pi/Desktop/ProyectoKREIS/kreis.png")
		raiz.geometry("600x400")
		raiz.title("PROYECTO KREIS")
		raiz.resizable(0,0)
		raiz.config(bg="white")
		Label(raiz,image=imagenKreis).place(x=160,y=105)

        # Add more GUI stuff here depending on your specific needs

    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize(  ):
            try:
                msg = self.queue.get(0)
                # Check contents of message and do whatever is needed. As a
                # simple test, print it (in real life, you would
                # suitably update the GUI's display in a richer fashion).
                print msg
            except Queue.Empty:
                # just on general principles, although we don't
                # expect this branch to be taken in this case
                pass

raiz.mainloop()


