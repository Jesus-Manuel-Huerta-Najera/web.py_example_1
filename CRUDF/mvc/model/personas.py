import mysql.connector

class Alumnos():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root', 
                password='root',
                host='127.0.0.1',
                port=3306,
                database='students_db'
                )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)

    def select(self):
        try:
            self.connect()
            query = ("SELECT * from alumnos;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r = {
                    'id':row[0],
                    'matricula':row[1],
                    'nombre':row[2],
                    'ap_p':row[3],
                    'ap_m':row[4],
                    'fecha':row[5],
                    'gen':row[6],
                    'estado':row[7]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result
    
    def view(self,id_persona):
        try:
            self.connect()
            query = ("SELECT * from alumnos where id = %s;")
            values = (id_persona,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                r = {
                    'id':row[0],
                    'matricula':row[1],
                    'nombre':row[2],
                    'ap_p':row[3],
                    'ap_m':row[4],
                    'fecha':row[5],
                    'gen':row[6],
                    'estado':row[7]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

    def insert(self, matricula, nombre,ap_p,ap_m,fecha,gen,estado):
        try:
            self.connect()
            query = ("INSERT INTO alumnos (matricula, nombre,ap_p,ap_m,fecha,gen,estado) values(%s,%s,%s,%s,%s,%s,%s);")
            values = (matricula, nombre,ap_p,ap_m,fecha,gen,estado)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self,matricula, nombre,ap_p,ap_m,fecha,gen,estado,id_persona):
        try:
            self.connect()
            query = ("UPDATE alumnos SET matricula=%s, nombre=%s, ap_p=%s,ap_m=%s,fecha=%s,gen=%s,estado=%s WHERE id=%s;")
            values = (matricula, nombre,ap_p,ap_m,fecha,gen,estado,id_persona)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self,id_persona):
        try:
            self.connect()
            query = ("DELETE FROM alumnos where id = %s;")
            values = (id_persona,)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False
'''
objeto = Personas()
objeto.delete(9)
for row in objeto.select():
    print(row)
'''