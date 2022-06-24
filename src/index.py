from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import json
from envio_mail import SendEMail, codigo_generado
from geopy.distance import geodesic

vef_code = codigo_generado

correo_inst = ''
contrasena = ''

def es_miembro_unal(correo):
    if '@unal.edu.co' in correo:
        enviar_email = SendEMail()
        enviar_email.send_email_test(correo)
    else:
#El correo no es de la unal
        pass





app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'unaventon'
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])

def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])

def register_page():
    if request.method == 'POST':   
        global correo_inst
        correo_inst = request.form['email']
        global contrasena
        contrasena = request.form['password']
        es_miembro_unal(correo_inst)
        return render_template('auth/register_auth.html')
    else:
        return render_template('auth/register.html')

@app.route('/login', methods=["GET", "POST"])

def login():
    if request.method == 'POST':
        correo_inst = request.form['email']
        contraseña = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM datos_usuario')
        data = cur.fetchall()
        for i in range(0,len(data)):
            if correo_inst==data[i][0]:
                if contraseña==data[i][1]:
                    return redirect('/')
                else:
                    return render_template('auth/login.html')
            else:
                return redirect('/register')
    else:
        return render_template('auth/login.html')


@app.route('/location')

def location():
        return render_template('location.html')


@app.route('/vef_code', methods=['POST'])

def verifica_codigo():
    codigo_a_verificacion = vef_code
    codigo_verificacion = request.form['vef_code']
    while codigo_verificacion != codigo_a_verificacion:
        return render_template('auth/register_auth_fail.html')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO datos_usuario (correo, password) VALUES (%s, %s)' , (correo_inst, contrasena))
    mysql.connection.commit()
    return redirect('/')


@app.route('/get_user_coords', methods=['POST'])

def intento():
    output = request.get_json()
    result = json.loads(output)
    lat = str(result["lat"])
    lon = str(result["lon"])
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO ircampuscarro (lat, lon) VALUES (%s, %s)' , (lat, lon))
    mysql.connection.commit()


@app.route('/ir_al_campus', methods=['POST'])
def ir_al_campus():
    return render_template('ir_al_campus.html')

@app.route('/salir_del_campus', methods=['POST'])
def salir_del_campus():
    return render_template('salir_del_campus.html')

@app.route('/ir_al_campus_carro', methods=['GET', 'POST'])
def ir_al_campus_carro():
    if request.method == 'POST':
        output = request.get_json()
        result = json.loads(output)
        lat = str(result["lat"])
        lon = str(result["lon"])
        nombre_usuario = request.form['nombre']
        celular_usuario = request.form['celular']
        placa_usuario = request.form['placa']
        tarifa_usuario = request.form['tarifa']
        horario_usuario = request.form['horario']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO ircampuscarro (lat, lon, Nombre, celular, placa, tarifa, horario) VALUES (%s, %s, %s, %s, %s, %s, %s)' , (lat, lon, nombre_usuario, celular_usuario, placa_usuario, tarifa_usuario, horario_usuario))
        mysql.connection.commit()
    else:
        return render_template('ir_al_campus_carro.html')


    return render_template('ir_al_campus_carro.html')

@app.route('/salir_del_campus_carro', methods=['POST'])
def salir_del_campus_carro():
    return render_template('salir_del_campus_carro.html')

if __name__ == '__main__':
    app.run(debug=True)
    
