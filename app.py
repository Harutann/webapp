from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from test_model import Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Response Data'

@app.route('/another')
def another():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'

@app.route("/users/<user_name>")
def users(user_name):
    return user_name

@app.route('/show_html')
def show_html():
    return render_template('test.html')

@app.route('/exercise')
def show2_html():
    return f'exercise:{request.args.get("my_name")}'

@app.route('/try_rest', methods=['POST'])
def try_rest():
    # リクエストデータをJSONとして受け取る
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json": request_json}
    return jsonify(response_json)

