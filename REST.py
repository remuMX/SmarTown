from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'SmarTown'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/SmarTown'

mongo = PyMongo(app)

# <editor-fold desc="Usuarios">

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
def add_usuario():
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

# </editor-fold>

# <editor-fold desc="Lugares">


@app.route("/lugares", methods=['POST'])
def add_lugar():
    lugares = mongo.db.Lugares
    lugar_nuevo = ({
        "nombre": request.json['nombre'],
        "ubicacion": request.json['ubicacion'],
        "categoria": request.json['categoria'],
        "tags": request.json['pais'],
        "estado": request.json['estado'],
        "municipio": request.json['municipio'],
        "pais": request.json['estado_civil'],
        "calificacion": request.json['pareja'],
        "opioniones":[]
    })

    lugar_id = lugares.insert(lugar_nuevo)

    lugar_creado = lugares.find_one({"_id": lugar_id})

    lugar_creado ={
        "nombre": lugar_creado['nombre'],
        "ubicacion": lugar_creado['ubicacion'],
        "categoria": lugar_creado['categoria'],
        "tags": lugar_creado['pais'],
        "estado": lugar_creado['estado'],
        "municipio": lugar_creado['municipio'],
        "pais":lugar_creado['estado_civil'],
        "calificacion": lugar_creado['pareja'],
        "opioniones": lugar_creado['opiniones']
    }

    return jsonify({'result':lugar_creado})

@app.route("/lugares", methods=['POST'])
def get_near_by_tags():
    lugares = mongo.db.Lugares
    lugar_nuevo = ({
        "nombre": request.json['nombre'],
        "ubicacion": request.json['ubicacion'],
        "categoria": request.json['categoria'],
        "tags": request.json['pais'],
        "estado": request.json['estado'],
        "municipio": request.json['municipio'],
        "pais": request.json['estado_civil'],
        "calificacion": request.json['pareja'],
        "opioniones": []
    })

    lugar_id = lugares.insert(lugar_nuevo)

    lugar_creado = lugares.find_one({"_id": lugar_id})

    lugar_creado = {
        "nombre": lugar_creado['nombre'],
        "ubicacion": lugar_creado['ubicacion'],
        "categoria": lugar_creado['categoria'],
        "tags": lugar_creado['pais'],
        "estado": lugar_creado['estado'],
        "municipio": lugar_creado['municipio'],
        "pais": lugar_creado['estado_civil'],
        "calificacion": lugar_creado['pareja'],
        "opioniones": lugar_creado['opiniones']
    }

    return jsonify({'result': lugar_creado})



# </editor-fold>


if __name__ == '__main__':
    app.run(debug=True)
