from os import abort
from werkzeug.utils import redirect
from flask import Flask, jsonify,render_template, request,session, url_for
import logging
from werkzeug.exceptions import abort


app = Flask(__name__)

app.secret_key = "123"
logging.basicConfig(filename='error.log',level=logging.DEBUG)

@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario ha hecho sesión {session["username"]}'
    else:
        return redirect(url_for('login'))
    # app.logger.debug('Entramos a hello_world, path /')
    # return "<p>Hello, World!</p>"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        usuario = request.form['username']
        session['username'] = usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')
  
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))
  
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
    
@app.route("/juego",methods=["POST"])
def insertarJuego():
    token = request.headers.get('token')
    app.logger.debug('Token',token)
    info=request.get_json()
    nombre = info["nombre"]
    precio = info["precio"]
    calificacion = info["calificacion"]
    return f'El juego {nombre} tiene un precio de {precio} y una calificación de {calificacion}'

@app.route('/juego/<int:id>')
def mostrarJuego(id):
    valores = {'nombre':'FIFA',"precio":1200,"calificacion":50,"id":id}
    return jsonify(valores)