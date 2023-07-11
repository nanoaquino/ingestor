import cx_Oracle
import json
import configparser
import os
from collections import defaultdict

host = ''
user = ''
password = ''
port = ''
sid = ''
path_consultas = ''
oracle_client_path = ''
path_salida_json = ''



class MyConnection(cx_Oracle.Connection):
    
    def __init__(self):
        print("Connecting to database")
        cx_Oracle.init_oracle_client(lib_dir=oracle_client_path)

        dsn = cx_Oracle.makedsn(host=host, port=port, sid=sid) 

        return super(MyConnection, self).__init__(user, password, dsn)



def read_config():
        global host, user, password, port, sid, path_consultas, oracle_client_path, path_salida_json
  
        config = configparser.ConfigParser()
        config.read('people.ini')

        #variables
        host = config['DB']['host']
        user = config['DB']['user']
        password = config['DB']['password']
        port = config['DB']['port']
        sid = config['DB']['sid']
        oracle_client_path = config['DB']['oracle_client_path']
        path_consultas = config['RUTAS']['path_consultas']
        path_salida_json = config['RUTAS']['path_salida_json']




def getConsultas(cur):
        consultas = os.listdir(path_consultas)
        print("cantidad de archivos sql a ejecutar: ", len(consultas))
        for c in consultas:
                json_filename = c.replace(".sql", ".json")
                processData(os.path.join(path_consultas, c),json_filename, cur)


def processData(sql, json_filename, cur):

        #leo el archivos sql
        sql_file = open(sql)
        sql_as_string = sql_file.read()
        sql_file.close()

        try:
                cur.execute(sql_as_string)

                data = {}
                data['item'] = []
                for row in cur:
                        data['item'].append(row[0])


                with open(os.path.join(path_salida_json, json_filename), 'w') as file:
                        #json.dump(data['item'] , file)
                        dict_str0 = str(data['item'])
                        file.write(dict_str0)

                print("Se crea el archivo: " + json_filename)

                with open(os.path.join(path_salida_json, json_filename), "rt") as file:
                        x = file.read()
	
                with open(os.path.join(path_salida_json, json_filename), "wt") as file:
                        x = x.replace("_","")
                        x = x.replace(":null",":\"\"")
                        x = x.replace("'","")
                        x = x.replace("},","},\n")
                        file.write(x)
                file.close()
        except cx_Oracle.IntegrityError as e:
                error_obj, = e.args
                print("Error al ejecutar la consulta")
                print("Error Code:", error_obj.code)
                print("Error Message:", error_obj.message)
                exit()

if __name__ == '__main__':
        print('Json generator changa 1.0')
        read_config()
        con = MyConnection()
        cur = con.cursor()
        getConsultas(cur)

