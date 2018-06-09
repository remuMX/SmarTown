from flask import Flask
from Logic import Usuarios

app = Flask(__name__)

@app.route("/add")
def AddUsuario(object):
    usuarios = Usuarios()
    return usuarios.add(object)



