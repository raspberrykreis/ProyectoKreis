import MFRC522
import RPi.GPIO as GPIO
import time
from Tkinter import *
import MySQLdb

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(12, GPIO.OUT)
Leido=False
#def LeerRFID():
	#RFID_KREIS = MFRC522.MFRC522()
	#(status,TagType) = RFID_KREIS.MFRC522_Request(RFID_KREIS.PICC_REQIDL)
	#(status,uid) = RFID_KREIS.MFRC522_Anticoll()
	#if status == RFID_KREIS.MI_OK:
		#Leido=True
	#else:
		#Leido=False

def Autenticar():
	conexion=MySQLdb.connect("localhost","root","test","kreisdb")
	cursor= conexion.cursor()
	CardJoseBordas= [227,214,123,45,99]
	CardPedroDelRio= [137,221,214,42,168]
	Autenticado=False
	Esperando=True
	global tarjeta, nombre


	
	RFID_KREIS = MFRC522.MFRC522()
	(status,TagType) = RFID_KREIS.MFRC522_Request(RFID_KREIS.PICC_REQIDL)
	(status,uid) = RFID_KREIS.MFRC522_Anticoll()
	
	if status == RFID_KREIS.MI_OK:
		card_id = str(uid[0]) + "." + str(uid[1]) + "." + str(uid[2]) + "." + str(uid[3])+ "." + str(uid[4])
		print "UID: " + card_id
		#Leido=True
	#	print("encintre")
		tarjeta=uid
		#print (tarjeta)
		
		consulta="SELECT nombres FROM user WHERE uid='" + card_id + "';" 
		cursor.execute(consulta)
		resultado=cursor.fetchall()
		print resultado
		nombre= resultado[0][0]
		print nombre
		#for fila in resultado:
			#print (fila)
		conexion.commit()
		conexion.close()	
	else:
		Leido=False
	#	print("no encintre")
	
	if len(uid)!=0:
		global fecha, hora
		fecha = time.strftime("%d-%m-%Y")
		hora= time.strftime("%H:%M:%S")
		TextoFecha="Ha accedido a nuestro sistema KREIS el dia  " + fecha
		TextoHora=" a las "+hora
		GPIO.output(12,0)
		print("Tarjeta Reconocida")
		print(TextoFecha + TextoHora)
		Autenticado=True
		raiz=Tk()
		LabelBienvenida=Label(raiz, text=nombre, font=("Helvetica",16))
		LabelBienvenida.place(x=20,y=20)
	else:
		print("No ha reconoocido Tarjeta")
		GPIO.output(12,1)
		Autenticado=False
	#GPIO.cleanup()
	return Autenticado

