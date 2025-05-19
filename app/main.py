from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensaje": "¡Servicio telemático en producción!"})

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return jsonify({"saludo": f"Hola, {nombre}. Bienvenido al servicio telemático."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
