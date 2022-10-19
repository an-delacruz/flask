from os import abort
from flask import Flask,render_template
import logging
from werkzeug.exceptions import abort


app = Flask(__name__)

logging.basicConfig(filename='error.log',level=logging.DEBUG)
@app.route('/')

def hello_world():
    app.logger.debug('Entramos a hello_world, path /')
    return "<p>Hello, World!</p>"


@app.route("/saludar/<nombre>", methods=['GET', 'POST'])
def saludar(nombre):
    return f'Saludos {nombre}'

@app.route("/edad/<int:edad>",methods=['GET'])
def edad(edad):
    return f'Edad: {edad}'

@app.route("/salir")
def salir():
    return abort(404)

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('404.html',error=error),404
    