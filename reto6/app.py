from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)

# La información clasificada reside en el entorno de configuración interno del sistema
app.config['FLAG_T4CT1C4'] = 'COMANDO{SST1_M0T0R_D3_PL4NT1LL4S_C0MPR0M3T1D0}'
app.config['ESTADO_RADAR'] = 'ACTIVO'
app.config['PROTOCOLO'] = 'DEFCON-3'

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        parametro = request.form.get('parametro', '')
        try:
            # El motor procesa la entrada dinámicamente antes de enviarla a la vista
            resultado = render_template_string(parametro)
        except Exception:
            resultado = "ERROR: EXCEPCIÓN EN EL MOTOR DE PROCESAMIENTO CENTRAL."
            
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
