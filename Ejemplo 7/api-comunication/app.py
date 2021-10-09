from flask import Flask, jsonify, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/nombre', methods=['GET'])
def getDatos():
    
    return 'Sir Isaac Newton'

@app.route('/suma', methods=['POST'])
def getSuma():
    resultado = int(request.json['n1']) + int(request.json['n2'])
    return str(resultado)

@app.route('/carnet', methods=['GET'])
def getCarnet():
    return jsonify({'carnet': '0000000000'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)