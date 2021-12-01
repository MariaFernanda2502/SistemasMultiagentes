from flask import Flask, jsonify
app = Flask(__name__, static_url_path='') #nuevo objeto


@app.route('/update/<string:valor>') #wrap o un decorador
def index(valor):
    num = float(valor) + .001
    return jsonify({'valor': num})

@app.route('/update2/<string:valor>') #wrap o un decorador
def index2(valor):
    num = float(valor) - .001
    return jsonify({'valor': num})

if __name__ == "__main__":
    app.run(debug=True) 