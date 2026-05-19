from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # El sistema captura el parámetro de búsqueda para la intercepción
    query = request.args.get('objetivo', '')
    
    # Renderizamos la plantilla pasando el input directamente (Vulnerable a XSS)
    resp = make_response(render_template('index.html', query=query))
    
    # La FLAG se oculta simulando ser un token de sesión de grado militar en las cookies
    resp.set_cookie('auth_token_ciberespacio', 'COMANDO{XSS_T4CT1C0_1NT3RC3PT4D0}')
    
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
