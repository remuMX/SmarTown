from flask import Flask
import Usuarios

app = Flask(__name__)


@app.route("/add", method)
def AddUsuario(object):
    return Usuarios.add(object)


if __name__ == '__main__':
    app.run(debug=True)

