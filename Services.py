from flask import Flask, jsonify
import Usuarios


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/usuarios/get')
def GetUsuarios():
    return jsonify(Usuarios.get())





if __name__ == '__main__':
    app.run(debug=True)

