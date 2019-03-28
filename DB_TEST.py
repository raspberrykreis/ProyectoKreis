import MySQLdb
DB_HOST='localhost'
DB_USER='root'
DB_PASS='mysqlroot'
DB_NAME='a'

def run_query(query=''):
	datos=[DB_HST,DB_USER,DB_PASS,DB_NAME]
	conn=MySQLdb.connect(*datos) #Conectar a la base de datos
	cursor=conn.cursor()		#crear un cursor
	cursor.exxecute(query)
	
	if query.upper().startswith('SELECT'):
		data=cursor.fetchall()		#Traer los resultados de un slect
	else:
		conn.commit()			#Hacer efectiva la escritura de datos
		data=Noone
	cursor.close()			#Cerrar el cursor
	conn.close()			#Cerrar la conexion
	
	return data 
