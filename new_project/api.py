import os
from flask import Flask, jsonify, request, session, render_template
from flask_cors import CORS,cross_origin
from flask_session import Session
from utils.database import get_list_names, get_table, update_table
from utils.keys import generate_secret_key

app = Flask(__name__)
app.config['SECRET_KEY'] = generate_secret_key()
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
CORS(app)

# HTML
@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/admin')
def admin_page():
    session['session_id'] = os.urandom(16).hex()
    return render_template('admin.html')

# API
@app.route('/get_list_names', methods=['GET'])
def get_list_names_route():
    list_names = get_list_names()
    return jsonify(list_names)

@app.route('/get_table', methods=['POST'])
def select_table_route():
    data = request.json
    database_name = data['database_name']
    table_name = data['table_name']
    table = get_table(database_name,table_name)
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
