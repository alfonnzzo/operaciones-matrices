from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='py+server')

def sumar(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def multiplicar(a, b):
    filas_a = len(a)
    cols_b  = len(b[0])
    n       = len(b)
    res = [[0.0] * cols_b for _ in range(filas_a)]
    for i in range(filas_a):
        for j in range(cols_b):
            for k in range(n):
                res[i][j] += a[i][k] * b[k][j]
    return res

@app.route('/')
def index():
    return send_from_directory('py+server', 'index.html')

@app.post('/api/suma')
def api_suma():
    data = request.get_json()
    a = data.get('matrizA')
    b = data.get('matrizB')

    if a is None or b is None:
        return jsonify({'error': 'Faltan las matrices.'}), 400

    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return jsonify({'error': 'Las matrices deben tener las mismas dimensiones para sumarse.'}), 400

    resultado = sumar(a, b)
    return jsonify({'resultado': resultado})

@app.post('/api/multiplicacion')
def api_multiplicacion():
    data = request.get_json()
    a = data.get('matrizA')
    b = data.get('matrizB')

    if a is None or b is None:
        return jsonify({'error': 'Faltan las matrices.'}), 400

    cols_a  = len(a[0])
    filas_b = len(b)

    if cols_a != filas_b:
        return jsonify({
            'error': f'Para multiplicar, las columnas de A ({cols_a}) deben ser iguales a las filas de B ({filas_b}).'
        }), 400

    resultado = multiplicar(a, b)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    print('Servidor corriendo en http://localhost:5000')
    app.run(debug=True, port=5000)
