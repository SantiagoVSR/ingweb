#archivo para conexion a base de datos
import pymysql
#parametros de conexion
conn = pymysql.connect(host='localhost', user='root', passwd='', database='universidad', port=3306)


def consultar_modalidades():
    cursor=conn.cursor()
    cursor.execute('Select * from modalidad')
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila[1])
    conn.close


consultar_modalidades()

def consultar_carreras():
    cursor=conn.cursor()
    cursor.execute('Select * from carrera')
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila[0],fila[1],fila[2],fila[3])
    conn.close


def insertar_carreras():
    cursor=conn.cursor()
    cursor.execute("Insert into carrera (codigo, nombre, universidad, id_modalidad) value('1006', 'computacion', 'UTPL', 3);")
    conn.commit
insertar_carreras()
consultar_carreras()