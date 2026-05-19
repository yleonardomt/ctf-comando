import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    c = conn.cursor()
    c.execute('CREATE TABLE oficiales (usuario TEXT, password TEXT)')
    c.execute("INSERT INTO oficiales VALUES ('general_comandante', 'Alfa_Tango_Supremo_99')")
    conn.commit()
    return conn

conn = init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    flag = None
    error = None
    if request.method == 'POST':
        user = request.form.get('usuario', '')
        pw = request.form.get('password', '')
        c = conn.cursor()
        try:
            # Vulnerabilidad: Inyección SQL directa
            query = f"SELECT * FROM oficiales WHERE usuario='{user}' AND password='{pw}'"
            c.execute(query)
            
            if c.fetchone():
                flag = "COMANDO{SQL1_B4S3_D3_D4T0S_C0MPR0M3T1D4}"
            else:
                error = "CREDENCIALES TÁCTICAS INVÁLIDAS."
        except Exception as e:
            error = "ERROR DE SINTAXIS EN LA DIRECTIVA."

    return render_template('index.html', flag=flag, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
