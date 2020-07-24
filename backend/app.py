from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
import yaml
import datetime

# Instancia de nuestra aplicacion Flask
app = Flask(__name__)
CORS(app, resources={r"/*" : {"origins" : '*' } })

# Credenciales de la base de datos
database_credentials   = yaml.load(open('database.yaml'), Loader=yaml.FullLoader)

# Configurar nuestro servidor con las credenciales de la BD
app.config['MYSQL_HOST']        = database_credentials['mysql_host']
app.config['MYSQL_USER']        = database_credentials['mysql_user']
app.config['MYSQL_PASSWORD']    = database_credentials['mysql_password']
app.config['MYSQL_DB']          = database_credentials['mysql_database']

# Instancia a la base de datos
mysql_instance  = MySQL(app)

# Endpoint para agendar una cita
@app.route('/agendar-cita', methods=['POST'])
def asignar_citas():

    # Guarda nuestros datos del frontend
    citas   = {
        'nombre': request.json['nombre'],
        'apellido': request.json['apellido'],
        'num_doc': request.json['numDoc'],
        'edad': request.json['edad'],
        'telefono': request.json['telefono'],
        'email': request.json['email'],
        'fecha_consulta': "123",
        'hora_consulta': "123",
        'motivo': request.json['motivo'],
        'now' : datetime.datetime.now()
    }
    
    # Abre la conexión con la base de datos
    cursor = mysql_instance.connection.cursor()

    # Ejecuta el SQL
    cursor.execute("""
        INSERT INTO citas (
            fecha_citas, 
            hora_citas, 
            nombre_usuario_citas, 
            apellido_usuario_citas, 
            telefono_usuario_citas, 
            email_usuario_citas, 
            documento_usuario_citas, 
            edad_usuario_citas, 
            motivo_citas,
            creacion_cita_timestamp
        )  VALUES (
            %(fecha_consulta)s, 
            %(hora_consulta)s, 
            %(nombre)s, 
            %(apellido)s, 
            %(telefono)s, 
            %(email)s, 
            %(num_doc)s, 
            %(edad)s, 
            %(motivo)s,
            %(now)s);
        """, citas)
        
    # Actualiza la conexión
    mysql_instance.connection.commit()
    # Cierra la conexión
    cursor.close()

    # Envía un mensaje de creación
    return jsonify({ "mensaje" : "La cita se ha guardado correctamente" })

# Endpoint para ver todas las citas guardadas en la BD
@app.route('/ver-citas', methods=['GET'])
def ver_citas():
    # Abre la conexión con la base de datos
    cursor = mysql_instance.connection.cursor()

    # Selecciona todas las citas de la tabla "citas"
    cursor.execute('SELECT * FROM citas;')

    # Convierte todos los valores de la base de datos a objetos de python
    result = cursor.fetchall()

    mysql_instance.connection.commit()
    cursor.close()
    
    return jsonify(result)


if __name__ == '__main__':
    # App corra
    app.run(debug=True)