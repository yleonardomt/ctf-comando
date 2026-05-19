import jwt
import datetime
from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

# CLAVE SECRETA DE GRADO MILITAR (Vulnerable por ser predecible)
SECRET_KEY = "BOLIVIA123"

@app.route('/')
def index():
    token = request.cookies.get('access_token')
    
    if not token:
        # Si no hay token, se asigna uno de rango bajo (cadete)
        payload = {
            "user": "operador_estandar",
            "role": "cadete",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        resp = make_response(render_template('index.html', role="cadete", flag=None))
        resp.set_cookie('access_token', token)
        return resp

    try:
        # El sistema valida el token pero la firma puede ser rota o el payload manipulado
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        role = data.get("role", "cadete")
        
        flag = None
        if role == "general":
            flag = "COMANDO{JWT_T4MP3R1NG_PR1V1L3G3_3SC4L4T10N}"
            
        return render_template('index.html', role=role, flag=flag)
    except:
        return "ERROR: INTEGRIDAD DEL TOKEN COMPROMETIDA. ACCESO DENEGADO.", 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008)
