from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'SmarTown'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/SmarTown'

mongo = PyMongo(app)


@app.route("/usuarios", methods=['GET'])
def get_all_usuarios():
    usuarios = mongo.db.Usuarios
    output = []
    for usuario in usuarios.find():
        output.append({'nombre': usuario['nombre'],
            "edad": usuario['edad'],
            "fecha_nacimiento": usuario['fecha_nacimiento'],
            "estado_civil": usuario['estado_civil'],
            "genero": usuario['genero'],
            "pareja": usuario['pareja'],
            "ciudad": usuario['ciudad'],
            "estado": usuario['estado'],
            "pais": usuario['pais'],
            "tags": usuario['tags']})

    return jsonify(output)

@app.route("/usuarios", methods=['POST'])
def post_usuario():
    usuarios = mongo.db.Usuarios
    usuario_nuevo = ({
    "nombre_completo": request.json['nombre_completo'],
    "anio_nacimiento": request.json['anio_nacimiento'],
    "correo": request.json['correo'],
    "pais": request.json['pais'],
    "estado": request.json['estado'],
    "municipio": request.json['municipio'],
    "tags": request.json['tags'],
    "estado_civil": request.json['estado_civil'],
    "pareja": request.json['pareja'],
    "tipo_usuario": request.json['tipo_usuario']
    })
    #cosas despues

    usuario_id = usuarios.insert(usuario_nuevo)

    nuevo_usuario = usuarios.find_one({'_id':usuario_id})

    usuario_creado = {
    "nombre_completo": nuevo_usuario['nombre_completo'],
    "anio_nacimiento":nuevo_usuario['anio_nacimiento'],
    "correo": nuevo_usuario['correo'],
    "pais": nuevo_usuario['pais'],
    "estado": nuevo_usuario['estado'],
    "municipio": nuevo_usuario['municipio'],
    "tags": nuevo_usuario['tags'],
    "estado_civil": nuevo_usuario['estado_civil'],
    "pareja": nuevo_usuario['pareja'],
    "tipo_usuario": nuevo_usuario['tipo_usuario']
    }

    return jsonify({'result': usuario_creado})


if __name__ == '__main__':
    app.run(debug=True)
