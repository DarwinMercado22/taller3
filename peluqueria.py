from flask import Flask, jsonify, request
import pymysql.cursors

transporte = Flask(__name__)

# Conexion de la base de datos
def connection_mysql():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='bd_api',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor)
    return connection


# Crear un usuario
@transporte.route('/usuarios', methods=['POST'])
def create_usuarios():

    data = request.get_json()
    connection = connection_mysql()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO usuarios (nombre, telefono) VALUES (%s, %s)"
            cursor.execute(sql, (data['nombre'], data['telefono']))
            result = cursor.fetchall()
        connection.commit()

    return jsonify({
        'Mensaje': 'Usuario registrado con exito'
    }), 201


# Obtener  los datos
@transporte.route('/usuarios', methods=['GET'])
def get_usuarios():
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = 'SELECT id, nombre, telefono FROM usuarios'
        cursor.execute(sql)
        result = cursor.fetchall()

        return jsonify({
            'Data': result
        }), 200


# Obtener un usuario por su ID
@transporte.route('/usuarios/<int:usuarios_id>', methods=['GET'])
def get_usuarios_by_id(usuarios_id):
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM usuarios WHERE id = %s'
        cursor.execute(sql, (usuarios_id,))
        result = cursor.fetchone()

    if result:
        return jsonify(result), 200
    else:
        return jsonify({'Mensaje': 'Usuario no encontrado'}), 404


# Actualizar un usuario por ID
@transporte.route('/usuarios/<int:usuarios_id>', methods=['PUT'])
def update_usuarios(usuarios_id):
    data = request.json
    nombre = data.get('nombre')
    correo = data.get('telefono')

    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = "UPDATE usuarios SET nombre = %s, telefono = %s WHERE id = %s"
        cursor.execute(sql, (nombre, correo, usuarios_id))
        connection.commit()

    return jsonify({'Mensaje': 'Usuario actualizado'}), 200


# Eliminar  usuario por ID
@transporte.route('/usuarios/<int:usuarios_id>', methods=['DELETE'])
def delete_usuarios(usuarios_id):
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(sql, (usuarios_id))
        connection.commit()

    return jsonify({'Mensaje': 'Usuario eliminado'}), 200


# Crear un estilos
@transporte.route('/estilos', methods=['POST'])
def create_estilos():

    data = request.get_json()
    nombre = data.get('nombre')
    precio = data.get('precio')

    connection = connection_mysql()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO estilos (nombre, precio) VALUES (%s, %s)"
            cursor.execute(sql, (nombre, precio))
        connection.commit()

    return jsonify({
        'Mensaje': 'estilos creado'
    }), 201


#todos los estilos
@transporte.route('/estilos', methods=['GET'])
def get_estilos():
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = 'SELECT id, nombre, precio FROM estilos'
        cursor.execute(sql)
        result = cursor.fetchall()

        return jsonify({
            'Estilos': result
        }), 200


#estilos por su ID
@transporte.route('/estilos/<int:estilos_id>', methods=['GET'])
def get_estilos_id(estilos_id):
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM vehiculo WHERE id = %s'
        cursor.execute(sql, (estilos_id,))
        result = cursor.fetchone()

    if result:
        return jsonify(result), 200
    else:
        return jsonify({'Mensaje': 'estilos no existe'}), 404


# Actualizar estilos por ID
@transporte.route('/estilos/<int:estilos_id>', methods=['PUT'])
def update_estilos(estilos_id):
    data = request.json
    nombre = data.get('nombre')
    precio = data.get('placa')

    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = "UPDATE estilos SET nombre = %s, placa = %s WHERE id = %s"
        cursor.execute(sql, (nombre, precio, estilos_id))
        connection.commit()

    return jsonify({'Mensaje': 'estilos actualizado'}), 200


# Eliminar estilos por ID

@transporte.route('/estilos/<int:estilos_id>', methods=['DELETE'])
def delete_estilos(estilos_id):
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = "DELETE FROM estilos WHERE id = %s"
        cursor.execute(sql, (estilos_id,))
        connection.commit()

    return jsonify({'Mensaje': 'estilos eliminado'}), 200


if __name__ == '__main__':
    transporte.run(debug=True)


