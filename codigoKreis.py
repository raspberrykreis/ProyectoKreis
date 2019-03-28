from Tkinter import *
import Tkinter as tk
import MFRC522
import RPi.GPIO as GPIO
import time
import MySQLdb
from MPU6050 import *
#Prueba Thikspeak
import urllib2
import sys
myapi='TBTXMSKFZ8SJMPJ9'
baseurl	='https://api.thingspeak.com/update?api_key=%s'%myapi
######


ReleKill=37
ReleP=36
botonsi=38
botonno=40
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 
GPIO.setup(ReleP,GPIO.OUT)
GPIO.setup(ReleKill,GPIO.OUT)
GPIO.setup(botonsi,GPIO.IN)
GPIO.setup(botonno,GPIO.IN)

class Aplicacion():
    def __init__(self):
        self.Dicc_Preg={1:'pregunta1',2:'Pregunta2',3:'Pregunta3',4:'Pregunta4',5:'Pregunta5',6:'Pregunta6',7:'Pregunta7',8:'Pregunta8',9:'Pregunta9',10:'Pregunta10'}
        self.Dicc_Resp={0:'Respuestas'}
        self.Cant_Preg=4
        self.valorms=500
        self.valorpms=500
        self.idequipo="KS000"		#PONER AQUI EL NOMBRE DEL EQUIPOO
        self.textolabel1="Ahora SI"
        self.textoPregunta=""
        self.textoRespSI="SI"
        self.textoRespNO="NO"
        self.colorlabel1="RED"
        self.eventoecendido=1
        self.eventoShock=6
        self.valornull=0
        self.UsuarioOK=False
        self.card_id=""
        self.cardvalida=False
        self.checkvalido=False
        self.thresholdShock=60 #este numero hay que calibrarlo con prueba/ estudio de cual es el valor de shock n permitido
        self.root=tk.Tk()
        self.root.geometry("480x320")
        self.root.resizable(0,0)
        self.root.config(bg="white")
        self.root.title("KREIS")
        self.Label1=tk.Label(self.root,text=self.textolabel1)
        self.Label1.grid(column=0,row=0)
        self.imagenKreis=PhotoImage(file="/home/pi/Desktop/ProyectoKREIS/kreis.png")
        self.imgKreis=Label(self.root,image=self.imagenKreis)
        self.imgKreis.place(x=100,y=59)
        self.LeerShock()
        self.checklist()
        self.Autenticar()
        self.puntero=1
        
        self.root.overrideredirect(True)
        self.root.overrideredirect(False)
        self.root.attributes('-fullscreen',True)   
        GPIO.output(ReleKill,1)
        GPIO.output(ReleP,1)
        
        self.root.mainloop()
 
		
    def checklist(self):
		if self.cardvalida==True and self.checkvalido==False:
			print self.puntero
			self.textoPregunta=self.Dicc_Preg.get(self.puntero)#Busca en el diccionaio la pregunta correspondiente
			self.LabelPregunta=tk.Label(self.root,text=self.textoPregunta)
			self.LabelPregunta.place(x=100,y=100)
			self.LabelPregunta1=tk.Label(self.root,text=self.textoRespNO)
			self.LabelPregunta1.place(x=365,y=300)
			self.LabelPregunta2=tk.Label(self.root,text=self.textoRespSI)
			self.LabelPregunta2.place(x=100,y=300)
			if GPIO.input(botonsi):
				print "Pregunta1SI"
				self.Dicc_Resp.update({self.puntero:'SI'})
				if self.puntero>=self.Cant_Preg:
					self.checkvalido=True
					self.LabelPregunta.place_forget()
				self.puntero+=1
			if GPIO.input(botonno):
				self.Dicc_Resp.update({self.puntero:'NO'})
				print "Pregunta1NO"
				if self.puntero>=self.Cant_Preg:
					self.checkvalido=True
					self.LabelPregunta.place_forget()
					self.LabelPregunta.place_forget()
					self.LabelPregunta.place_forget()

				self.puntero+=1
		print(self.Dicc_Resp)
		self.root.after(self.valorpms,self.checklist)
		
	
		
		
		
    def LeerShock(self):
		
		self.root.after(self.valorms,self.LeerShock) #
		if self.checkvalido:
			DataShock=LeerMPU6050()
			x="%.2f" %DataShock[0]
			y="%.2f" %DataShock[1]
			z="%.2f" %DataShock[2]
			####
			conn=urllib2.urlopen(baseurl+'&field1=%s&field2=%s&field3=%s'%(x,y,z))
			print conn.read()
			conn.close()
			####
			#print x
			#print y
			#print z
			res= float(x)+float(y)+float(z)
			print res
			if res>self.thresholdShock or res <-1*self.thresholdShock:
				conexion=MySQLdb.connect("localhost","root","test","kreisdb")
				#conexion=MySQLdb.connect("192.168.0.97","kreis","kreis","kreisdb")
				cursor=conexion.cursor()
				self.fecha=time.strftime("%d-%m-%Y")
				self.hora=time.strftime("%H:%M:%S")
				cursor2=conexion.cursor()
				insertar="INSERT INTO `eventos` (`id_evento`, `uid`, `tipo`, `fecha`, `hora`, `id_equipo`, `hora_finalizada`) VALUES (%s,%s,%s,%s,%s,%s,%s);"
				datos=(self.valornull, self.card_id, self.eventoShock, self.fecha, self.hora,self.idequipo, res)
				cursor2.execute(insertar,datos)
				conexion.commit()
				conexion.close()



    def Autenticar(self):
		if self.textolabel1=="ACERQUE SE TARJETA":
			self.textolabel1="IDENTIFIQUESE POR FAVOR"
		else:
			self.textolabel1="ACERQUE SE TARJETA"
		self.Label1.config(text=self.textolabel1, font=("Helvetica",16))
		self.Label1.place(x=90,y=30)
		conexion=MySQLdb.connect("localhost","root","test","kreisdb")
		#conexion=MySQLdb.connect("192.168.0.97","kreis","kreis","kreisdb")
		cursor=conexion.cursor()
		RFID_KREIS=MFRC522.MFRC522()
		(status, TagType)=RFID_KREIS.MFRC522_Request(RFID_KREIS.PICC_REQIDL)
		(status,uid)=RFID_KREIS.MFRC522_Anticoll()

		if status== RFID_KREIS.MI_OK:
			
			self.card_id=str(uid[0])+"."+str(uid[1])+"."+str(uid[2])+"."+str(uid[3])+"."+str(uid[4])
			print "UID: " +self.card_id
			consulta= "SELECT nombres FROM user WHERE uid='"+self.card_id+"';"
			cursor.execute(consulta)
			resultado=cursor.fetchall()
			if len(resultado)==0:
				self.cardvalida=False
				print "Usuario no registrado"
				self.root.after(self.valorms,self.Autenticar) 
			else:
				nombre=resultado[0][0]
				print nombre
				self.cardvalida=True
		else:
			self.root.after(self.valorms,self.Autenticar) #SI no lee ningun usuario agende este metodo para hacerlo cada self.valorms
			Leido=False
		if (self.cardvalida):
			self.fecha=time.strftime("%d-%m-%Y")
			self.hora=time.strftime("%H:%M:%S")
			self.Label1.config(text="OPERADOR:"+nombre, font=("Helvetica",16))
			cursor1=conexion.cursor()
			insertar="INSERT INTO `eventos` (`id_evento`, `uid`, `tipo`, `fecha`, `hora`, `id_equipo`, `hora_finalizada`) VALUES (%s,%s,%s,%s,%s,%s,%s);"
			datos=(self.valornull, self.card_id, self.eventoecendido, self.fecha, self.hora,self.idequipo, self.hora)
			cursor1.execute(insertar,datos)
			conexion.commit()
			conexion.close()
            #print o label.config ha accedido date+time
			Autenticado=True
			GPIO.output(ReleKill,0)
		else:
			Autenticado=False
			GPIO.output(ReleKill,1)
		
		return Autenticado

aplicacion=Aplicacion()
