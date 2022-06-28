from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import json
from envio_mail import SendEMail, codigo_generado
from geopy.distance import geodesic

vef_code = codigo_generado

correo_inst = ''
contrasena = ''

cords = ''


lat_req = ''
lon_req = ''


def es_miembro_unal(correo):
    if '@unal.edu.co' in correo:
        enviar_email = SendEMail()
        enviar_email.send_email_test(correo)
    else:
#El correo no es de la unal
        pass

def calcular_distancia(cords_set_1, cords_set_2):
    distancia = (str(geodesic(cords_set_1, cords_set_2))).split(' ')
    result = (float(distancia[0]))*1000
    result = float("{:.3f}".format(result))
    return result




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
    global cords
    cords = {lat, lon}

@app.route('/get_user_req_coords', methods=['POST'])

def intento_req():
    output = request.get_json()
    result = json.loads(output)
    global lat_req
    lat_req = result["lat"]
    global lon_req
    lon_req = result["lon"]
    return ""

@app.route('/ubicacion_para_ir_al_campus')
def ubicacion_para_campus():
    return render_template('ir_al_campus_copy.html')



@app.route('/ir_al_campus')
def ir_al_campus():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM ircampuscarro')
    data = cur.fetchall()
    user_current_position = [float(lat_req), float(lon_req)]
    rutas_cercanas = []
    distancia = []
    for i in range(0, len(data)):
        x = data[i][0]
        x = x.split(',')
        check_cords = (float(x[0]), float(x[1]))
        if calcular_distancia(user_current_position, check_cords) <= 1500:
            rutas_cercanas.append(data[i])
            distancia.append(calcular_distancia(user_current_position, check_cords))


        

    
    return render_template('ir_al_campus.html', registros=rutas_cercanas, distancia=distancia)

@app.route('/salir_del_campus')
def salir_del_campus():
    return render_template('salir_del_campus.html')

@app.route('/ir_al_campus_carro', methods=['GET', 'POST'])
def ir_al_campus_carro():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre']
        celular_usuario = request.form['celular']
        placa_usuario = request.form['placa']
        tarifa_usuario = request.form['tarifa']
        horario_usuario = request.form['horario']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO ircampuscarro (cords, Nombre, celular, placa, tarifa, horario) VALUES (%s, %s, %s, %s, %s, %s)' , (cords, nombre_usuario, celular_usuario, placa_usuario, tarifa_usuario, horario_usuario))
        mysql.connection.commit()
    else:
        return render_template('ir_al_campus_carro.html')


    return render_template('ir_al_campus_carro.html')

@app.route('/salir_del_campus_carro', methods=['POST'])
def salir_del_campus_carro():
    return render_template('salir_del_campus_carro.html')

if __name__ == '__main__':
    app.run(debug=True)
    
