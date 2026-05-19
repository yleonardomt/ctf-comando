import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = ""
    if request.method == 'POST':
        direccion = request.form.get('direccion', '')
        # VULNERABILIDAD CRÍTICA: Ejecución de comandos mediante shell=True sin sanitización
        comando = f"ping -c 2 {direccion}"
        try:
            output = subprocess.check_output(comando, shell=True, stderr=subprocess.DEVNULL, timeout=5)
            resultado = output.decode()
        except subprocess.CalledProcessError as e:
            resultado = "ERROR: FALLO EN LA CONEXIÓN CON EL OBJETIVO."
        except subprocess.TimeoutExpired:
            resultado = "ERROR: TIEMPO DE RESPUEBA AGOTADO."
        except Exception:
            resultado = "ERROR: INTERRUPCIÓN EN EL BUS DE DATOS."

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
