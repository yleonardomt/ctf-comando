import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # El sistema carga el documento que se le pida por la URL
    doc_name = request.args.get('doc', 'reporte_01.txt')
    base_dir = '/app/documentos/'
    
    # VULNERABILIDAD: Se une la ruta base con el input sin filtrar "../"
    file_path = os.path.join(base_dir, doc_name)
    
    contenido = ""
    try:
        with open(file_path, 'r') as f:
            contenido = f.read()
    except FileNotFoundError:
        contenido = f"ERROR: EL DOCUMENTO '{doc_name}' NO EXISTE EN LA BASE DE DATOS."
    except Exception as e:
        contenido = "ERROR DE LECTURA CLASIFICADA."

    return render_template('index.html', contenido=contenido, doc_name=doc_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
