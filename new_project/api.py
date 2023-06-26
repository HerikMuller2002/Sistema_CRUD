from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_session import Session
from utils.database import get_databases, get_table, update_table
from utils.keys import generate_secret_key

app = Flask(__name__)
app.config['SECRET_KEY'] = generate_secret_key()
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
CORS(app)

@app.route('/get_databases', methods=['GET'])
def get_databases_route():
    databases = get_databases()
    return jsonify(databases)

@app.route('/select_table', methods=['POST'])
def select_table_route():
    global table
    data = request.json
    database_name = data['database_name']
    table_name = data['table_name']
    table = get_table(database_name,table_name)

@app.route('/get_table', methods=['GET'])
def get_table_route():
    return jsonify(table)

@app.route('/update_table', methods=['POST'])
def update_table_route():
    data = request.json
    database_name = data['database_name']
    table_name = data['table_name']
    updated_table = data['table']
    update_table(database_name, table_name, updated_table)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5050, debug=True)
