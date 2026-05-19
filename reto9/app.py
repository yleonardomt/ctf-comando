from flask import Flask, render_template, request, make_response

app = Flask(__name__)

frecuencia_actual = "144.500 MHz"
mensaje_estado = "OPERATIVO - CANAL SEGURO"

@app.route('/', methods=['GET', 'POST'])
def index():
    global frecuencia_actual, mensaje_estado
    flag = None
    
    if request.method == 'POST':
        nueva_frec = request.form.get('frecuencia')
        if nueva_frec == "CIBER-BOL":
            frecuencia_actual = nueva_frec
            mensaje_estado = "FRECUENCIA DE EMERGENCIA ACTIVADA"
            flag = "COMANDO{CSRF_F0RG3RY_T4CT1C4L_BYP4SS}"
        else:
            frecuencia_actual = nueva_frec
            mensaje_estado = "FRECUENCIA ACTUALIZADA"

    return render_template('index.html', 
                           frecuencia=frecuencia_actual, 
                           estado=mensaje_estado, 
                           flag=flag)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)
