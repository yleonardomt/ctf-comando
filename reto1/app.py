from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # El usuario por defecto es el 1
    uid = request.args.get('id', '1')
    
    # Si el usuario cambia el parámetro a 2, obtiene la flag (IDOR)
    flag = "COMANDO{1D0R_R3FL3J0_0CULT0_B0L}" if uid == '2' else None
    
    return render_template('index.html', flag=flag, uid=uid)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
