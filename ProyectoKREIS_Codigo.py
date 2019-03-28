from Tkinter import *
from Autenticacion.Autenticacion import *
import RPi.GPIO as GPIO
import threading



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12,0)
fecha=""
PreguntarRFID=False
MostrarLabelAut=False
ColorLetra="red"
TextIndicacion=""
class LeerRFID(Frame):
	def __init__(self,parent=None,msecs=1000): # default = 1 second
		Frame.__init__(self,parent)
		self.msecs = msecs
	
		self.repeater()

	def repeater(self): 
		global Aceite,Neumaticos,Luces,Cinturon,BotonNext,LabelAvisoElementos,LabelAvisoAuth,ColorLetra
		PreguntarRFID=Autenticar()
		if PreguntarRFID==False:
			self.after(self.msecs, self.repeater)
			text1="Por favor acerque una tarjeta valida al sensor"
			LabelAvisoAuth=Label(raiz,text=text1, bg=ColorLetra, font=("Helvetica",16))
			LabelAvisoAuth.place(x=20,y=20)
		else:
			#LabelAvisoAuth.place_forget
			#LabelBienvenida=Label(raiz, text=text1, font=("Helvetica",16))
			#LabelBienvenida.place(x=20,y=20)
			#text1="Nombre de Usuario:				"
			#LabelBienvenida=Label(raiz, text=text1, font=("Helvetica",16))
			#LabelBienvenida.place(x=20,y=20)

			#LabelNeumatico=Label(raiz,text="Neumaticos",font=("Heveltica",16))
			#LabelNeumatico.place(x=100,y=59)
			#BotonNematicoSI=Button(raiz,text="SI", command=MostrarAceiteOpcion, font=("Helvetica",))
			#SiNeumatico=Checkbutton(raiz,text="SI", offvalue="L",bg="white",font=("Helvetica",22))
			#SiNeumatico.place(x=370,y=59)
			#NoNeumatico=Checkbutton(raiz,text="NO", offvalue="L",bg="white",font=("Helvetica",22))
			#NoNeumatico.place(x=370,y=109)

			#raiz.title("Elemento de Seguridad")
			#LabelAvisoAuth.place_forget()
			#imgKreis.place_forget()
			#Neumaticos = Checkbutton(raiz, text="Neumaticos", offvalue="L",bg="white",font=("Helvetica", 22))
			#Neumaticos.place(x=100,y=59)
			#Aceite = Checkbutton(raiz, text="Aceite ", offvalue="L",bg="white",font=("Helvetica", 22))
			#Aceite.place(x=100,y=97)
			#Luces = Checkbutton(raiz, text="Luces", offvalue="L",bg="white",font=("Helvetica", 22))
			#Luces.place(x=100,y=136)
			#Cinturon= Checkbutton(raiz, text="Cinturon", offvalue="L",bg="white",font=("Helvetica", 22))
			#Cinturon.place(x=100,y=176)
			BotonNext=Button(raiz,text="SIGUIENTE",command=VentanaSensor,font=("Helvetica", 14))
			BotonNext.place(x=340,y=280)
			#LabelAvisoElementos=Label(raiz,text="Por favor Escoga los elementos",font=("Helvetica",16))
			#LabelAvisoElementos.place(x=20,y=20)
		#Blink labelAutenticacion
		if ColorLetra=="blue":
			ColorLetra="red"
		else:
			ColorLetra="blue"


def VentanaSensor():
	LabelAvisoAuth.place_forget()
	raiz.title("Sensores")
	#Aceite.place_forget()
	#Neumaticos.place_forget()
	#Luces.place_forget()
	#Cinturon.place_forget()
	BotonNext.place_forget()
	#LabelAvisoElementos.place_forget()
	#LabelAvisoSensores=Label(raiz,text="Sensores", bg=ColorLetra,font=("Helvetica",16)).place(x=20,y=20)
	#def RepetirLectura():
		#MPU6050=LeerMPU6050()
		#print(MPU6050)
		#raiz.after(1000,RepetirLectura())

if __name__ == '__main__': 
	raiz=Tk()
	raiz.geometry("480x320")
	raiz.title("PROYECTO KREIS")
	raiz.resizable(0,0)
	raiz.config(bg="white")
	LeerRFID(parent=raiz,msecs=500)
	#LabelAvisoAuth=Label(raiz,text="Por favor acerque una tarjeta valida al sensor", bg=ColorLetra, font=("Helvetica",16))
	#LabelAvisoAuth.place(x=20,y=20)
	imagenKreis=PhotoImage(file="/home/pi/Desktop/ProyectoKREIS/kreis.png")
	imgKreis=Label(raiz,image=imagenKreis)
	imgKreis.place(x=100,y=59)
	raiz.mainloop()


