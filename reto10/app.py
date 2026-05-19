import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    c = conn.cursor()
    # Tabla de usuarios normal
    c.execute('CREATE TABLE activos (id INTEGER, nombre TEXT)')
    # Tabla donde reside la FLAG secreta
    c.execute('CREATE TABLE boveda_seguridad (secreto TEXT)')
    c.execute("INSERT INTO activos VALUES (1, 'SISTEMA_CENTRAL')")
    c.execute("INSERT INTO boveda_seguridad VALUES ('COMANDO{BL1ND_SQL1_M4ST3R_B0L}')")
    conn.commit()
    return conn

db = init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = ""
    if request.method == 'POST':
        activo_id = request.form.get('id', '')
        c = db.cursor()
        try:
            # VULNERABILIDAD: Inyección ciega en el ID
            query = f"SELECT nombre FROM activos WHERE id = {activo_id}"
            c.execute(query)
            result = c.fetchone()
            if result:
                mensaje = "ESTADO: ACTIVO LOCALIZADO"
            else:
                mensaje = "ESTADO: NO ENCONTRADO"
        except:
            # El error es genérico para no dar pistas de SQL
            mensaje = "ESTADO: ERROR DE PROCESAMIENTO"
            
    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)
