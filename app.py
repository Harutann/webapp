from flask import Flask, request, render_template
app = Flask(__name__)
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
