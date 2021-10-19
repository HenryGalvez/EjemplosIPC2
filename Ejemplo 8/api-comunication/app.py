from flask import Flask
from flask_cors import CORS

from routes.todo import todos

app = Flask(__name__)
CORS(app)

@app.route('/')
def getDatos():
    return 'Sir Isaac Newton'

app.register_blueprint(todos, url_prefix='/api/todo')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)